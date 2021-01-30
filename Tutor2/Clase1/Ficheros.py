'''archivo = open('Personas.txt')
print(archivo)

with open("FICHERO", mode="MODO") as fichero:
'''
'''
# Leer forma 1
contador = 0
contenido = ''
for line in archivo:
    contador = contador + 1
    contenido += line
print('Lineas contabilizadas: ' + str(contador))
archivo.close()

# leer forma 2
archivo = open('Personas.txt')
contenido = archivo.read()
print(contenido)
archivo.close()
'''
'''
#Escritura forma 1
f = open('mi_fichero.txt', 'w')
try:
    f.write('esto es IPC2')
finally:
    f.close()

#Escritura Forma 2
code = 'Listado de personas'
code += '\n Pedro'
code += '\n Alejandro'
code += '\n Roberto'
with open('prueba.txt', 'w') as fichero:
    fichero.write(code)
'''
'''
#Abrir archivos con try
print('Apertura de Archivo usando Try / Except \n')
nombre_archivo = input()
try:
    file = open(nombre_archivo)
except:
    print('No se pudo abrir el fichero: ' + nombre_archivo)
    exit()
'''
