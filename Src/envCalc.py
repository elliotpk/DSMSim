
import googlemaps
import API_Handling

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
    return API_Handling.Route2(seller, buyer)
