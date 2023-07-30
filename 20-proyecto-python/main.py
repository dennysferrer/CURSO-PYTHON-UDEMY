from usuarios import acciones

hazEl = acciones.Acciones()

def run():
    print(""" 
    Acciones disponibles:
    1. registro
    2. login
    """)
    
    accion = input(f'Que deseas hacer: ')

    if (accion == 'registro'):
        hazEl.registro()


    elif (accion == 'login'):
        hazEl.login()



if __name__ == '__main__':
    run()