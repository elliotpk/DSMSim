import math
from itertools import combinations, permutations
from collections import deque
import csv
import os
import random
import json

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
                if(validateCombination(combination, bidderList)):  
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
            
        avgPrice = nom / len(combo)     # Compute Jain's fairness index
        nom = nom**2
        denom = denom * len(combo)
        avgDistance /= len(combo)       # Compute avg distance
        
        output.append({'combo':combo, 'fairness':nom/denom, 'avgDistance':avgDistance, 'avgPrice':avgPrice})
        
    sortedOutput = sorted(output, key=lambda i:i['fairness'], reverse=True)        #Sort by fairness
    
    #sortedOutput = sorted(output, key=lambda i:i['avgDistance'], reverse=True)    #Sort by avgDistance
    
    return sortedOutput
    
        

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
    
    combinationData = []
    for i in range(len(buyers)):
        temp = {'buyer':buyers[i],'blocks':combination[i]}
        
        quantity,price,distanceSum = (0,0,0)               # Sum up the distance of sales, sqrt((x2-x1)^2 + (y2-y1)^2)
        
        for block in combination[i]:
            distanceSum += math.sqrt((buyers[i].location[0]-block[1].location[0])**2 + (buyers[i].location[1]-block[1].location[1])**2)
            quantity += block[0].Amount
            price += block[0].Price

        temp['pricePerUnit'] = round(price/quantity, 2)
        temp['distanceSum'] = round(distanceSum, 2)
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
      
# Gen Rand Location works 
def randLocation():
    x= random.randint(0,95144)
    with open('places.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        print(csv_reader)
        rows = list(csv_reader)
        print(rows[x])

def specLocation(city, country):
    with open('places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ny = ",".join(row)
            if ny.__contains__(city+',') == True and ny.__contains__(country+',') == True:
                return ny

print(specLocation("Paris", "France"))
    
    


# finds continent  can also potentially save as variable


   

def list_find(some_list,some_item,find_all=False): 
    
            if (some_item in some_list): 
                if find_all: 
                    index_list = [] 
                    for an_index in range(len(some_list)): 
                        if some_list[an_index] == some_item: 
                            index_list.append(an_index) 
                    return index_list 
                else: 
                    return some_list.index(some_item) 
            else: 
                return None 
        
def Continent(city):

    with open('locations1.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if city in row:
                ny = ", ".join(row)
                print(ny) 

    it_is_at = list_find(ny,"Europe") 
    if (it_is_at != None): 
        print("Europe") 
    else:
        print("America")
