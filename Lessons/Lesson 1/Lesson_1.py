class BrowserWindow:
    def open(self,link):
        self.current_link = link
        print(f'Link {link} was opened')
class Computer:
    def go_online(self):
        return  BrowserWindow()

    def open_itvdn_lesson(self):
        browser_window = self.go_online()
        browser_window.open('itvdn.com')

        return browser_window

my_own_computer = Computer()
browser = my_own_computer.open_itvdn_lesson

# ---------------------------------------------------------------------
class Human:
    def __init__(self, name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


person = Human(
    name='Jonh',
    age='34',
    gender='male'
)
print('----------------------------')
print('name :', person.name)
print('age:', person.age)
print('gender:', person.gender)
print('----------------------------')
# -------------------------------------------------------------------
