from NodoAlumno import Estudiante

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, carnet, carrera):
        nuevo = Estudiante(nombre, carnet, carrera)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarNodos(self):
        tmp = self.primero
        while tmp is not None:
            print('Carnet: ' + tmp.carnet + ' Nombre:' + tmp.nombre + ' Carrera:' +tmp.carrera)
            tmp = tmp.siguiente