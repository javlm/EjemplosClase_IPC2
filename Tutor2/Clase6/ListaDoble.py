from Nodo import Estudiante

class Lista:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, nombre, carnet):
        nuevo = Estudiante(nombre, carnet)
        if self.inicio is None:
            self.inicio = nuevo
            return nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            return nuevo
        return None

    def getEstudiante(self, carnet):
        tmp = self.inicio
        while tmp is not None:
            if tmp.carnet == carnet:
                return tmp
            tmp = tmp.siguiente
        return None

    def MostrarEstudiantes(self):
        tmp = self.inicio
        while tmp is not None:
            print('Carnet: ', tmp.carnet, 'Nombre: ', tmp.nombre)
            print('Cursos:')
            tmp.cursos.MostrarCursos()
            print('------------------------------------')
            tmp = tmp.siguiente

