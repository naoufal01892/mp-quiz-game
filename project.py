import csv
import random

csv_file_path = 'Book1.csv'

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    csv_data = list(csv_reader) 
    random_line = random.choice(csv_data)
    first_item = random_line[0]
    print(first_item)
