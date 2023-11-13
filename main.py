import csv
import random
import re
from xml.dom import minidom

xmldoc = minidom.parse('currency.xml')
Tags1 = xmldoc.getElementsByTagName('CharCode')
Tags2 = xmldoc.getElementsByTagName('Nominal')
def year(date):
    delimiters = " |\\."
    result = re.split(delimiters, date)
    return(result[2])


with open('books.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
Years = ['2015', '2018']
counter = 0
counter_i = 0
counter_j = 0

database = [[]]
string = ''
print(len(data))
for i in data:
    if len(i) != 1:
        while counter_j < len(i):
            string += i[counter_j]
            counter_j += 1
        i[0] = string
    string = i[0].split(';')
    if len(string[1]) > 30:
        counter += 1
    database[counter_i].extend(string)
    counter_i += 1
    counter_j = 0
    database.append([])
    string = ''
database.pop(len(database) - 1)
csvfile.close()
Author = input('')

for i in database:
    if Author in i[4] and (year(i[6]) in Years):
        print(i)

new_file = open('Books.txt', 'w+')
ID_base = []
for i in range(20):
    x = random.randint(0, len(database) - 1)
    while database[x][0] in ID_base:
        x = random.randint(0, len(database) - 1)
    else:
        ID_base.append(database[x][0])
    new_file.write(f'{str(i + 1)} | {database[x][3]} | {database[x][1]} | {year(database[x][6])}\n')

new_file.close()
print(counter)
del counter_j, counter_i, database, ID_base, Author, string, data, i, Years, x
counter = 0
print('\nAll attributes:')
for elem in Tags1:
    print('CharCode: ', Tags1[counter].firstChild.data, 'Nominal: ', Tags2[counter].firstChild.data)
    counter += 1
