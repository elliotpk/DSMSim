
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

def mix(fromcity, tocity):
        return (fromcity + tocity + 6458)

def distanceCalc(seller, buyer):
    x = str.split(seller , ',')
    y= str.split(buyer, ',')

    a= x[0]
    b= x[1]                     # translates input from  distance matrix api into our function.
    c = y[0]
    d = y[1]
        
        
    seller1= a +"," + b
    buyer1=  c +"," + d
        
    API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'        
        return API_Handling.Route(API_KEY, seller, buyer)
