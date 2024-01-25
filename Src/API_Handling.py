import googlemaps
from datetime import datetime

def Route(api_key, origin, destination):      #will return KeyError: Distance if no viable route is found.
    gmaps = googlemaps.Client(key=api_key)

    # Make the distance matrix request
    matrix = gmaps.distance_matrix(origin, destination)

    if matrix['status'] == 'OK':
        distance = matrix['rows'][0]['elements'][0]['distance']['text']
        mes = distance.replace('.', '')                    # FIX TODO remove values after punctuation
        fes= mes.replace(',', '')                          # tar bort komma tecken, fuckar med apin annars
        print(fes)
        res = [int(i) for i in fes.split() if i.isdigit()]      # tar ut individuella siffror
        ny = (str(res))[1:-1]                                   # DET HÄR ÄR DEN VIKTIGA BEHÅLL DEN HÄR, den behåller siffervärdet
        print(ny) 

        return distance
    else:
        return None 

if __name__ == "__main__":
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
