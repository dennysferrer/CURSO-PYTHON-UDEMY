"""
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 50 y luego muestra la lista
"""

def createList():
    lista = []
    while (len(lista) < 50):
        lista.append(input('Digite un numero: '))

    print(lista)


if __name__ == '__main__':

    createList()