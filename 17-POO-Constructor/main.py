from coche import Coche

carro = Coche('Verde', 'Renault', 'Sandero', '200', '150')

carro.getInfo()

if type(carro) == Coche:
    print("Es un objeto correcto !!")
else:
    print("No es un objeto !!")

