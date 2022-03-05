from multiplicar import multiplicar


def saludo(nombre,numero):
    print(f'Hola mundo y hola {nombre}')
    multiplicar(numero)




if __name__ == '__main__':
    nombre = input('Entre un nombre: ');
    numero = int(input('Digite un número: '))
    saludo(nombre,numero);

    