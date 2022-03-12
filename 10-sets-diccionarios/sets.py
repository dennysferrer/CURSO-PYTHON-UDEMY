"""
Set es un tipo de dato, para definir una coleccion de valores, pero no tiene ni indice ni orden
"""

personas = {
    'Francisco',
    "Manolo",
    'Victor'
}

print(personas)
print(type(personas))

personas.add('Paco')
print(personas)