from Simple.ListaSimple import ListaSimple
from Doble.ListaDoble import ListaDoble
import xml.etree.ElementTree as ET
from lxml import etree

#se parsea el xml para obtener las clases de los animales
tree = ET.parse('zoo.xml')
root = tree.getroot()

#se declaran las listas diferentes de diferentes clases de animales
mamiferos = ListaSimple()
reptiles = ListaSimple()
aves = ListaSimple()
anfibios = ListaSimple()

#se recorre la estructura de elementos XML
for elemento in root: #tag
    if elemento.attrib['clase']== 'reptiles':
        for subelemento in elemento:
            reptiles.insertar(subelemento.text, "")
    elif elemento.attrib['clase']== 'aves':
        for subelemento in elemento:
            aves.insertar(subelemento.text, "")
    elif elemento.attrib['clase']== 'anfibios':
        for subelemento in elemento:
            anfibios.insertar(subelemento.text, "")
    elif elemento.attrib['clase']== 'mamiferos':
        for subelemento in elemento:
            mamiferos.insertar(subelemento.text, subelemento.attrib['familia'])

listaClases = ListaDoble()
#Clases = etree.xpath('//clase')
for clase in root:
    listaClases.insertar(clase.attrib['clase'], clase.attrib['tipo'])

print('Lista de Clases de Animales sin animales asociados')
listaClases.mostrar()
clase_mam = listaClases.getNodo('mamiferos')
clase_mam.animal = mamiferos
print('\nLista de Clases de Animales con mamiferos asociados')
listaClases.mostrar()
