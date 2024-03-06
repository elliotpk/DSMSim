import math
from itertools import combinations, permutations
from collections import deque
import csv
#import os
import random
#import json
#from Database import API_Handling
import envCalc
import yaml

API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'
configFile = "config.yaml"



def matchMakingCalculation(sellerList, bidderList):
    'Returns list of valid combinations given the current auctioning data'
   
    permNum, permComb = (0,0)                            #init var
    validCombinations = []
   
    blocks = getBlocks(sellerList)          #Get list of blocks for sale
   
    print(f"Beginning matchmaking calculation\n {int((len(blocks) / 2) + 1) * math.comb(len(blocks), len(bidderList))* len(blocks)} combinations to test")


    for perm in permutations(blocks):                               # For every permutation of blocks for sale
        for rot in listRotator(perm):                               # For every Rotation of every permutation of blocks for sale
            for combination in splitfinder(rot, len(bidderList)):   # For every combination of every rotation of every permutation of blocks for sale
                                                                    # This will collect every way all blocks can be allotted to buyers      
                if(validateCombination(combination, bidderList)):   #TODO NEVERTRUE, ?
                    validCombinations.append(formatCombination(combination, bidderList))    # if combination adheres to rules set by auction, validate it
                    
                permComb +=1
        permNum += 1


        print(f"Permutation number {permNum} / {int((len(blocks) / 2) + 1)}\nCombinations tested: {permComb}")
       
        if(permNum > len(blocks)/2): break              #Doesn't this exclude valid combinations?


    if(len(validCombinations) == 0):
        return None
   
    validCombinations = evaluateCombinations(validCombinations)         # sorts either by Fairness or average distance depending on preference.

    return validCombinations


def getBlocks(sellerList):
    "Extract the blocks and sellers and format in handleable manner"
   
    blocks = []
    for seller in sellerList:
        sellerBlockList = seller.LinkOfBlocks.display()
        for block in sellerBlockList:
            blocks.append((block, seller))
    return blocks


def evaluateCombinations(combinations):
    "Function to compute data to sort by such as fairness and avg distance"
   
    output = []
   
    for combo in combinations:  # For each valid set of buyer-block combinations
     
        nom, denom, avgDistance, avgPrice = (0,0,0,0)
       
        for buyerSet in combo:  # Compute Raj Jain's Fairness index variables and Distance sum
            avgDistance += buyerSet['distanceSum']
            nom += buyerSet['pricePerUnit']
            denom += buyerSet['pricePerUnit']**2
            green= buyerSet['eco']  
           
        avgPrice = nom / len(combo)     # Compute Jain's fairness index
        nom = nom**2
        denom = denom * len(combo)
        avgDistance /= len(combo)       # Compute avg distance
        
       
        score= getScore(green, (nom/denom), configFile)
       
        output.append({'combo':combo, 'fairness':nom/denom, 'avgDistance':avgDistance, 'avgPrice':avgPrice, 'score' : score , 'eco' : green})
        print(output[-1])
    
    #sortedOutput = sorted(output, key=lambda i:i['fairness'], reverse=True)        #Sort by fairness
    #sortedOutput = sorted(output, key=lambda i:i['avgDistance'], reverse=True)    #Sort by avgDistance
    sortedOutput = sorted(output, key=lambda i:i['score'], reverse=True)          #Sort by score
    
   
    return sortedOutput
   
       
#TODO currently, this never  returns true

def validateCombination(combination, buyers): # Combination = list with (number of buyers)+1 lists within, each containing (block,seller) tuples, combination[-1] containing "unbought" blocks
    "Function to determine if a combination of blocks is valid"
   
    # Validate if the order of buying blocks is broken
    for block in combination[-1]:
        if(not checkIfPreviousBlockUnbought(block[0], combination[:len(combination)-2])):
            return False


    # Validate if every buyer has a fulfilled need
    for i in range(len(buyers)):
        need = buyers[i].needs
        for block in combination[i]:
            need -= block[0].Amount
        if(need > 0): return False
    return True






def formatCombination(combination, buyers):
    "Process and format combination data to be saved, compute fairness, distance data etc"
    
    ("entered formatCombination")       #This never happens now
    
    combinationData = []
    for i in range(len(buyers)):
        temp = {'buyer':buyers[i],'blocks':combination[i]}
       
        quantity,price,distanceSum = (0,0,0)            # Sum up the distance of sales, sqrt((x2-x1)^2 + (y2-y1)^2)
       
        for block in combination[i]: # TODO Change location in below row to route calc
            
            CityCountryString1 =str(block[1].location)
            CCS1comma = CityCountryString1.find(',')
            City1 = CityCountryString1[:CCS1comma]
            
            CityCountryString2 =str(buyers[i].location)
            CCS2comma = CityCountryString2.find(',')
            City2 = CityCountryString2[:CCS2comma]
            
            x = envCalc.distanceCalc(City1, City2)
            
            '''
            with open('Database/Network_Database/shortest_paths.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['From'] == City1 and row['To'] == City2:
                        x= float(row['Distance'])
            
            
                                                                                ####HÄRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR######################
            '''
            
            
            quantity += block[0].Amount
            price += block[0].Price
            distanceSum += x 
            ecoFriendly = (100 -(x / 225))/100
            

        temp['pricePerUnit'] = round(price/quantity, 2)
        temp['distanceSum'] = round(distanceSum, 2)
        temp['eco'] = ecoFriendly
        combinationData.append(temp)


    return combinationData

def listRotator(inputList):
    'Takes a list and returns every possible rotation of it in an array'


    rotations = len(inputList)
    outputList = []
    inputList = deque(inputList)
    while rotations > 0:
        outputList.append(tuple(inputList))
        inputList.rotate(1)
        rotations -= 1
   
    return outputList


def splitfinder(blocklist, numBuyers):      # blocklist = All the blocks from the sellers arranged in a specific permutation
   
    'Find all possible ways to split the blocks between the buyers (including one "buyer" for unbought blocks)'
    'Assumes that only the "unbought" blocks can be empty since every buyer should have a demand'
   
    possibleSplits = []
    for breakpoints in combinations(range(1, len(blocklist) + 1), numBuyers):  # Combinatorics: find all places to place splitpoints between groups
       
        possibilityN = []
        possibilityN.append(list(blocklist[0 : breakpoints[0]]))               # How does this line work?
       
        for i in range(0, numBuyers - 1):
            possibilityN.append(list(blocklist[breakpoints[i] : breakpoints[i + 1]]))  
       
        possibilityN.append(list(blocklist[breakpoints[(len(breakpoints) - 1)] : (len(blocklist))]))


        possibleSplits.append(list(possibilityN))
       
    return possibleSplits






def checkIfPreviousBlockUnbought(unboughtBlock, boughtBlocks):
    'Checks Recursively if a block that has to be bought in conjunction with another block, was bought on its own'
   
    if unboughtBlock.next() != None:
        for blockset in boughtBlocks:
            for block in blockset:
                if unboughtBlock.next() == block[0]:
                    return False
        return checkIfPreviousBlockUnbought(unboughtBlock.next(), boughtBlocks)
    else:
        return True
     
def randLocation():
    x= random.randint(0,13117) # All cities in activecities.csv
    with open('Database/Network_Database/activecities.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
        return(str(rows[x][1] + ',' +rows[x][4]))
   


def specLocation(city, country):
    with open('Database/Network_Database/worldcities.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ny = ",".join(row)
            if ny.__contains__(city+',') == True and ny.__contains__(country+',') == True:
                return ny
   
   
def getScore(fairness, ecoFriendly, conf): 
    with open(configFile, "r") as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
            ecoProcent = conf.get('ecoPercent', None)
            fairnessProcent = conf.get('fairnessPercent', None)

    fairnessRes = fairness * ecoProcent
    ecoFriendlyRes = ecoFriendly * fairnessProcent
    score = (fairnessRes + ecoFriendlyRes)
    return score
