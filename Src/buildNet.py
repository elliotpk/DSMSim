
import math
import csv
import random
import json
import API_Handling
import envCalc
import yaml
import placeClasses
from collections import defaultdict
import itertools
from math import inf

API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'

def internationalRouting():
    
    nationalNets = allNationalNetworks() 
    with open('Database/closest_cities.csv', 'r', newline='', encoding='utf-8') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip header row
        for row in reader:
            country, neighbor, city1, city2, distance =  row[0], row[1], row[2], row[3], row[4]
            nationalNets[country]
                
            
                

def allNationalNetworks():
    countriesWithCities = countryBuilder()
    nationalnetworks = defaultdict(list) 
    for i in range(0, countriesWithCities): 
        country =countriesWithCities[i].name
        cities = countryNet(countriesWithCities[i])
        nationalnetworks[country].append[cities]
    return nationalnetworks
                
    

def cityBuilder(name):
    "Creates a city object"
    x= placeClasses.City(name)
    return x

def countryBuilder():
    "builds a country object that contains relevant city objects, given a structured csv file"
    
    countriesWithCities =[]             # return variable            
    countryList = []
    
    
    with open('Database/varuhus.csv', 'r', newline='', encoding='utf-8') as csvfile:
        
        reader = csv.reader(csvfile)
        
        for row in reader:                              #create temporary list for interaction from csv file
            countryList.append([row[0],row[1]])         #goes through csv file
            
        currentCities = []                              # holds cities in current country
        
        for d in range(0, len(countryList)-1):          # goes through whole list of cities
            
            nowCountry= placeClasses.Country(countryList[d][1])     #creates country object
            
            if countryList[d][1] == countryList[d+1][1]:
            
                currentCities.append(cityBuilder(countryList[d][0]))    # appends city objects to country object
            else:
                nowCountry.cities= currentCities                        # starts new country object
                countriesWithCities.append(nowCountry)                  # bulds on list of country objects
        
    return countriesWithCities 
                
def connectionsScanner(cityObj):
    "returns which delivery-connection should be established"
    
    x= cityObj.connections
    count= 1
    for i in range(len(x)):
        if (x[i] ==None):
            return count
        else: count += 1
    return -1  

def insertion_sort(arr):
    x = []
    for q in range(0, len(arr)):
        x.append(arr[q])
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr   
           
def countryNet(countryObj):
    "takes a single country object and establishes a proximity net which is represented in the connections attribute of the city objects"
    
    cities = countryObj.cities
    countryNet = []
    x= []
    y =[]
    

    for i in range(0, len(cities)):
        
        distanceList = []
        
        for j in range(0, len(cities)):
            distance = API_Handling.Route2(cities[i].name,cities[j].name)
            distanceList.append([distance, cities[j]])
        
        sortedx= sorted(distanceList)                #returns sortedx list of city objects according to of distances from currently researched city
       
        
        for j in range(0, len(sortedx)):
            x =insertion_sort(sortedx)
        
        z= []
        for h in range(0, len(x)):
            z.append(x[h][1].name)
        print(z)
        
        ''' CONTINUE HERE'''
 
        m =[]
        m.append([x[i][1].name])
        for s in range(0, 3):
            m.append([x[s+1][0], x[s+1][1].name])
        y.append(m)
        print(str(i))
        
        origins=defaultdict(list)
        print(x[i][1].name)
        for a in range(0,3):
            origins[x[a][1].name].append([x[a+1][0], x[a+1][1].name])
        
    return y
    
    

x = placeClasses.Country('Sweden')
x.cities=[placeClasses.City("Stockholm"), placeClasses.City("Malmö"), placeClasses.City("Gothenburg"),placeClasses.City("Uppsala"), placeClasses.City("Västerås"), placeClasses.City("Örebro"),placeClasses.City("Linköping"), placeClasses.City("Helsingborg"), placeClasses.City("Jönköping") ]
cities = [placeClasses.City("Umeå"), placeClasses.City("Kiruna"), placeClasses.City("Malmo"),placeClasses.City("Stockholm")]


z= countryNet(x)
print(z)
#print(z)
#for i in range(0, 4):
#    print(str(z[i].connections) + " " + str(z[i].name))

    

                

            
            
      