import random
import time
n = 3
k = 0
m = n
cont = 0
bases = []

def exponente(a,m,n):
    r = 1
    while m > 0:
        if m & 1 == 1:
            r = (r*a)%n
        a = (a*a) % n
        m >>= 1
    return r

def generar_base():
    a = random.randint(2,n-1)
    if a in bases:
        a = random.randint(2,n-1)
    else:
        bases.append(a)
        return a

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

def main():
    inicio = time.time()
    factorizar(n) 
    probar_base()
    fin = time.time()
    print(fin-inicio)

main()
