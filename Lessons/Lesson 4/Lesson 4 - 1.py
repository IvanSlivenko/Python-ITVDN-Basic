class Core:
    def __init__(self):
        self._types = {
        "A": 100,
        "B" :300
        }

    def get_salary(self, clas_name):
        return self._types.get(clas_name, 0)

class AccountingInterfase:
    def __init__(self, data):
        self._core = Core()
        self._people_class_dict = data
    def get_name(self, data, name):
        for i in data.keys():
            if i == name:
                return i
    def get_person_salary(self, name):
        person_class = self._people_class_dict.get(name)
        return self._core.get_salary(person_class)

database = {"John":"A" ,"Sally":"B"}
accounting = AccountingInterfase(data=database)
current_name = input("Ім'я співробітника\n")

print(f'{accounting.get_name(database, current_name)}`s salary', accounting.get_person_salary(current_name))
