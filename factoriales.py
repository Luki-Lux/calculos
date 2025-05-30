def factorial(n):
    termino = n
    resultado = 1
    while termino>1:
        resultado = resultado*termino
        termino = termino-1
    print(resultado)

def main():
    i = 0
    while True:
        print(i)
        factorial(i)
        i+=1

if __name__ == "__main__":
    main()