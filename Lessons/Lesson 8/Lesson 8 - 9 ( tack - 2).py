import random
import datetime
import json

user = ['Anna', 'David', 'Olga']
user_list=[]

for el in user:
    current_data=datetime.datetime.now().strftime('%d,%m,%Y')
    user_list.append({'name': el,'age': random.randint(1,99),'time_registration': current_data})

for string in user_list:
    print(string)

data = {
    'data': user_list,
    'current_data': datetime.datetime.now().strftime('%d,%m,%y')
}


