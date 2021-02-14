from Ejemplo2.Simple.ListaSimple import ListaSimple
class Clase:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.animal = ListaSimple()
        self.siguiente = None
        self.anterior = None
