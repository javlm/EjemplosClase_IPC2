from Ejemplo2.Simple.Animal import Animal

class ListaSimple:
    def __init__(self):
        self.inicio = None

        #insercion
    def insertar(self, nombre, familia):
        nuevo = Animal(nombre, familia)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

        #mostrar
    def mostrar(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '. Nombre: ' + str(tmp.nombre)  + ', Familia: ' + str(tmp.familia) + '\n')
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
