# Programación orientada a objetos POO

class Coche:

    # Atributos o variables del objeto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 250
    plazas = 2

    # Metodos o acciones del objeto (funciones)

    def acelerar(self):
        self.velocidad += 1
        return self.velocidad

    def frenar(self):
        self.velocidad -= 1
        return self.velocidad

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color


coche1 = Coche()

coche1.setColor("Verde")

print(coche1.acelerar())
print(coche1.getVelocidad())
print(coche1.getColor())


