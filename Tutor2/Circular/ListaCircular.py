from  Circular.Nodo import Estudiante

class ListaCircular:
    def __init__(self):
        self.primero = None # referencia al primero Nodo 'Estudiante' de la Lista
        self.ultimo = None # referencia al ultimo Nodo 'Estudiante' de la lista

    def insertarNodo(self, carnet, nombre, fecha): #insercion al final de la lista, usando la referencia al ultimo.
        nuevo = Estudiante(carnet, nombre, fecha)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            nuevo.siguiente = nuevo
        else:
            tmp = self.ultimo
            if tmp is not None:
                tmp.siguiente = nuevo
                self.ultimo = nuevo
                nuevo.siguiente = self.primero


    def imprimirEstudiantes(self):
        tmp = self.primero
        while True:
            print(' Codigo: ', tmp.carnet, 'Nombre: ', tmp.nombre)
            tmp = tmp.siguiente
            if tmp == self.primero:
                break

    def getEstudiante(self, carnet):
        tmp = self.primero
        while True:
            if tmp.carnet == carnet:
                return tmp
            tmp = tmp.siguiente
            if tmp == self.primero:
                return None



