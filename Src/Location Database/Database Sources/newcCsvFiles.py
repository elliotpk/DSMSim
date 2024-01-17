import csv
'''
# Open the input CSV file and the output file
with open('cities.csv', 'r') as infile, open('cities2.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    
    # Specify the columns to keep
    fields_to_keep = ['name', 'country_name']  # Remove 'B' and 'D'

    # Create a writer object with the updated columns
    writer = csv.DictWriter(outfile, fieldnames=fields_to_keep)
    writer.writeheader()  # Write the header with updated fields

    # Iterate through rows and write to the new CSV file
    for row in reader:
        # Create a new row with only the fields to keep
        new_row = {field: row[field] for field in fields_to_keep}
        writer.writerow(new_row)
'''
'''
# Open the input CSV file and the output file
with open('countries.csv', 'r') as infile, open('countries2.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    
    # Specify the columns to keep
    fields_to_keep = ['name', 'subregion']  # Remove 'B' and 'D'

    # Create a writer object with the updated columns
    writer = csv.DictWriter(outfile, fieldnames=fields_to_keep)
    writer.writeheader()  # Write the header with updated fields

    # Iterate through rows and write to the new CSV file
    for row in reader:
        # Create a new row with only the fields to keep
        new_row = {field: row[field] for field in fields_to_keep}
        writer.writerow(new_row)
    '''
    
'''
input_filename = 'countries2.csv'
output_filename = 'countries3.csv'
values_to_keep = {'Southern Europe', 'Northern America', 'Northern Europe'}  # Set of values to keep

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row['subregion'] in values_to_keep:
            writer.writerow(row)
'''

'''
file1 = 'cities2.csv'
file2 = 'countries3.csv'

# Read values from file2.csv to create a set of unique values
values_to_keep = set()
with open(file2, 'r') as f2:
    reader2 = csv.DictReader(f2)
    for row in reader2:
        # Assuming the values of interest are in a column 'A'
        values_to_keep.add(row['name'])  # Adjust 'A' to the correct column name

# Filter file1.csv based on values from file2.csv
with open(file1, 'r') as f1, open('cities3.csv', 'w', newline='') as output:
    reader1 = csv.DictReader(f1)
    writer = csv.DictWriter(output, fieldnames=reader1.fieldnames)
    writer.writeheader()

    for row in reader1:
        # Assuming the values of interest are in a column 'A'
        if row['country_name'] in values_to_keep:  # Adjust 'A' to the correct column name
            writer.writerow(row)
'''
'''
file1 = 'cities3.csv'
file2 = 'countries3.csv'

# Dictionary to store values from file2.csv based on the common field
values_dict = {}

# Read file2.csv and store values based on the common field in a dictionary
with open(file2, 'r') as f2:
    reader2 = csv.DictReader(f2)
    for row in reader2:
        # Assuming 'common_field' is the shared field
        values_dict[row['country_name']] = row['subregion']  # Adjust field names accordingly

# Update file1.csv by adding a new field from file2.csv based on the common field
with open(file1, 'r') as f1, open('location_db.csv', 'w', newline='') as output:
    reader1 = csv.DictReader(f1)
    fieldnames = reader1.fieldnames + ['subregion']  # Add the new field to file1.csv
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader1:
        # Assuming 'common_field' is the shared field
        common_value = row['country_name']
        if common_value in values_dict:
            row['subregion'] = values_dict[common_value]
        else:
            row['subregion'] = ''  # If no matching value found, you can assign a default value

        writer.writerow(row)
        
'''
import csv

input_file = 'locations.csv'
output_file = 'locations1.csv'
word_to_remove = 'Northern'  # Word to be removed
field_to_edit = 'subregion'  # Field containing the word to be removed

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Remove the word from the specific field
        row[field_to_edit] = row[field_to_edit].replace(word_to_remove, '')
        writer.writerow(row)