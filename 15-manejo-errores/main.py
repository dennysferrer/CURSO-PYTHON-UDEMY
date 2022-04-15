# Capturar excepciones y manejar errores en código
# suceptible a fallos y errores

"""
try:
    nombre = input('Digite un nombre: ')
    if len(nombre)>1:
        nombre_usuario = f"El nombre es: {nombre}"
    print(nombre_usuario)

except:
    print("Ha ocurrido un error!, debes introducir un nombre")
else:
    print("Todo ha funcionado correctamente")


# Manejar multiples excepciones

try:
    numero = int(input("Digite un número para elevarlo al cuadrado: "))
    print(f"El cuadrado de {numero} es: {numero*numero}")
except TypeError:
    print("Debes convertir la cadena a entero")
except ValueError:
    print("Debes introducir un número entero")
"""

# Excepciones personalizadas

try:
    nombre = input("Digite el nombre: ")
    edad = int(input("Digite la edad: "))

    if edad<5 or edad>110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre)<1:
        raise ValueError("El nombre no está completo")
    else:
        print("Bienvenido al Master en Python")
except ValueError:
    print("Introduce los datos correctamente")

