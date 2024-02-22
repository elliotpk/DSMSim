
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

def distance(city1, city2):
    # Dummy distance calculation function based on the index of the cities in the list
    return abs(city1 - city2)

def build_network(city_lists):
    network = {}
    for cities in city_lists:
        for distance, city_name in cities:
            if city_name not in network:
                network[city_name] = {'connections': []}
        
        for city_index, (distance, city_name) in enumerate(cities):
            distances_to_other_cities = [(distance(city_index, i), other_city_name) for i, (other_distance, other_city_name) in enumerate(cities) if other_city_name != city_name]
            sorted_distances = sorted(distances_to_other_cities)
            closest_cities = [city_name for _, city_name in sorted_distances[:4]]
            network[city_name]['connections'] = closest_cities
    return network

def limit_connections(network):
    for city, data in network.items():
        # Ensure each city has at least one connection
        if not data['connections']:
            # Add the closest city as a connection if none exist
            closest_city = min((distance(city, other_city), other_city) for other_city in network.keys() if other_city != city)[1]
            network[city]['connections'].append(closest_city)
        
        # Limit the number of connections to four
        network[city]['connections'] = data['connections'][:4]  

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
    #print(cities)
    countryNet = []
    x= []
    y =[]
    
    #print (len(cities) -1)
    for i in range(0, len(cities)):
        #print(i)
        distanceList = []
        
        
           #### index fault ,will currently not take into account subsequent uses of sortedx#######
            #### CANT EDIT CONNECTIONS IF CONNECTIONS ARE ESTABLISHED################
        for j in range(0, len(cities)):
            
            distance = API_Handling.Route(API_KEY,cities[i].name,cities[j].name)
            distanceList.append([distance, cities[j]])
        
        sortedx= sorted(distanceList)                #returns sortedx list of city objects according to of distances from currently researched city
        
        for j in range(0, len(sortedx)):
            p= []  
            for h in range(0, len(sortedx)):
                p.append(sortedx[h][1].name)
             
            #print(str(p) + " ashjdflhsal") # checks current order of cities
            
            openConnection1 = connectionsScanner(sortedx[0][1])                           #checks for open connection 
            openConnection2 = connectionsScanner(cities[j])
            name1= "connection" + str(openConnection1)                                     #name1 becomes connection1, connection2, connection3, etc.
            name2 = "connection" + str(openConnection2)      
            placeholder1 =getattr(sortedx[0][1], "connections")
            placeholder2= getattr(cities[j], "connections")        
            #print(str(placeholder1) + " " +str(sortedx[0][1].name) + "  Connection List:  Object is " + str(cities[j].name))
            
            x =insertion_sort(sortedx)
      
        m =[]
        for s in range(0, 3):
            m.append([x[s+1][0], x[s+1][1].name])
        y.append(m)
        y.append ("\n")
        print(y)
        return y

x = placeClasses.Country('Sweden')
x.cities=[placeClasses.City("Stockholm"), placeClasses.City("Malmö"), placeClasses.City("Gothenburg"),placeClasses.City("Uppsala"), placeClasses.City("Västerås"), placeClasses.City("Örebro"),placeClasses.City("Linköping"), placeClasses.City("Helsingborg"), placeClasses.City("Jönköping") ]
cities = [placeClasses.City("Umeå"), placeClasses.City("Kiruna"), placeClasses.City("Malmo"),placeClasses.City("Stockholm")]


z= countryNet(x)
print(z)
#for i in range(0, 4):
#    print(str(z[i].connections) + " " + str(z[i].name))