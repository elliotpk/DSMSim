import csv

'''
# Open the input CSV file and the output file                                               from cities1 to cities2
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
values_to_keep = {'Southern Europe', 'Northern America', 'Northern Europe', 'Western Europe', 'Eastern Europe'}  # Set of values to keep

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
    
'''
file1 = 'cities3.csv'
file2 = 'countries3.csv'
common_column = 'country_name'
output_file = 'locations2.csv'

def combine_csv_files(file1, file2, common_column, output_file):
    # Read data from the first CSV file and create a dictionary
    data_dict = {}
    with open(file1, 'r') as f1:
        reader = csv.DictReader(f1)
        for row in reader:
            key = row[common_column]
            data_dict[key] = row

    # Read data from the second CSV file and update the dictionary
    with open(file2, 'r') as f2:
        reader = csv.DictReader(f2)
        for row in reader:
            key = row[common_column]
            # If the key already exists, update the values, otherwise, add a new entry
            if key in data_dict:
                data_dict[key].update(row)
            else:
                data_dict[key] = row

    # Write the combined data to a new CSV file
    header = reader.fieldnames  # Use the header from the second file
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=header)
        writer.writeheader()
        writer.writerows(data_dict.values())

    print(f'Combined data saved to {output_file}')

'''
        

input_file = 'locations5.csv'
output_file = 'places.csv'
word_to_remove = 'Western'  # Word to be removed
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