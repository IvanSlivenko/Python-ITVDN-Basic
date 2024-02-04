# ------------------------------------------------------------------ Клас №1
class Parallelogram:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def get_multiplication(self):
        area = self.width * self.length
        return area
#------------------------------------------------------------------------------------- Екземпляр класу № 1
figure = Parallelogram(10,12)
print('-----------------------------------------')
print(f'Площа прямокутника з шириною : {figure.width} та довжиною : {figure.length} =', figure.get_multiplication())
print('-----------------------------------------')


#---------------------------------------------------------------------- Клас № 2
class qwest(Parallelogram):
    pass
#-------------------------------------------------------------------------------------- Екземпляр класу № 2
qwest_oun = qwest(2,5)
print(f'{qwest_oun.width} * {qwest_oun.length} = ', qwest_oun.get_multiplication())
print('---------------------------------------')

#----------------------------------------------------------------------- Клас № 3
class request(qwest):
    pass
#------------------------------------------------------------------------------------- Екземпляр класу № 3
test = request(5,5)
print(f'{test.width} * {test.length} = ', test.get_multiplication())
print('---------------------------------------')