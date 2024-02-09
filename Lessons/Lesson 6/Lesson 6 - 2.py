#------------------------------------ Example 1
chars = []
for char in 'abcde':
    chars.append(char)
    print(chars)
print('-'* 30)
print(chars)
#---------------------------------- Example 1 - shorts
chars = [char for char in 'abcde']
print('-'*30)
print(chars)

#------------------------------------ Example 2
names = ['make','john', 'sally']
print('-'*30)
print(names)
#---------------------------------- Example 2 - shorts
names = [name.capitalize() for name in names]
print(names)
print('-'*30)

numbers= [1, 2, 3, 4, 5, 6]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
print('-'*30)

unique_values = {value ** 2 for value in [1, 3, 5, 5, 2, 2, 1, 7]}
print(unique_values)
print('-'*30)

