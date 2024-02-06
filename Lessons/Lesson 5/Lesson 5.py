a = [1, 2, 3, 4, 5]

def iterate(array):
    for elem in array:
        print(elem)

def recur_iter(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        recur_iter(array, index)

iterate(a)
print('-'*25)
recur_iter(a)