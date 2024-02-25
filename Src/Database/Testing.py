import csv

# Read city data from the first CSV file
city_data = {}
with open('worldcities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city_key = (row['City'], row['Country'])
        city_data[city_key] = (row['lat'], row['lng'])            

# Read European cities from the second CSV file
european_cities = []
with open('varuhus.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        european_cities.append((row['City'], row['Country']))

# Write city data with latitude and longitude to a new CSV file
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['City', 'Country', 'Latitude', 'Longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for city, country in european_cities:
        if (city, country) in city_data:
            latitude, longitude = city_data[(city, country)]
            writer.writerow({'City': city, 'Country': country, 'Latitude': latitude, 'Longitude': longitude})