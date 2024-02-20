import csv

#-------------------------------------------------csv В стрічку
with open('../../Files/data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file ,delimiter=',')
    data = [row for row in csv_reader]

print(data)


print('-'*45)

