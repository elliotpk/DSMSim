import os
from Database import API_Handling

def distanceCalc(seller, buyer):
    
    API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'     
    return API_Handling.Route2(seller, buyer)
