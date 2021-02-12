import xml.etree.ElementTree as ET

tree = ET.parse('zoo.xml')
root = tree.getroot()
print(root)

print('\nTodos los Atributos')
for elemento in root: # mamiferos y reptiles
    for subelemento in elemento: #animal
        print(subelemento.attrib)

for elemento in root:
    print(elemento.tag) #tag
    for subelemento in elemento:
        print('> ' + subelemento.text) #valores -> text

print('\nUnico elmento:')
print(root[1][0].text)

print('cantidad')
print(len(root[0]))
