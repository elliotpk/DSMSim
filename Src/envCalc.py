#ATT TÄNKA PÅ
#6,458 Kilometres is distance between  rotterdam new york
#
import googlemaps
import API_Handling
import csv





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
    ny = []
    print(city + " YEAH")
    with open('Database/places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        cities = list(reader)
        #print(cities)
        for rows in cities:
            
            if (city) in rows:                  #TODO this doesn't trigger.... because of faulty input string? IMPORTANT
                print("YAW")
                ny = ", ".join(rows)
                print(ny)

        it_is_at = list_find(ny,"Europe") 
        if (it_is_at != None): 
            return("Europe") 
        else:
            return("America")  

def mix(fromcity, tocity):
        return (fromcity + tocity + 6458)

def distanceCalc(seller, buyer):
        
        API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'
        
        if(Continent(seller)== Continent(buyer)): 
                print( "Samma region") 
                
                print(str(seller + " " + buyer + " TEST" ))             #TODO somehow two countries with separate continents slip in here 
                
                print(str(API_Handling.Route(API_KEY, seller, buyer))+' km')
                return API_Handling.Route(API_KEY, seller, buyer)
        elif(Continent(seller)=="Europe" and Continent(buyer)== "America"): 
                print("To New York from Rotterdam") 
                x=API_Handling.Route(API_KEY, seller, 'Rotterdam')
                y =API_Handling.Route(API_KEY, 'New York City', buyer)
                print(str(mix(x,y))+' km')
                return mix(x,y)
        elif(Continent(buyer)=="Europe" and Continent(seller)== "America"): 
                x=API_Handling.Route(API_KEY, seller, 'New York City')
                y =API_Handling.Route(API_KEY, 'Rotterdam', buyer)
                print(str(mix(x,y))+' km')
                print("To Rotterdam from New York")
                return mix(x,y)
                   
seller= "'Madrid', 'Spain'"
buyer= "'Boston', 'United States'"       

#Continent(seller)
distanceCalc(seller, buyer)

# Bränsleberäkning för sjörutt
