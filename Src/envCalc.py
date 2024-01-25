#ATT TÄNKA PÅ
#6,458 Kilometres is distance between  rotterdam new york
#
import googlemaps
import API_Handling
import csv




seller= "Malmö"
buyer= "Lund"

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

    with open('Database/places.csv', 'r', newline='', encoding='utf-8') as csvfile:
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

def mix(fromcity, tocity):
        return (fromcity + tocity + 6458)
#bbb
def DistanceCalc(seller, buyer):
        
        API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'
        
        if(Continent(seller)==Continent(buyer)): 
                print( "Samma region") 
                print(API_Handling.Route(API_KEY, seller, buyer))
        elif(Continent(seller)=="Europe" and Continent(buyer)== "America"): 
                print("To New York from Rotterdam") 
                x=API_Handling.Route(API_KEY, seller, 'Rotterdam')
                y =API_Handling.Route(API_KEY, 'New York City', buyer)
                print(mix(x,y))
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
