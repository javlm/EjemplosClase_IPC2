from ListaDoble import Lista

def principal():
    TDA_ListaDoble = Lista()
    ProfArea = [[771, 'IPC 2'], [772, 'Estructuras de Datos'], [796, 'Lenguajes Formales']]
    CommArea = [[112, 'Mate Inter 2'], [114, 'Mate Inter 3'], [152, 'Fisica 2']]
    ProfArea.extend(CommArea)
    opcion = 0
    student = None
    while opcion != 5:
        print('-------- Menu Estudiantes --------')
        print('     1. Agregar Estudiante')
        print('     2. Asignar Curso')
        print('     3. Consultar Estudiante')
        print('     4. Ver Estudiantes')
        opcion = input()
        if opcion == '1':
            print('Agregando un Estudiante al Sistema')
            print('Ingrese carnet:')
            carnet = input()
            print('Ingrese nombre:')
            nombre = input()
            student = TDA_ListaDoble.insertarFinal(carnet, nombre)
            if student is not None:
                print('Estudiante agregado exitosamente')
        elif opcion == '2':
            print('Cursos Disponibles para Asignacion:')
            cont = 1
            for c in ProfArea:
                print(cont, '-', c[1])
                cont += 1
            curso = input() # '1'
            curso = int(curso) # '1' -> 1
            curso -= 1
            student.cursos.asignarCurso(ProfArea[curso][0], ProfArea[curso][1])
        elif opcion == '3':
            print('Ingrese carnet de estudiante a consultar:')
            carne = input()
            student = TDA_ListaDoble.getEstudiante(carne)
            if student is not None:
                print('Info General')
                print('Nomrbre: ', student.nombre)
                print('Cursos:')
                student.getCuros_Estudiente()
            else:
                print('No existe estudiante')
        elif opcion == '4':
            TDA_ListaDoble.MostrarEstudiantes()
        else:
            opcion = 5


principal()