from ListaSimple import ListaEnlazada

class Estudiante:
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.cursos = ListaEnlazada()
        self.siguiente = None
        self.anterior = None

    def getCuros_Estudiente(self):
        self.cursos.MostrarCursos()

