import googlemaps
from datetime import datetime

def calculate_distance_duration(api_key, origin, destination):
    gmaps = googlemaps.Client(key=api_key)

    # Make the distance matrix request
    matrix = gmaps.distance_matrix(origin, destination)

    if matrix['status'] == 'OK':
        distance = matrix['rows'][0]['elements'][0]['distance']['text']
        duration = matrix['rows'][0]['elements'][0]['duration']['text']
        return distance, duration
    else:
        return None, None

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    API_KEY = 'AIzaSyC8ObuqZq-i3Ppwu2SbxPez4K567ZTzQNk'

    # Input the origin and destination locations
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")

    distance, duration = calculate_distance_duration(API_KEY, origin, destination)

    if distance and duration:
        print(f"Distance: {distance}")
        print(f"Duration: {duration}")
    else:
        print("Failed to fetch distance and duration. Please check your input and API key.")