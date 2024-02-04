def function(data, new_value):
    if isinstance(data,list): #----------- Якщо data є списком, то
        data.append(new_value)
    elif isinstance(data, set): #----------- Якщо data є множиною, то
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data

print(function([1,2,3], 4))
print(function({1,2,3}, 4))
print(function('Ivan  ','Slivenko'))


