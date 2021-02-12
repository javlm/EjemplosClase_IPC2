from lxml import etree #modulo debe ser instalado win+r -> cmd -> pip install lxml
tree = etree.parse('zoo.xml')
animales = tree.xpath('//mamiferos/animal')

print('Todos los valores\n')
for animal in animales:
    print('Etiqueta: ' + animal.tag)
    print('Valor:' + animal.text)
    print(animal.attrib)
    print('\n')
