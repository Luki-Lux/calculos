def collatz(n):
    n= int(n)
    values = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
            values.append(n)
        else:
            n = 3*n + 1
            values.append(n)
    print(values)
collatz(200)