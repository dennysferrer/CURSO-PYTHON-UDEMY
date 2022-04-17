class Persona:

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido
    
    def getApellido(self):
        return self.apellido

    def setAltura(self, altura):
        self.altura = altura
    
    def getAltura(self):
        return self.altura
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, Python"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def getExperiencia(self):
        return self.experiencia

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"


class Tecnico(Informatico):

    def __init__(self):
        super().__init__()
        self.auditor = "Experto"
        self.experienciaRedes = 15

    def mantenimientoRedes(self):
        return "Haciendo mantenimiento de las redes"


