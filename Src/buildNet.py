
import math
import csv
import random
import json
import API_Handling
import envCalc
import yaml
import placeClasses

lastconnection = "connection4"                      #if more connections  than 4 are desired, the maximum amount of connections should be inserted here

API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'


'''
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
    "collects Country networks and connects them"
    return

def cityBuilder(name):
    "Creates a city object"
    x= placeClasses.City(name)
    return x
    
def is_string(variable):
    
    return isinstance(variable, str)

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

def countryBuilder():
    "builds a country object that contains relevant city objects, given a structured csv file"
    countriesWithCities =[]
    built = []
    listCountry = []
    with open('Database/varuhus.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            listCountry.append([row[0],row[1]])
        for d in range(0, len(listCountry)-1):
            if listCountry[d][1] == listCountry[d+1][1]:
                print("same")
            else:
                print("different")
        
            
            #if ny.__contains__(city+',') == True and ny.__contains__(country+',') == True:

            

                               
            #built.append(x)
            #countriesWithCities.append(countryObject) 
            #count += 1
    return "test"#countriesWithCities 
    
            
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
        
        for j in range(1, len(cities)):
            
            distance = API_Handling.Route(API_KEY,cities[i],cities[j])
            distanceList.append([cities[j], distance])
        
        sortedx= sorted(distanceList)                #returns sortedx list of city objects according to of distances from currently researched city
        
        
        ''' ###PROBLEM does not check for multiplicity on second search
                       no distance limit for connections
        
        
        
        
        PROBLEM###'''
        
      
        for j in range(1, len(sortedx)):                                              #the 1 excludes the closest city (itself)

            openConnection1 = connectionsScanner(sortedx[i][0].connections)                           #checks for open connection 
            openConnection2 = connectionsScanner(sortedx[j][0].connections)
            name1= "connection" + openConnection1                                     #name1 becomes connection1, connection2, connection3, etc.
            name2 = "connection" + openConnection2                 
            
            if (openConnection1 != -1  and openConnection2 != -1):                    #if both objects have open connections 
                
                
                if (getattr(sortedx[i], name1) == None 
                    and sortedx[j].name not in getattr(sortedx[i, "connections"])):       # checks which connection is open  and not already connected 
                    
                    setattr(sortedx[i], name1, sortedx[j] )                             # sets  an open connection in city1 to (city2, distance)
                    setattr(sortedx[j], name2, ([sortedx[i][0], sortedx[j][1]]))         # sets connection  in city2 to [city1, distance]

                    list1 = getattr(sortedx[i, "connections"])
                    list1[openConnection1] = sortedx[j].name                            # sets closed flag on object 1 connections with "city2"
                    setattr(sortedx[i], "connections", list1)
                    
                    list2 = getattr([sortedx[j], "connections"])                                         
                    list2[openConnection2] = sortedx[j].name                             # sets closed flag on object 2 connections  with "city1" 
                    setattr(sortedx[i], "connections", list2 )
            
            
            elif(openConnection2 == -1):                # if the closest city is fully connected
                
                if (getattr(sortedx[i], name1) == None):
                    setattr(sortedx[i], name1, sortedx[j])
                    setattr(sortedx[j], lastconnection, ([sortedx[i][0], API_Handling.Route(sortedx[j].name,sortedx[i].name)]))   # replace last connection on city2, so that every city is in network
                    
                    list1 = getattr(sortedx[i, "connections"])
                    list1[openConnection1] = sortedx[j].name                                        # sets closed flag on object 1 connections
                    setattr(sortedx[i], "connections", list1)
                    break           # this should only happen to one city 

        countryNet.append(sortedx[i])
        
    return countryNet


x = placeClasses.Country('Sweden')
x.cities=['Stockholm', 'Gothenburg', 'Malmo','Vasteras']
countryBuilder()
    
    

                

            
            
      