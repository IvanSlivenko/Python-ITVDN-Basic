file_name = '../../Files/my_text'  # --------------- Назва файла та розташування файла
text_file = open(file_name,'r', encoding='utf-8')#---------- Відкриваємо файл
# 'r' - для читання, 'w' - для запису

txt = text_file.read(2)#------------ Читаємо файл
#------------------------в дужках вказуємо кількість символів, що потрібно прочитати

print('txt:', txt)#---------------------------------------Демонструємо прочитане

text_file.seek(0) # Повертаємось на нульову позицію у файлі

txt=text_file.read(2)
print('txt:', txt)
text_file.seek(0)

print("-"*40)
txt_2 = text_file.readline() # ---------------------------Зчитуємо цілий рядок
print('txt_2:', txt_2)

txt_2 = text_file.readline() # ---------------------------Зчитуємо цілий рядок
print('txt_2:', txt_2)
print('-'*45)

text_file.seek(0)
txt_3 = text_file.readlines() #-------------------------- Зчитуємо всі рядки у список
print('txt_3', txt_3)
print('-'*45)

text_file.seek(0)
for row in txt_3:
    for letter in row:
        print(letter)
print('-'*45)
text_file.close() #-------------------------------- Закриваємо файл

# Hello Ivan
# Привіт Іван

text_file = open(file_name,'w', encoding='utf-8')#---------- Відкриваємо файл для запису
text_file.write("Hello")#------------------------------------ Записуємо нове значення  у файл
# text_file.seek(0)
text_file.close()#------------------------------------------ Закриваємо файл

text_file = open(file_name,'r', encoding='utf-8')#---------- Відкриваємо файл
txt_4 = text_file.readline() # -----------------------------------------------Читаємо весь рядок
text_file.close()# -----------------------------------------Закриваємо файл

print('txt_4:', txt_4)
print('-'*45)
text_file = open(file_name,'a', encoding='utf-8')#---------- Відкриваємо файл
text_file.write(" ")#------------------------------------ Додаємо значення  у файл
text_file.write("2024")#------------------------------------ Додаємо значення  у файл
text_file.close()

text_file = open(file_name,'r', encoding='utf-8')#---------- Відкриваємо файл для запису
tex_5 = text_file.readline()
text_file.close()
print('txt_5:', tex_5)
print('-'*45)

with open(file_name,'r') as text_file:
    text = text_file.read()

print('text', text)
print('-'*45)

with open(file_name,'a') as text_file:
    text_file.write(" ")  # ------------------------------------ Додаємо значення  у файл
    text_file.write("-")  # ------------------------------------ Додаємо значення  у файл
    text_file.write(" ")#------------------------------------ Додаємо значення  у файл
    text_file.write("peace in Ukraine")  # ------------------------------------ Додаємо значення  у файл

print('-'*45)

with open(file_name,'r') as text_file:
    text_2 = text_file.read()

print('text_2', text_2)
print('-'*45)













