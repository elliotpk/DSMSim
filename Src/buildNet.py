
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


def buildNet():
# Step 1: Parse data from file1
    cities = defaultdict(list)  # Store cities by country
    with open('Database/varuhus.csv', 'r', newline='', encoding='utf-8') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip header row
        for row in reader:
            country, city = row[1], row[0]
            cities[country].append(city)    
   
# Step 2: Parse data from file2
    
    neighbors = defaultdict(list)  # Store neighboring countries
    with open('Database/neighbours.csv', 'r', newline='', encoding='utf-8') as file2:
        reader = csv.reader(file2)
        next(reader)  # Skip header row
        for row in reader:
            country, *neighboring_countries = row
            neighbors[country] = neighboring_countries

# Step 3: Find the closest cities between neighboring countries
    closest_cities = defaultdict(dict)
    for country, neighboring_countries in neighbors.items():
    
        print("started " + str(country) + " first city is " +  str(cities[" " + str(country)][0]))
        for neighbor in neighboring_countries:
            for city1 in cities[" " + str(country)]:
                for city2 in cities[" " + str(neighbor)]:
                # Assuming you have a function to calculate the distance between two cities
                    distance = getDistance(city1, city2)
                    if distance < closest_cities[country].get(neighbor, (inf, None))[0]:
                        closest_cities[country][neighbor] = (distance, (city1, city2))
                       

# Step 4: Write the results to a new file
    with open('Database/closest_cities.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Country', 'Neighboring Country', 'City 1', 'City 2', 'Distance'])
        for country, neighboring_countries in closest_cities.items():
            for neighbor, (distance, (city1, city2)) in neighboring_countries.items():
                writer.writerow([country, neighbor, city1, city2, distance])

def getDistance(city1, city2):
    # Dummy distance calculation function based on the index of the cities in the list
    x = 300000
    try:
      x= API_Handling.Route(API_KEY, city1, city2)
    except:
        pass
    return x



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
            
            x =insertion_sort(sortedx)
 
        m =[]
        for s in range(0, 3):
            m.append((x[s+1][0], x[s+1][1].name))
        y.append(m)
        print(y)
    return y
    
    

x = placeClasses.Country('Sweden')
x.cities=[placeClasses.City("Stockholm"), placeClasses.City("Malmö"), placeClasses.City("Gothenburg"),placeClasses.City("Uppsala"), placeClasses.City("Västerås"), placeClasses.City("Örebro"),placeClasses.City("Linköping"), placeClasses.City("Helsingborg"), placeClasses.City("Jönköping") ]
cities = [placeClasses.City("Umeå"), placeClasses.City("Kiruna"), placeClasses.City("Malmo"),placeClasses.City("Stockholm")]



buildNet()
#z= countryNet(x)
#print(z)
#for i in range(0, 4):
#    print(str(z[i].connections) + " " + str(z[i].name))

    

                

            
            
      