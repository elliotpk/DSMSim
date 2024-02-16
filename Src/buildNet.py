
import math
import csv
import random
import json
import API_Handling
import envCalc
import yaml
import placeClasses

 API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'


''''

Each country has a local network stored withiin a Country class variable
One route should be established between each neighbouring  country by means of the warehouse closest to the border
make a list of distances from each warehouse to each other warehouse in a country
sort each ciies distances to other cities by top 4, do this in order from most to least populated city in each country.
connect those in local variables connection1...connection.4 or higher if you wish!

for loop that identifies each specific country and runs the following on said country
-   Scanner that searches through  every instance of one specific country in  varuhus.csv
-   Create Country object with country name
-   create City object with city name 
- 
-    ########### RESEARCH  ALL DISTANCES TO OTHER CITIES IN COUNTRY FOR ONE CITY ########
-    from most populated to least populated pick 4 closest, put in connection1...connection4
-   if city you want to add has full connections, skip to next city
-    TEST make sure no city has no delivery routes

###PROBLEMS####

* How to identify best city to neighbouring country
'''

lastconnection = "connection4"                      #if more connections  than 4 are desired, the maximum amount of connections should be inserted here

def buildNet():
    "collects Country networks and connects them"
    return

def cityBuilder(name):
    "Creates a city object"
    x= placeClasses.City(name)
    return x
    
def countryBuilder():
    "builds a country object that contains relevant city objects, given a structured csv file"
    countriesWithCities =[]
    built = []
    with open('Database/places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            count = 0
            
            if (row[1] not in built):
                countryObject= placeClasses.genCountry(row[1])
                countryName = row[1]               
                
                for row in range(count,count + 10000000):           # given an organized cvs file, finds all instances of cities in country.
                    if row[1] != countryName:       
                        break
                    else:
                        countryObject.cities.append(cityBuilder(row[0]))    # appends city objects
 
                built.append(x)
                countriesWithCities.append(countryObject) 
            count += 1
    return countriesWithCities 
    
 def connectionsScanner(cityObj):
    "returns which delivery-connection should be established"
    x= cityObj.connections
    count= 1
    for i in range(len(x)):
        if (i ==None):
            return count
        else: count += 1
    return -1   
    
           
def countryNet(countryObj):
    "takes a single country object and establishes a proximity net which is represented by a list of arrays"
    
    cities = countryObj.cities
    countryNet = []
    

    for i in range(0, len(cities)):
        distanceList = []
        
        for j in range(0, len(cities)):
            
            distance = API_Handling.Route(API_KEY,cities[i],cities[j])
            distanceList.append([cities[j].name, distance])
        
    
        sorted= sorted(distanceList)                #returns sorted range of distances from other cities
        
        '''###PROBLEM  does not ensure that all cities have connections currently PROBLEM ###'''
        
        ''' if closest city is full of connections, establish a connection with their least significant connection, erase previous connection'''
        
      
        for j in range(1, len(sorted)):                                              #the 1 excludes the closest city (itself)
            
            openConnection1 = connectionsScanner(sorted[i])                           #checks for open connection 
            openConnection2 = connectionsScanner(sorted[j])
            name1= "connection" + openConnection1                                     #name1 becomes connection1, connection2, connection3, etc.
            name2 = "connection" + openConnection2                 
            
            if (openConnection1 != -1  and openConnection2 != -1):                    #if both objects have open connections 
                
                if (getattr(sorted[i], name1) == None):                               #checks which connection is open    
                    setattr(sorted[i], name1, sorted[j] )                             # sets  an open connection in city1 to (city2, distance)
                    setattr(sorted[j], name2, ([sorted[i][0], sorted[j][1]]))         # sets connection  in city2 to [city1, distance]

                    list1 = getattr(sorted[i, "connections"])
                    list1[openConnection1] = 1                                        # sets closed flag on object 1 connections
                    setattr(sorted[i], "connections", list1)
                    
                    list2 = getattr([sorted[j], "connections"])                       # # sets closed flag on object 2 connections                    
                    list2[openConnection2] = 1              
                    setattr(sorted[i], "connections", list2 )
            
            
            elif(openConnection2 == -1):                # if the closest city is full of connections
                
                if (getattr(sorted[i], name1) == None):
                    setattr(sorted[i], name1, sorted[j])
                    setattr(sorted[j], lastconnection, ([sorted[i][0], API_Handling.Route(sorted[j].name,sorted[i].name)]))   # replace last connection on city2, so that every city is in network
                    break           # this should only happen to one city   

        countryNet.append(sorted[i])
        
    return countryNet

    
    

                

            
            
      