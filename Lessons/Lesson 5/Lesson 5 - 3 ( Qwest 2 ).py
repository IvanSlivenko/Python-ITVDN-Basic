def values(n,current =1):
    if current<=n:
        print(current)
        values(n=n, current=current+1)

values(int(input('Введіть число від 1 до 10\n')))

