class Parser: # ------------------------------- Механізми перетворення стічок у число
    def __init__(self):
        pass
    @staticmethod#--------------------------------------- Декоратор статичних методів
    def __converter_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result
    def parse(self, expression):
        packed_values = tuple(expression.split(' '))
        if len(packed_values) < 3:
            print('Wrong indentation, check your expression')
            return 0, 0, '+'
        a, op, b = packed_values
        return self.__converter_type(a), self.__converter_type(b), op

class Core: #---------------------------------- Механізми обчислення
    def __init__(self):
        self.parser = Parser()
        self._function ={
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }
    def calculate(self,expression ):
        a, b, op = self.parser.parse(expression)
        result = self._function.get(op)(a, b)
        return result

class Interfase: #------------------------------ Застосування механізмів
    def __init__(self):
        self.core = Core()
    def run_calculator(self):
        while True:
            print("Enter your expression \n")
            expression = input()
            result = self.core.calculate(expression)
            print('Result : {}'.format(result))
            print("-" * 10)

if __name__ == "__main__": # ------------------- Запуск кода
    calculator = Interfase()#---------------------------------------Створюємо екземпляр класу "Interfase"
    calculator.run_calculator()



