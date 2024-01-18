
#ATT TÄNKA PÅ
#6,458 Kilometres is distance between  rotterdam new york
#

import DSMSimGrupp92023.Src.refCalc as refCalc
import googlemaps_test
import csv




seller= "Stockholm"
buyer= "New York"

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

    with open('Database/locations1.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        cities = list(reader)
        for rows in cities:
            if (city) in rows:
                ny = ", ".join(rows)
                print(ny) 

        it_is_at = list_find(ny,"Europe") 
        if (it_is_at != None): 
            return("Europe") 
        else:
            return("America")  

def DistanceCalc(seller, buyer):
        if(Continent(seller)==Continent(buyer)): 
                print( "Samma region") 
        elif(Continent(seller)=="Europe" and Continent(buyer)== "America"): 
                print("To New York from Rotterdam") 
        elif(Continent(buyer)=="Europe" and Continent(seller)== "America"): 
                print("To Rotterdam from New York") 
        else:
                print("FEL")                    # will never execute due to ordering of csv file

DistanceCalc(seller, buyer)

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



