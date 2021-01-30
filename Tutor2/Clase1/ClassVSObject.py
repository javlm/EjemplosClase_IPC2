class Persona:
    numero_personas = 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.addPersona()

    def presentarse(self):
        print('hola' + self.name)

    @classmethod
    def getPersonas(cls):
        return cls.numero_personas

    @classmethod
    def addPersona(cls):
        cls.numero_personas += 1

p1 = Persona('Vanesa')
print(p1.getPersonas())
p2 = Persona('Pedro')
print(p1.getPersonas())
p3 = Persona('Laura')
print(p1.getPersonas())
