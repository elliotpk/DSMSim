
#ATT TÄNKA PÅ
#6,458 Kilometres is distance between  rotterdam new york
#

import ReferenceCalculator
import googlemaps_test
import csv
import locations1.csv
import yaml




Stad1= "Stockholm"
Stad2= "Piteå"
DistanceCalc(Stad1, Stad2)
def DistanceCalc(Stad1, Stad2):
        if(Continent(Stad1)==Continent(Stad2)): 
                return "Samma region" 
        elif(Continent(Stad1)=="Europe" and Continent(Stad2)== "America"): 
                return "To Rotterdam from New York" 
        elif(Continent(Stad2)=="Europe" and Continent(Stad1)== "America"): 
                return "To New York From Rotterdam" 
        else:
                print("FEL")


#KOD

#API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'
#
#origin = (rand(mydatabase))
#destination = mybidder([destination]) eller rand(mydatabase)
#origin[continent] = "US"                               # continent can be either US or EU
#destination[continent] =EU"

#if origin(continent) == destination(continent)
#       #calculate_distance_duration(API_KEY, origin, destination):  

#else if continent(origin) == US
#       #x = calculate_distance_duration(API_KEY, origin, New york):  
        #y = sea route fuel
        #z = #calculate_distance_duration(API_KEY, Rotterdam, destination):
        
# elseif contient(origin) == EU  
#       #x = calculate_distance_duration(API_KEY, origin, Rotterdam):  
        #y = sea route fuel
        #z = #calculate_distance_duration(API_KEY, New york, destination): 
        
# else return "origin or destination not in allowed locations" 
#
#calculate_distance_duration(API_KEY, origin, destination):  
#    


