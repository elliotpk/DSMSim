from datetime import datetime
import math
import csv

def get_coordinates(city_name):
    with open('Database/Network_Database/worldcities.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city_ascii'] == city_name:
                return float(row['lat']), float(row['lng'])
    return None, None  # Return None if city is not found

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


'''
# Example usage:
lat1 = 59.3294
lon1 = 18.0686
lat2 = 63.8250
lon2 = 20.2639

distance = haversine(lat1, lon1, lat2, lon2)
print("Distance:", distance, "kilometers")


if __name__ == "__main__":              
    'Testar APIn'
    
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'

    # Input the origin and destination locations
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    distance = Route(API_KEY, origin, destination)

    if distance:
        print(f"Distance: {distance}")
    
    else:
        print("Failed to fetch distance and duration. Please check your input and API key.")
'''

x= Route2('Hudiksvall', 'Stockholm')
print(x)