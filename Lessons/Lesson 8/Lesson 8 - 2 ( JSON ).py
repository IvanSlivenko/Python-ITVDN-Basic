import json

file_name = '../../Files/my_file.json'

with open(file_name, 'r') as file:
    data = json.load(file)

print(data)
