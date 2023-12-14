import csv
color = []
name = []
with open('example.csv') as csvFile:
    readFile = csv.reader(csvFile, delimiter=',')
    for row in readFile:
        print(row)
        colors = row[2]
        names = row[1]
        color.append(colors)
        name.append(names)
print('\n')
print(color)
print(name)
