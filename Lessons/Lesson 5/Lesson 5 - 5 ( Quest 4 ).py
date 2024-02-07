def sum_val(num, res=0):
    if not num:
        return res
    print('res', res) #---#
    print('num', num)#---#
    print('num % 10 = ', num % 10)#----#
    res += num % 10 #---------------------- res = res + num % 10 (Остача від ділення на 10 )
    print('current res          =', res)#----#
    num //= 10  # -------------------------- num = num/10
    print('current num =', num)#----#
    print('-' * 20)#---#
    return sum_val(num, res)

s = sum_val(125)
print(s)