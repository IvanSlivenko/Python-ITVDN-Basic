def check_pow_2(n):
    if n == 1:
        print('YES')
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print("NO")

check_pow_2(16)