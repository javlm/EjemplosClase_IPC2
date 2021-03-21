# ------------------------- Clases para crear las listas doblemente enlazadas de las cabeceras/cabezas para filas y para columnas
class Nodo():
	def __init__(self, id, valor):
		self.id = id
		self.valor = valor
		self.anterior = None
		self.siguiente = None

class ListaDoble():
	def __init__(self):
		self.cabeza = None

	def insertarCabecera(self, coordenada):
		pass

#-----------------------------Codigo para empezar la Lista Ortogonal -----> MATRIZ <----------------
class Nodocelda():
	def __init__(self, x, y, caracter):
		self.caracter = caracter # * o -
		self.coordenadaX = x
		self.coordenadaY = y
		self.nombre = ''
		self.arriba = None 
		self.abajo = None 
		self.derecha = None #self.siguiente / self.next
		self.izquierda = None #self.anterior 


class MatrizDispersa(): # EstructuraMatriz
	def __init__(self):
		self.cabecera = Nodocelda() # Nodo donde almacenan el nombre
		self.columnas = ListaDoble() # y --> y1, y2, y3, y4, y5 ....
		self.filas = ListaDoble() # x ---> x1, x2, x3, x4, x5.... 
		self.cabecera.derecha = self.columnas
		self.cabecera.abajo = self.filas

	def insertarNodo(self, x, y, caracter):
		nuevoNodoCelda = Nodocelda(x,y,caracter)

#<filas> 5
#<columnas>8
#<imagen> --------
#		  ********
#		  *------*
#         ********
#		  --------
#		matriz_n1  	->  self.columnas:ListaDoble() nodo1 nodo2 nodo3 nodo4 nodo5 nodo6 nodo7 nodo8
#   		! 									     !     !     !     !     !     !     !     !
#	self.filas:ListaDoble()
#		nodo1 ->                                     -     -     -     -     -     -     -     -
#		nodo2 ->                                     *     *     *     *     *     *     *     *
#		nodo3 ->
#		nodo4 ->
#		nodo5 ->


class main():
	##################### Lectura XML#########################
	##########################################################

	xml = getRoot()

	principal = ListaSimple()
	NodoMatriz = None
	for elemento in xml:
		NodoMatriz = principal.insertar(xml.nombre) #return NodoMatriz(matriz_n1)

	filas = xml.filas #5
	columnas = xml.columnas
	nombrematriz = xml.nombre

   	cont = 1 
   	while cont <= filas:
		NodoMatriz.EstructuraMatriz.filas.insertarCabecera(cont)
		cont += 1

	cont = 1 
   	while cont <= columnas:
		NodoMatriz.EstructuraMatriz.columnas.insertarCabecera(cont)
		cont += 1

	NodoMatriz.EstructuraMatriz.cabecera.nombre = xml.nombre # NodoMatriz.nombre
	
	imagen = xml.imagen #-------*******
	NodoMatriz.EstructuraMatriz.insertarNodoCelda() #---implementacion de ustedes