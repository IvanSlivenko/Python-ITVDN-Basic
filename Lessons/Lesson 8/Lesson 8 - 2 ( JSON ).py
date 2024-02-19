import json

file_name = '../../Files/my_file.json' #------------------------------ Знаходимо файл

with open(file_name, 'r') as file: #----------------------------- Менеджер контексту для читання
    data = json.load(file)#----------------------------------------- Записуємо у змінну, прочитаний файл
    data.append({"name": "Volodumur", "lastName": "Slivenko"})#----- Додаємо у кінець змінної -- data --
    data.append({"name": "Mariya", "lastName": "Slivenko"})#--
    data.append({"name": "Anna", "lastName": "Slivenko"})# --
print(data)

with open('../../Files/my_file_2.json', 'w') as file: #------------- Менеджер контексту для записування
    data_2 = json.dump(data, file) #-----------Записуємо -- data -- у file


with open('../../Files/my_file_2.json', 'r') as file: #------------- Менеджер контексту для читання
    data_2_1 = json.load(file)# ------------------------------------Записуємо у змінну, прочитаний файл

print('data_2_1', data_2_1)


