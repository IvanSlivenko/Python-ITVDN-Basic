import csv #---------------------Імпортуємо csv

with open('../../Files/example1.csv','r') as f: #----------------------------Відкриваємо файл
    print('-'*45)
    reader = csv.reader(f)#----------------------------- передаємо у рідер файловий дискриптор
    print('Line  nums', reader.line_num)#---------------- правило парсингу
    print('Dialect', reader.dialect)#------------------   правило парсингу -- dialect --

#------------------------------------------------ Ітеруємо файл у циклі
    for row in reader:
        print(row)
