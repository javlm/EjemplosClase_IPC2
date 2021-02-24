nombres = []

#agregar elementos al final de la lista
nombres.append('Laura')
nombres.append('Daniel')
nombres.append('Zara')
nombres.append('Ximena')
nombres.append('Hector')

print('Imprimir elementos de nombres:')
for el in nombres:
    print(el)

nombres.sort() #reverse=True -> para ordenar en reversa 9.. 8.. 7.. 0 / z.. x..

print('\nImprimir nombres ordenada:')
for el in nombres:
    print(el)

#nueva lista
nombres2 = ['Pablo', 'Alan','Evelyn']
#concatenando nombres2 a nombres
nombres += nombres2

print('\nNueva Lista: Desordenada nuevamente')
for name in nombres:
    print(name)

#se ordena de nuevo
nombres.sort()

if 'Ximena' in nombres:
    print('\nNombre encontrado en lista')

print('Nombre en la lista',len(nombres))
