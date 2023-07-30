from usuarios import usuario as modelo
from notas import acciones

accionesNotas = acciones.AccionesNotas()

class Acciones:

    def registro(self):
        print("\nOk, vamos a registrar ...")
        nombre = input('Cual es tu nombre?: ')
        apellido = input('Cual es tu apellido?: ')
        email = input('Cual es tu email?: ')
        password = input('Cual es tu password?: ')

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if (registro[0]) >= 1:
            print(f'Felicidades {registro[1].nombre} se ha registrado con el email {registro[1].email}') 
        else:
            print(f'No te has registrado correctamente ...')

    def login(self):
        email = input('\nCual es tu email?: ')
        password = input('Cual es tu password?: ')

        usuario = modelo.Usuario('','',email, password)
        login = usuario.identificar()

        if (login):
            print('\nIdentificación correcta ...', login[1])
            self.proximasAcciones(login)
        else:
            print('\nNo existen datos ...')

    def proximasAcciones(self, usuario):
        print("\n#############################################################")
        print("""
            Acciones Disponibles:
            1. Crear notas (crear)
            2. Mostrar tus notas (mostrar)
            3. Eliminar notas (eliminar)
            4. Salir (salir)
        """)

        accion = input("Qué deseas hacer?: ")

        if (accion == "crear"):
            print(f"\nOk {usuario[1]}, vamos a crear una nota ...")
            accionesNotas.crearNotas(usuario)
            self.proximasAcciones(usuario)
        elif (accion == "mostrar"):
            print(f"\nOk {usuario[1]}, vamos a mostrar tus notas ...")
            accionesNotas.mostrarNotas(usuario)
            self.proximasAcciones(usuario)
        elif (accion == "eliminar"):
            print(f"\nOk {usuario[1]}, vamos a eliminar notas ...")
            accionesNotas.eliminarNotas(usuario)
            self.proximasAcciones(usuario)
        elif (accion == "salir"):
            print(f"\nOk {usuario[1]}, gracias por venir ...")
            exit()
        else:
            print("\nOpción incorrecta ...")
            self.proximasAcciones(usuario)
