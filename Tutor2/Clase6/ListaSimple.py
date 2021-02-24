from NodoCurso import Curso

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def asignarCurso(self, cod, nombre):
        nuevo = Curso(cod, nombre)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def MostrarCursos(self):
        tmp = self.inicio
        while tmp is not None:
            print(' Codigo: ', tmp.cod, 'Nombre: ', tmp.nombre)
            tmp = tmp.siguiente