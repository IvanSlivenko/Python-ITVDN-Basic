# class BrowserWindow:
#     def open(self,link):
#         self.current_link = link
#         print(f'Link {link} was opened')
# class Computer:
#     def go_online(self):
#         return  BrowserWindow()
#
#     def open_itvdn_lesson(self):
#         browser_window = self.go_online()
#         browser_window.open('itvdn.com')
#
#         return browser_window
#
# my_own_computer = Computer()
# browser = my_own_computer.open_itvdn_lesson

#---------------------------------------------------------------------
# class Human:
#     def __init__(self, name,age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def get_name(self):
#         return self.name
#
#     def get_gender(self):
#         return self.gender
#
#     def get_age(self):
#         return self.age
#
#
# person = Human(
#     name='Jonh',
#     age='34',
#     gender='male'
# )
# print('----------------------------')
# print('name :', person.name)
# print('age:', person.age)
# print('gender:', person.gender)
# print('----------------------------')
#-------------------------------------------------------------------
class Human_2:
    def __init__(self, age, name, gender): # -------------------Коструктор класу
        self.age = age
        self.name = name
        self.gender = gender

human_2_1 = Human_2(
    age = 41,
    name = 'Ivan',
    gender = 'Man'
)
print('-----------------------------------------------------------')
print('human_2_1.name:', human_2_1.name)
print('human. age :', human_2_1.age)
print('human_2_1.gender', human_2_1.gender)
print('-----------------------------------------------------------')

class Car:
    def __init__(self, marka, model, yеar):
        self.marka = marka
        self.model = model
        self.yеar = yеar

current_car = Car(
    marka= 'Dachia',
    model = 'Sandero',
    yеar = 2010
)
print('----------------------------------------')
print('current_car.marka', current_car.marka)
print('current_car.marka', current_car.model)
print('current_car.marka', current_car.yеar)
print('----------------------------------------')

#------------------------------------------- Оголошуємо клас
class User:
#------------------------------------------- Описуємо структуру
    def __init__(self, login, password):
        self.login = login
        self.password = password
#------------------------------------------- Створюємо методи
    def get_login(self):
        return self.login

    def get_password(self):
        return self.password
    def get_login_and_pasword(self):
        return self.login, self.password
#------------------------------------------ Використовуємо клас
current_user = User(
    login = 'ivan8822@ukr.net',
    password = '123456789'
)
print(current_user.login)
print(current_user.password)
print('-----------------------------------------')
print(current_user.get_login())
print(current_user.get_password())
print(current_user.get_login_and_pasword())
print('-----------------------------------------')
#-------------------------------------------------
class Human_2_2:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def say_hello(self):
        print('Hello, I im {}'.format(self.name))
        print(f'My age is {self.age}')

class HumanExtended(Human_2_2):
    pass

human_2_3 = Human_2_2(
    name='Ivan',
    age=42
)

human_2_3.say_hello()

human_2_4 = HumanExtended(
    name = 'Viktor',
    age = 40
)

print(human_2_4.name, human_2_4.age)
print('---------------------------------------')