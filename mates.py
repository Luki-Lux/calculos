#Comprueba si un numero es primo o pseudoprimo de Fermat en base 2
def fermat(n):
    if pow(2,n-1,n) == 1:
        return True
    else:
        return False

#Usando la funcion anterior, comprueba si la funcion anterior devuelve verdadero para todos los numeros del 3 al n y si lo hace se escribe a primos_fermat.txt, no incluye el número dos
#su orden es "primos(n)" ej: primos(10000000)
def primos(n):
    with open("primos_fermat.txt", "w") as file:
        file.write("2\n")
        for i in range(1,n):
            if fermat(i):
                file.write(str(i))
                file.write("\n")
    print("Finalizado")
        
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
    orden = input("Que quieres hacer? factoriales, números de fibonacci, numeros primos por debajo de cierto número o los números por los que pasa un número de la conjetura de Collatz?")  
    orden = orden.split()

    if orden[0] == "primos":
        print("caxa")
        primos(10000000)
    elif orden[0] == "fibonacci":
        fibonacci(int(orden[1]))
    elif orden[0] == "collatz":
        collatz(int(orden[1]))
    elif orden[0] == "factoriales":
        factorial(int(orden[1]))

#Con esto se puede importar sin ejecutar el código
if __name__ == "_main__":
    main()