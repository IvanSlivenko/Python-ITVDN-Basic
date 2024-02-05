class Parser:
    def __init__(self):
        pass

    def __convert_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                return float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(''))
        if len(packed_values)<3:
            print('Wrong indentation, check your expression')
            return 0, 0, '+'
        a, op, b = packed_values
        return  self.__convert_type(a) ,self.__convert_type(b), op

class Interfase:
    def __init__(self):
        self.core = Core()

    def run_calculator(self):
        print('Enter your expressions')
        exptessions = input()
        # result = self.core.

class Core:
    def __init__(self):
        self.parser = Parser()
        self._function= {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self,expressoin):
        a, b, op = self.parser.parse(expressoin)
        result = self._function.get(op)(a, b)
        return result