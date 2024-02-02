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
    def __init__(self, age):
        self.age = age
    def say_hello(self):
        print(f'My age is {self.age}')

class HumanExtended(Human_2_2):
    def __init__(self, name, age):
        super().__init__(age) # ----------Підключаємо аргументи батьківського класу
        self.name = name

    def say_hello(self):
        print(f'My name is {self.name} and  my age is {self.age} ')

human_2_4 = HumanExtended(
    name = 'Viktor',
    age = 40
)
print('---------------------------------------')
human_2_4.say_hello()
print('---------------------------------------')

#------------------------------------------------- Множинне наслідування класів
class Doctor:
    def can_cure(self):
        print('я лікар, я вмію лікувати')

class Architekt:
    def cun_build(self):
        print('я архітектор, я вмію будувати')


class Person(Doctor, Architekt):
    def cun_build_person(self):
        print('я людина, я теж вмію будувати')
s = Person()
print(s.cun_build())
print('------------------------------')
print(s.can_cure())
print('------------------------------')
print(s.cun_build_person())
print('---------------------------------')