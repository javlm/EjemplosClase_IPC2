from xml.dom import minidom

mydoc = minidom.parse('items.xml')
items = mydoc.getElementsByTagName('product')

#print('Valor de Atributos de elementos:')
print(items[0].attributes['name'].value)
for el in items:
    print(el.attributes['name'].value)

print('\nSegundo Valor')
print('forma 1: ' + items[0].childNodes[0].data)
print('fomra 2: ' + items[0].firstChild.data)

print('\nTodo los Valores:')
for el in items:
    print(el.firstChild.data)

print('\nCantidad:')
print(len(items))
