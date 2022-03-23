"""
Hacer un programa que verifique si una variable está vacía, rellenarla con texto en minuscula y mostrar el texto en mayuscula
"""

def programa(texto):
    if(len(texto)):
        print('La variable está vacía')
    else:
        print('La variable no está vacía')


if __name__ == '__main__':
    cadena = ''
    programa(cadena)