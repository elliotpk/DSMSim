import random
import csv
import os
    
# gen Specific Location
'''
def find_row( search_term):
    with open('places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if search_term in str(row):
                return row
    return None

print(find_row("London"))
'''

# finds continent  can also potentially save as variable

'''with open('places.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    rows = list(csv_reader)
    y= rows[2300]

print(y)    
x = y

ny = ", ".join(x)
print(ny) 

def list_find(some_list,some_item,find_all=False): 
    
    if (some_item in some_list): 
        if find_all: 
            index_list = [] 
            for an_index in range(len(some_list)): 
               if some_list[an_index] == some_item: 
                   index_list.append(an_index) 
            return index_list 
        else: 
            return some_list.index(some_item) 
    else: 
        return None 
it_is_at = list_find(ny,"Europe") 
if (it_is_at != None): 
  print(" Is in Europe {}".format(it_is_at) ) 
else:
  print("Is in America")'''

'''

def list_find(some_list,some_item,find_all=False): 
    
            if (some_item in some_list): 
                if find_all: 
                    index_list = [] 
                    for an_index in range(len(some_list)): 
                        if some_list[an_index] == some_item: 
                            index_list.append(an_index) 
                    return index_list 
                else: 
                    return some_list.index(some_item) 
            else: 
                return None 
        
def Continent(city):

    with open('places.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        cities = list(reader)
        for rows in cities:
            if (city) in rows:
                print(rows)
                ny = ", ".join(rows)
                print(ny) 

        it_is_at = list_find(ny,"Europe") 
        if (it_is_at != None): 
            return("Europe") 
        else:
            return("America")
        

Continent("New York")
'''

x= random.randint(0,95144)
with open('places.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
        print(rows[x][0] + ', ' +rows[x][1])