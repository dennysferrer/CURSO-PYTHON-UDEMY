"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave>valor
"""

Personas = {
    'nombre': 'Victor',
    'apellidos': 'Robles',
    'edad': 35,
    'web': 'www.ferreringenieriasas.com'
}

print(Personas)
print(Personas['web'])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Dennys',
        'apellido': 'Ferrer',
        'edad': 34
    },
    {
        'nombre': 'Javier',
        'apellido': 'Ramirez',
        'edad': 45
    },
    {
        'nombre': 'Victor',
        'apellido': 'Robles',
        'edad': 30
    }
]

print(contactos)
print(contactos[0])
print(contactos[0]['nombre'])
print(contactos[0]['apellido'])
print(contactos[0]['edad'])