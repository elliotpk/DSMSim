import googlemaps
from datetime import datetime

def Route(api_key, origin, destination):      #will return KeyError: Distance if no viable route is found.
    gmaps = googlemaps.Client(key=api_key)

    # Make the distance matrix request
    matrix = gmaps.distance_matrix(origin, destination)

    if matrix['status'] == 'OK':
        distans = matrix['rows'][0]['elements'][0]['distance']['text']
        print(distans)
        fes= distans.replace(',', '')                          # tar bort komma tecken, fuckar med apin annars
        ges =fes.split('.')[0]                                  #tar bort decimalvärden helt, dvs avrundar till golvet.
        #print(ges)

        res = [int(i) for i in ges.split() if i.isdigit()]      # tar ut individuella siffror
        ny = (str(res))[1:-1]                                   # DET HÄR ÄR DEN VIKTIGA BEHÅLL DEN HÄR, den behåller siffervärdet
        print(ny) 

        return ny
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
