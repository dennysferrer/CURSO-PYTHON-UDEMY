cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1,2,5,8,3,4]

print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos

cantantes.append('Sylvestre Dangond')
cantantes.insert(1,'David Bisbal')
print(cantantes)

# Eliminar elementos

cantantes.pop(1)
print(cantantes)

cantantes.remove('Bad Bunny')
print(cantantes)

# Dar la vuelta a la lista

numeros.reverse()
print(numeros)

#Buscar elementos dentro de la lista

print('Drake' in cantantes)
print(len(cantantes))

#Cuantas veces aparece un elemento en la lista

print(numeros.count(8))
print(cantantes.index('Drake'))

#Unir listas

cantantes.extend(numeros)
print(cantantes)
