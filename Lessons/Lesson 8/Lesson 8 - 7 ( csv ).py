import csv

with open('../../Files/output.csv','w') as f: #---------- Відкриваємо файл для запису
    # writer = csv.writer(f,quoting=csv.QUOTE_NONE)#------------------- З комою
    # writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # ------------------- З лапками
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # ---------------- Без нічого
    writer.writerow(['h1', 'h2', 'H2'])#-------------------Запис в рядок
    writer.writerow(['222', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])


