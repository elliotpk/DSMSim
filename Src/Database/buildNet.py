import csv
import API_Handling
import placeClasses
from collections import defaultdict
from math import inf

API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'

def internationalRouting():
    "connects the  two closest cities in neighbouring countries for all cities in database"
    nationalNets = allNationalNetworks()
    with open('Database/Network_Database/closest_cities.csv', 'r', newline='', encoding='utf-8') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip header row
        for row in reader:
            country, neighbor, city1, city2, distance =  row[0], row[1], row[2], row[3], row[4]
            distance = API_Handling.Route2(city1, city2)
            
            x= nationalNets[country]
            if len(x) == 0:
                emptyCountry = defaultdict(list)
                emptyCountry[city1].append([distance, city2]) 
                x.append(emptyCountry)  # Use append to add the dictionary to the list
            else:
                y = x[0]
                y[city1].append([distance, city2])
                x[0] = y
            
    #z = nationalNets['Albania']        # check specific cities for outcomes
    #v=z[0] 
    #print(v['Tirana'])        
    
    return nationalNets              

def allNationalNetworks():
    "returns a  {country: (all intercity-connections within that country)} dictionary"
    
    countriesWithCities = countryBuilder()
    nationalnetworks = defaultdict(list)

    for i in range(1, len(countriesWithCities)): 
        country =countriesWithCities[i].name
        
        cities = countryNet(countriesWithCities[i])             #"Problems"
        
        nationalnetworks[country].append(cities) 
    return nationalnetworks

def cityBuilder(name):
    "Creates a city object"
    x= placeClasses.City(name)
    return x

def countryBuilder(): #TODO """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""THE PROBLEMS ARE HERE """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "builds a country object that contains relevant city objects, given a structured csv file"
    
    countriesWithCities =[]             # return variable            
    countryList = []
    
    
    with open('Database/Network_Database/output.csv', 'r', newline='', encoding='utf-8') as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:                              #create temporary list for interaction from csv file
            countryList.append([row[0],row[1]])         #goes through csv file
            
                
        currentCities = []                              # holds cities in current country
        
        for d in range(0, len(countryList)):          # goes through list of cities in csv file
            
            nowCountry= placeClasses.Country(countryList[d-1][1])     #creates country object
            
            if countryList[d][1] == countryList[d-1][1]:
                currentCities.append(cityBuilder(countryList[d][0]))    # appends city objects to country object
            else:
                nowCountry.cities= currentCities                        # starts new country object
                countriesWithCities.append(nowCountry)                  # bulds on list of country objects
                currentCities = []  
                currentCities.append(cityBuilder(countryList[d][0])) 
                            
    return countriesWithCities 

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
    "takes a single country object and establishes a proximity net which is represented in a dictionary of tuples containing target city and distance"

    cities = countryObj.cities         #our input  
    origins=defaultdict(list)          #our output       

    for i in range(0, len(cities)):
        " This segment prepares a list of distances to currently investigated city"
        
        distanceList = []
        for j in range(0, len(cities)):
            distance = API_Handling.Route2(cities[i].name,cities[j].name)
            distanceList.append([distance, cities[j]]) 
        try:    
            sortedx= sorted(distanceList)
        except:
            sortedx = distanceList   
                     
        for j in range(0, len(sortedx)):
            x =insertion_sort(sortedx)
        
        
        "This segment prepares everything for the output dictionary. it establishes the three closest cities egarded for the network"
        z= []
        zObj= []
        
        for h in range(0, len(x)):                  
            z.append(x[h][1].name) 
            zObj.append([x[h][0], x[h][1]]) 

        
        for d in range(0, 3):
            try:
                origins[str(z[0])].append([zObj[d+1][0], zObj[d+1][1].name])
            except:
                pass
    #print(origins)
    return origins
    
#x = placeClasses.Country('Sweden')
#x.cities=[placeClasses.City("Stockholm"), placeClasses.City("Malmö"), placeClasses.City("Gothenburg"),placeClasses.City("Uppsala"), placeClasses.City("Västerås"), placeClasses.City("Örebro"),placeClasses.City("Linköping"), placeClasses.City("Helsingborg"), placeClasses.City("Jönköping") ]
#cities = [placeClasses.City("Umeå"), placeClasses.City("Kiruna"), placeClasses.City("Malmo"),placeClasses.City("Stockholm")]


#z= countryNet(x)
#print(z)
 
e= internationalRouting()  
print(e)

                

            
            
      