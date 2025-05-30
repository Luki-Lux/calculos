def fibonacci(n):
    num1 = 1
    num2 = 2
    values = [1,2]
    for i in range(1,n):
        num2 = values[-1] + values[-2]
        num1 = values[-1]
        values.append(num2)
    print(values)