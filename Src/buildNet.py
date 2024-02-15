
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



def buildNet():
    return
    
def countryBuilder():
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
                        countryObject.cities.append(row[0])
 
                built.append(x)
                countriesWithCities.append(countryObject) 
            count += 1
    return countriesWithCities 

def cityBuilder(name):
    x= placeClasses.City(name)
    return x
    
           
def countryNet(countryObj):
    
    cities = countryObj.cities
    citiesObj = []
    countryNet = []
    
    for i in range(0, len(cities)): 
        scan=cityBuilder(cities[i])  # converts cities from variable to object   
        citiesObj.append(scan)

    for i in range(0, len(citiesObj)):
        distanceList = []
        
        for j in range(0, len(citiesObj)):
            
            distance = API_Handling.Route(API_KEY,citiesObj[i],citiesObj[j])
            distanceList.append([citiesObj[j], distance])
            
            
        '''put smallest nonzero value  in connection 1 , 2nd smallest connection2 etc.'''
        '''### PROBLEM   when a city searches, it should exclude itself, this does not currently happen  PROBLEM ###'''
        
        sorted= sorted(distanceList)                #returns sorted range of distances from other cities
        
        for j in range(0, len(sorted)):                                  
            
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
                    
                    list2 = getattr([sorted[j], "connections"])                        # # sets closed flag on object 2 connections                    
                    list2[openConnection2] = 1              
                    setattr(sorted[i], "connections", list2 )
                    
        countryNet.append(sorted[i])
        
    return countryNet
            
                    
        
                
                
            
def connectionsScanner(cityObj):
    "returns which connection should be established"
    x= cityObj.connections
    count= 1
    for i in range(len(x)):
        if (i ==None):
            return count
        else: count += 1
    return -1

    
    

                

            
            
      