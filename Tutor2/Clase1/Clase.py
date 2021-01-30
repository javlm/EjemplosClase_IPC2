class Persona:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def presentarse(self):
        print("Me llamo " + self.name)

p1 = Persona('Javier', 21, 'M')
p2 = Persona('Elver', 18, 'M')

p1.presentarse()
p2.presentarse()
