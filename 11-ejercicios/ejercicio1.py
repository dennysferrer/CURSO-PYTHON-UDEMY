def ordenar(numeros):
    numeros.sort()
    print(numeros)

def mostrar(numeros):
    for item in numeros:
        print(item)

def buscar(numeros, numero):
    print(numero in numeros)



if __name__ == '__main__':
    numeros = [34,56,788,2,45,89,996]
    numero = int(input('Digita el número a buscar: '))
    ordenar(numeros)
    mostrar(numeros)
    buscar(numeros,numero)