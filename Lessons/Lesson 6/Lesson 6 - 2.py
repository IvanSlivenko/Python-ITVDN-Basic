#---------------------------------------------------------------------- Example 1
chars = []
for char in 'abcde':
    chars.append(char)
    print(chars)
print('-'* 30)
print(chars)

chars = [char for char in 'abcde']
print('-'*30)
print(chars)

#------------------------------------------------------------------------ Example 2
names = ['make','john', 'sally']
print('-'*30)
print(names)

names = [name.capitalize() for name in names]
print(names)
print('-'*30)
#------------------------------------------------------------------------ Example 3
numbers= [1, 2, 3, 4, 5, 6]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
print('-'*30)
#------------------------------------------------------------------------ Example 4
unique_values = {value ** 2 for value in [1, 3, 5, 5, 2, 2, 1, 7]}
print(unique_values)
print('-'*30)
#------------------------------------------------------------------------ Example 5
unique_values_2 = {value for value in [1, 3, 5, 5, 2, 2, 1, 7]}
print(unique_values_2)
print('-'*30)
#------------------------------------------------------------------------ Example 6
data = ['John_25','Sally_19','Susan_35','Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)
print('-'*30)
#------------------------------------------------------------------------ Example 7
values_squares = {value: value for value in range(10)}
print(values_squares)
print('-'*30)

values_squares = {value: value ** 2 for value in range(1, 10)}
print(values_squares)
print('-'*30)
#------------------------------------------------------------------------ Example 8
m = tuple(n for n in range(1, 12))
print(m)
print('-'*30)

#------------------------------------------------------------------------ Example 9
matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist ]
print(flatten_matrix)

#------------------------------------------------------------------------ Example 10
def func(index, count):
    return {
        "ID": index,
        "values": ["{}_{}".format(index,value) for value in range(count)]
    }
r = func(1,3)
print(r)
print('-' * 60)
#------------------------------------------------------------------------ Example 11
def generate(count):
    return [func(i, j) for i,j in zip(range(count),list(range(count))[::-1])]

r_2 = generate(10)
print(r_2)
print('-'*50)

#------------------------------------------------------------------------ Example 12
f = [value for sublist in r_2 for value in sublist['values']]
print(f)



