# definicion de un diccionario

m = {}
m['Enero'] = 1
m['Febrero'] = 2
m['Marzo'] = 3

# deficion de  una lista
ProfArea = list()
ProfArea.append([771, 'IPC 2'])
ProfArea.append([772, 'Estructuras de Datos'])
ProfArea.append([796, 'Lenguajes Formales'])

# definicion de una lista
CommArea = [[112, 'Mate Inter 2'], [114, 'Mate Inter 3'], [152, 'Fisica 2']]

# definicion de un diccionario
Estudiante = {
    'nombre': 'Jose Manuel Lara Elias',
    'carnet': 201344708,
    'cursos': CommArea
}

Estudiante2 = {
    'nombre': 'Javier Estuardo Lima Abrego',
    'carnet': 202100000,
    'cursos': ProfArea,
}




Estudiantes = [Estudiante, Estudiante2]
#                   0           1

Estudiantes[1]['nombre'] = 'Roberto Gonzales'
Estudiantes[1]['carnet'] = 20220000
Estudiantes[1]['cursos'] = CommArea


print(Estudiantes[1])




