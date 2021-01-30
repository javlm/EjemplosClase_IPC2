#Ejemplo 1
name = input('Enter file:')
handle = open('Info.txt', 'r')
print(type (handle))
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

# Tipos de variables Ejemplo 2
a = 1               #Variable de tipo int
b = 'dos'           #Variable de tipo string
c = 3.14            #Variable de tipo float
d = True            #Variable de tipo booleano
e = False           #Variable de tipo booleano
f = [a,b,c,d,e,]    #Variable de tipo lista
#Imprimir los tipos de variable y su valor
print(type (a), a)
print(type (b), b)
print(type (c), c)
print(type (d), d)
print(type (e), e)
#Imprimir la lista de valores en f y el tipo de
#variable
print([(x, type (x)) for x in f])
#Una varialbe tambien puede cambiar de tipo
#durante la ejecucion
print(type (f))
g = 1
print(type (g))
g = 'nuevo valor'
print(type (g))
print(str(a) + ' ' + g)
if a%2 == 0 :
    print('a es par')
else :
    print('a es impar')

#Ejemplo 3
numeros = [11,12,13,14,15,16,17,18,19]
print([(x, x**3) for x in numeros if x%2])

#Ejemplo 4
import random
import math

for i in range(5):
    print(random.randint(1, 25))

print(math.pi)

