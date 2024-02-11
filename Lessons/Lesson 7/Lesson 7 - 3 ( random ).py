import random

print('(random.random()',random.random()) #--------- Випадкове чило в діпазоні від 0 до 1
print('-'*20)
print('random.randint(0,10)',random.randint(0,10))#---------Випадкове чило в діпазоні що ми вказуємо у дужках
print('-'*20)
print('random.choice([1, 2, 3, 4, 5]) = ', random.choice([1, 2, 3, 4, 5]))#---------Випадковий елемент з вкзаного списку
print('-'*20)

random.seed(9)#------------------ Генерує випадкові числа ( починаючи з параметру)
seq = [1, 2, 3, 4, 5, 6]
random.shuffle(seq)#--------------------- Переішує список
print(seq)
print('-'*20)

