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
        
def Continent(city, country):
    with open('Database/places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        cities = list(reader)
        for rows in cities:
            
            if (city  in rows and country in rows):                  #TODO this doesn't trigger.... because of faulty input string? IMPORTANT
                ny = ", ".join(rows)

        it_is_at = list_find(ny,"Europe") 
        if (it_is_at != None): 
            return("Europe") 
        else:
            return("America")  

def mix(fromcity, tocity):
        return (fromcity + tocity + 6458)

def distanceCalc(seller, buyer):
    x = str.split(seller , ',')
    y= str.split(buyer, ',')

    a= x[0]
    b= x[1]
    c = y[0]
    d = y[1]
        
        
    seller1= a +"," + b
    buyer1=  c +"," + d
        
    API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'
        
    if(Continent(a,b)== Continent(c, d)): 
        #print( "Samma region")           
        print(str(API_Handling.Route(API_KEY, seller, buyer))+' km')         
        return API_Handling.Route(API_KEY, seller, buyer)
    elif(Continent(a,b)== "Europe" and Continent(c,d)== "America"): 
        print("To New York from Rotterdam") 
        x=API_Handling.Route(API_KEY, seller1, 'Rotterdam')
        y =API_Handling.Route(API_KEY, 'New York City', buyer1)
        print(str(mix(x,y))+' km')
        return mix(x,y)
    elif(Continent(a,b)== "America" and Continent(c,d)== "Europe"):
        x=API_Handling.Route(API_KEY, seller1, 'New York City')
        y =API_Handling.Route(API_KEY, 'Rotterdam', buyer1)
        print(str(mix(x,y))+' km')
        print("To Rotterdam from New York")
        return mix(x,y)
    
    
    
 
seller = "Los Angeles,United States"
buyer = "Vladivostok,Russia"  

#Continent(seller)
    

# 22500 km = 1 score Distance Vladivostok - Los Angeles (Avrundat)
# 225 km = 100 score Distance Vladivostok / 100 (Avrundat)
    
# Bränsleberäkning för sjörutt
