from datetime import datetime
import math
import csv
import requests


API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'

def get_distance(origin, destination, api_key):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        distance = data['rows'][0]['elements'][0]['distance']['text']
        return distance
    else:
        print("Error:", data['status'])
        return None

def get_coordinates(city_name):
    with open('Database/Network_Database/worldcities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city_ascii'] == city_name:
                return float(row['lat']), float(row['lng'])
    return None, None  # Return None if city is not found

def closestWarehouse(city, Country):
    with open('Database/Network_Database/varuhus.csv', 'r', encoding='utf-8') as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        closestWarehouseDistance= 999999999999999
        for row in reader:
            
            if row[1] == Country:
                currentWarehouse =row[0]            
                currentCityDistance = Route2(city, currentWarehouse)
                
                if currentCityDistance < closestWarehouseDistance:
                    closestWarehouseDistance= currentCityDistance
                    closestWarehouse= currentWarehouse 
    return closestWarehouse


def Route2(city1, city2): # distance Calculation using latitude and longitude with haversine formula
    lat1, lon1 =get_coordinates(city1)
    lat2, lon2 =get_coordinates(city2)
    
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Calculate the distance
    distance = R * c
    
    return distance