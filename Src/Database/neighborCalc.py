import csv
import API_Handling
from collections import defaultdict
from math import inf

def buildNet():
# Step 1: Handles cities in varuhus
    cities = defaultdict(list)  # Store cities by country
    with open('Network_Database/varuhus.csv', 'r', newline='', encoding='utf-8') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip header row
        for row in reader:
            country, city = row[1], row[0]
            cities[country].append(city)
    
 
# Step 2: handles countries from neighbours
    neighbors = defaultdict(list)  # Store neighboring countries
    with open('Network_Database/neighbours.csv', 'r', newline='', encoding='utf-8') as file2:
        reader = csv.reader(file2)
        next(reader)  # Skip header row
        for row in reader:
            country, *neighboring_countries = row
            neighbors[country] = neighboring_countries 
    
    
# Step 3: Find the closest cities between neighboring countries
    closest_cities = defaultdict(dict)
    for country, neighboring_countries in neighbors.items():
        print(cities[country])
        for neighbor in neighboring_countries:
            for city1 in cities[str(country)]:
                for city2 in cities[str(neighbor)]:
                    distance = getDistance(city1, city2)
                    if distance < closest_cities[country].get(neighbor, (inf, None))[0]:
                        closest_cities[country][neighbor] = (distance, (city1, city2))
                       

# Step 4: Write the results to a new file
    with open('Network_Database/closest_cities.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Country', 'Neighboring Country', 'City 1', 'City 2', 'Distance'])
        for country, neighboring_countries in closest_cities.items():
            for neighbor, (distance, (city1, city2)) in neighboring_countries.items():
                writer.writerow([country, neighbor, city1, city2, distance])
        
                
def getDistance(city1, city2):
    x = 500000     # value larger than the circumference of the earth in case city is not found since sim needs ints
    try:
      x= API_Handling.Route2(city1, city2)
    except:
        pass
    return x

buildNet()