from Ejemplo2.Doble.Clase import Clase
class ListaDoble:
    def __init__(self):
        self.inicio = None

        #insercion
    def insertar(self, nombre, tipo):
        nuevo = Clase(nombre, tipo)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

        #mostrar
    def mostrar(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '. Nombre: ' + str(tmp.nombre)  + ', Tipo: ' + str(tmp.tipo))
            print('Animales registrados: ' + str(tmp.animal.getSize()))
            contador += 1
            tmp = tmp.siguiente

            #tamanio
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

        #busqueda y retorno
    def getNodo(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None
