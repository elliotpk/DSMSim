import csv


def Nw_Build():
    # Read city data from all cities in the world
    city_data = {}
    with open('Network_Database/worldcities.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_key = (row['city_ascii'], row['Country'])
            city_data[city_key] = (row['lat'], row['lng'])            

    # Read European cities from desired set of warehouse locations
    european_cities = []
    with open('Network_Database/varuhus.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            european_cities.append((row['City'], row['Country']))

# Write city data with latitude and longitude to a CSV-file for use in buildNet.py
    with open('Network_Database/output.csv', 'w', newline='') as csvfile:
        fieldnames = ['City', 'Country', 'Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for city, country in european_cities:
            if (city, country) in city_data:
                latitude, longitude = city_data[(city, country)]
                writer.writerow({'City': city, 'Country': country, 'Latitude': latitude, 'Longitude': longitude})