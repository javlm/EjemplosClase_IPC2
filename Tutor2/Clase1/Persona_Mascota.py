class Mascota:
    def __init__(self, n, c):
        self.nombre = n
        self.tipo = c

    def introduce_self(self):
        print("Mi nombre es " + self.name)


class Persona:
    def __init__(self, n, i):
        self.nombre = n
        self.isOwner = i

    def Adoptar(self):
        pass


r1 = Mascota("Tom", "Gato")
r2 = Mascota("Jerry", "Raton")

p1 = Persona("Alice", False)
p2 = Persona("Becky", True)
