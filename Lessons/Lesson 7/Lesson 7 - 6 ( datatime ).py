from datetime import datetime

#---------------------------------------------------------Отримуємо поточну дату та час
now = datetime.now()
print(now)
print('-'*35,'1')

#--------------------------------------------------------- Отримуємо поточний час
print(datetime.time(now))
print('-'*35, '2')

#--------------------------------------------------------- Отримуємо потрібні параметри поточної дати
print(now.year, now.month, now.day)
print('-'*35, '3')
print(now.day, now.month, now.year )
print('-'*35, '4')

#--------------------------------------------------------- Переводимо строку у дату
data_string = "21 June, 2018"
date_object = datetime.strptime(data_string,"%d %B, %Y")
print(date_object)
print('-'*35,'5')

