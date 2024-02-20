import csv
#-----------------------------------------------csv В стовбці
with open('../../Files/data.csv','r') as csv_file:
    print('-' * 45)
    csv_reader_2 = csv.reader(csv_file)
    for el in csv_reader_2:
        print(el)


print('-'*45)
