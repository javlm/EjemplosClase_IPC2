class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def show(self):
        print('Me llamo ' + self.nombre)

class Gato(Mascota):
    def __init__(self, nombre, edad, color, raza):
        super.__init__(self, nombre, edad)
        self.color =color
        self.raza = raza

    def hablar(self):
        print('Miau')

class Perro(Mascota):
    def hablar(self):
        print('Guau')

m1 = Mascota('Manchas',2)
m2 = Gato('Wilson',8, 'Cafe', 'Angora')
m3 = Perro('Max',14)

m2.show()
