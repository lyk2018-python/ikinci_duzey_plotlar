import csv


file=open('zomato.txt', 'w')
with open('zomato.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        file.write(str(row))
file.close()
