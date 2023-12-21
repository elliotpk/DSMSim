

import requests

def get_coordinates(token, location_name):
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
    endpoint = f"{base_url}{location_name}.json?access_token={token}"

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        # Extract the coordinates from the response
        if data['features']:
            coordinates = data['features'][0]['geometry']['coordinates']
            return coordinates
        else:
            print("Coordinates not found for the location.")
            return None
    else:
        print("Error:", response.status_code)
        return None

def mapbox_matrix_api(token, coordinates):
    base_url = "https://api.mapbox.com/directions-matrix/v1/mapbox/driving/"
    endpoint = f"{base_url}{';'.join(coordinates)}?access_token={token}"

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

# Replace 'YOUR_MAPBOX_TOKEN' with your actual Mapbox token
mapbox_token = 'sk.eyJ1IjoiYXJ2ZnJvLTQiLCJhIjoiY2xwZ3J2cHU4MDE3OTJpbXhoazZ6bWhkeCJ9.3Qn_PG8X0pdxSd7DsJWjwA'

start_location = input("Enter the starting location: ")
destination_location = input("Enter the destination: ")

start_coordinates = get_coordinates(mapbox_token, start_location)
destination_coordinates = get_coordinates(mapbox_token, destination_location)

if start_coordinates and destination_coordinates:
    result = mapbox_matrix_api(mapbox_token, [f"{start_coordinates[0]},{start_coordinates[1]}", f"{destination_coordinates[0]},{destination_coordinates[1]}"])
    if result:
        distance = result['durations'][0][1]  # Distance between start and destination in seconds
        distance_in_km = distance / 60  # Convert seconds to minutes (assuming distance is in seconds)
        print(f"The distance between {start_location} and {destination_location} is approximately {distance_in_km:.2f} kilometers.")