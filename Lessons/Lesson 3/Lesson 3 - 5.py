class Parallelogram:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def get_area(self):
        area = self.width * self.length
        return area

figure = Parallelogram(10,12)
print(figure.get_area())