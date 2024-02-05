class Parser:
    def __init__(self):
        pass
    @staticmethod # ---------------------- декоратор статичного методу
    def __convert_type(value_str): #------------------------------------ визначаємо тип очікуваного числа
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                return float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):#----------------------------------- Перетворюємо строку у число
        packed_values = tuple(expression.split(' '))
        if len(packed_values) < 3:
            print('Wrong indentation, check your expression')
            return 0, 0, '+'
        a, op, b = packed_values
        return self.__convert_type(a), self.__convert_type(b), op
class Core: #---------------------------------------------------- Виконуємо обчислення
    def __init__(self):
        self.parser = Parser()
        self._function= {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }
    def calculate(self, expression):
        a, b, op = self.parser.parse(expression)
        result = self._function.get(op)(a, b)
        return result
class Interfase: #------------------------------------------ Приймаэмо данні та застосовуємо методи
    def __init__(self):
        self.core = Core()

    def run_calculator(self):
        while True:
            print('Enter your expressions')
            expression = input()
            result = self.core.calculate(expression)
            print('Result: {}'.format(result))
            print("=" * 10)

if __name__ == "__main__": #------------------------------ Запускаємо код
    calculator = Interfase()
    calculator.run_calculator()