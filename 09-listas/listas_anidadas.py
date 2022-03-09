print('\n************LISTA DE CONTACTOS*************')

name = ''
email = ''
contact_list = []

while (name != 'salir'):
    name = input('Write contact name: ')
    email = input('Write contact email: ')
    contact = list((name, email))
    contact_list.append(contact)

print(contact_list)