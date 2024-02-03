
#---------------------------------------------------------------- Поліфорфізм за допомогою Перевизначення
class Multiplier:
    def __init__(self, a):
        self.a = a



    def print_a(self, x):
        print(f' число {self.a} помножене на число {x} = ', self.a * x)

class Exponent(Multiplier):
    def print_a(self, x):
        print(f' число {self.a} в степені {x} = ', self.a ** x)

mult = Multiplier(2)
mult.print_a(3)
print('------------------------------------')
expo = Exponent(2)
expo.print_a(3)

print('------------------------------------')