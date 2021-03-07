from Circular.ListaCircular import ListaCircular

ListaCricular_Estudiantes = ListaCircular() #en su caso seria de Matrices

ListaCricular_Estudiantes.insertarNodo('201612098', 'Javier Lima', 'Septiembre 22')
ListaCricular_Estudiantes.insertarNodo('201778965', 'Alan Pereira', 'Octubre 9')
ListaCricular_Estudiantes.insertarNodo('201807135', 'Rosalinda Martinez', 'Diciembre 15')
ListaCricular_Estudiantes.insertarNodo('201920786', 'Lucia Gonzales', 'Agosto14')

carnet = '201612098'
print(ListaCricular_Estudiantes.getEstudiante(carnet).nombre, ListaCricular_Estudiantes.getEstudiante(carnet).fecha_nac)
# si el carnet no es correcto tira error de Nonetype porque None no tiene atributo nombre
#asi pueden buscar una matriz por su nombre y acceder a sus atributos

