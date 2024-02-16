import googlemaps
from datetime import datetime

def Route(api_key, origin, destination):      #will return KeyError: Distance if no viable route is found.
    'Tar två städer, ger distans med en int'
    gmaps = googlemaps.Client(key=api_key)

    # Make the distance matrix request
    matrix = gmaps.distance_matrix(origin, destination)

    if matrix['status'] == 'OK':
        distans = matrix['rows'][0]['elements'][0]['distance']['text']
        x1= distans.replace(',', '')                          #tar bort komma tecken när distansen blir stor
        x2 =x1.split('.')[0]                                  #tar bort punkter när distanser blir små

        x3 = [int(i) for i in x2.split() if i.isdigit()]      # tar ut individuella siffror
        output = (str(x3))[1:-1]                              # behåller siffervärdet
        output = int(output)

        return output
    else:
        return None 

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
