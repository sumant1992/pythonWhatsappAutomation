import csv

lst = []

with open('WthatsApp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(f'"{row[0]}"')


print(lst)