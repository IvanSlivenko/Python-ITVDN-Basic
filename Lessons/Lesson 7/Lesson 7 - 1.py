import collections

counts = collections.Counter([1,1,2,3,3,3])
print(counts)
print('-'*50)

dict_of_list = collections.defaultdict(list)

for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if value % 2 == 0:
        dict_of_list['even'].append(value)
    else:
        dict_of_list['odd'].append(value)
print(dict_of_list)
print("-"*20)

d = collections.deque([1, 2, 3]) #
print('d',d)
print('-'*20)
d.popleft() #------------------------------------- Видаляємо зі списку ( зліва )
print('d popleft', d)
print('-'*20)
d.append(4) #------------------------------------- додаємо до списку ( справа )
print('d append',d)
print('-'*20)
d.appendleft(6) #---------------------------------- додаємо до списку ( зліва )
print('d appendleft',d)
print('-'*20)
d.pop() #------------------------------------- Видаляємо зі списку ( справа )
print('d pop',d)
print('-'*20)

