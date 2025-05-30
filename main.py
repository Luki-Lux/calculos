import random
import time
n = 3
k = 0
m = n
cont = 0
bases = []

#Prueba de Rabin-Miller

#Función de exponenciación modular
def exponente(a,m,n):
    r = 1
    while m > 0:
        if m & 1 == 1:
            r = (r*a)%n
        a = (a*a) % n
        m >>= 1
    return r

#Función que genera la base aleatoria en la que hacer la prueba
def generar_base():
    a = random.randint(2,n-1)
    if a in bases:
        a = random.randint(2,n-1)
    else:
        bases.append(a)
        return a

#Función que factoriza el número - 1  como 2^n * k donde k es impar
def factorizar(n):
    global m
    global k
    m = n-1
    while True:
        if (m-1)%2 == 0:
            m = m/2
            k += 1
        else:
            break

#Comprueba si es primo o compuesto con la base que tocó
def probar_base():
    global cont
    a = generar_base()
    op = exponente(a,m,n)
    if op == 1 or op == -1:
        print("Primo")
        return True
    else:
        while True:
            if cont < k:
                op = exponente(op,2,n)
                if op == 1:
                    print("Compuesto")
                    return False
                elif op == -1:
                    print("Primo")
                    return True
                else:
                    cont += 1
            else:
                print("Compuesto")
                return False

#Lo ejecuta todo
def primo(n):
    inicio = time.time()
    factorizar(int(n)) 
    probar_base()
    fin = time.time()
    print(fin-inicio)
        
#Calcula n números de la secuencia de Fibonacci, su orden es "fibonacci (n)" ej: fibonacci 10000
def fibonacci(n):
    values = [1,2]
    for i in range(1,n-1):
        num = values[-1] + values[-2]
        values.append(num)
    print(values)

#Calcula los valores que toma un número en la conjetura de Collatz su orden es "collatz (n)" ej: collatz 754
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

#Calcula el factorial de un número su orden es "factorial (n)" ej: factorial 52
def factorial(n):
    termino = n
    resultado = 1
    while termino>1:
        resultado = resultado*termino
        termino = termino-1
    print(resultado)

#La función main, pide una orden y la ejecuta
def main():
    orden = input("Que quieres hacer? Un factorial, números de fibonacci, comprobar si un número es primo o los números por los que pasa un número como valor incial de la conjetura de Collatz? ")  
    orden = orden.split()

    if orden[0] == "primo":
        primo(int(orden[1]))
    elif orden[0] == "fibonacci":
        fibonacci(int(orden[1]))
    elif orden[0] == "collatz":
        collatz(int(orden[1]))
    elif orden[0] == "factorial":
        factorial(int(orden[1]))

#Con esto se puede importar sin ejecutar el código
if __name__ == "__main__":
    main()
