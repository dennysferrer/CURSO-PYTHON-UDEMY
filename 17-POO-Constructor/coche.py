class Coche:

    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
    
    # Metodos o acciones del objeto (funciones)

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setMarca(self,marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje
    
    def getCaballaje(self):
        return self.caballaje

    def acelerar(self):
        self.velocidad += 1
        return self.velocidad

    def frenar(self):
        self.velocidad -= 1
        return self.velocidad

    def getInfo(self):
        print(f'Marca Vehículo: {self.marca}')
        print(f'Modelo Vehículo: {self.modelo}')
        print(f'Color Vehículo: {self.color}')
        print(f'Velocidad Vehículo: {self.velocidad}')
        print(f'Caballaje Vehículo: {self.caballaje}')
    

        

    

    