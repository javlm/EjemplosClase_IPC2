#Importaciones

from Usuarios import Usuario
from Videojuegos import Videojuego
import json

class Gestor:
    def __init__(self):
        self.usuarios =[]
        self.games=[]
        self.games.append(Videojuego("The Witcher 3: Wild Hunt","PS4",450,"Geralt of Rivia en busqueda de Cirilla"))
        self.games.append(Videojuego("The Sims 4","PC",210,"simulacion social, para rolear :v"))
        self.games.append(Videojuego("Gears of War 4","XBOX One",340,"Una guerra infinita"))
        self.games.append(Videojuego("The Last of Us II","PS4",400,"Se parchan a Joel, y Ellie empieza una matanza xd"))
        
        self.usuarios.append(Usuario('Javier Estuardo','Lima Abrego','admin','admin'))

    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None

    def crear_usuario(self,nombre,password,usuario,apellido):
        self.usuarios.append(Usuario(nombre,apellido,password,usuario))


    def obtener_games(self):
        return json.dumps([ob.__dict__ for ob in self.games])
    

    def eliminar_game(self, titulo):
        for x in self.games:
            if(x.titulo==titulo):
                self.games.remove(x)
                return True
        return False


    def crear_game(self,game):
        self.games.append(game)

    def modificar_game(self,nombre,game):
        for x in self.games:
            if(x.titulo==nombre):
                self.games[self.games.index(x)]=game
                return True
        return False