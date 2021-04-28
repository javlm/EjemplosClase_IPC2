from usuario import Usuario
from videojuego import Videojuego
import json

class Gestor:
    def __init__(self):
        self.usuarios =[]
        self.games=[]
        self.games.append(Videojuego("The Witcher 3: Wild Hunt","PS4",450,"El brujo, Geralt of Rivia, inicia la búsqueda de Ciri o Cirilla, la hija del emperador de Niflgaard, que a su vez es perseguida por un ejercito de elfos, la Cacería Salvaje","https://store-images.s-microsoft.com/image/apps.28990.69531514236615003.8f0d03d6-6311-4c21-a151-834503c2901a.d629260e-2bc4-4588-950c-f278cbc22a64"))
        self.games.append(Videojuego("Horizon Zero Dawn: Standard Edition","PS4",210,"El mundo se va al carajo por unas máquinas que se vuelven locas y casi exterminan a la humanidad. Gracias al trabajo de unos cientificos la vida empieza de nuevo.","https://s2.gaming-cdn.com/images/products/6202/orig/horizon-zero-dawn-complete-edition-cover.jpg"))
        self.games.append(Videojuego("Gears of War 4","XBOX One",340,"Por más de 14 años, el mundo de Sera ardía. Después que unas especies desconocidas Locust emergieran del suelo, el mundo estalló en una guerra que sembró al planeta en escombros.","https://store-images.s-microsoft.com/image/apps.11650.13510798887356280.235dc311-b50e-403c-af16-ceffcc2c2399.99b85445-285f-4bc9-a0ec-53e5c36b1ae3"))
        self.games.append(Videojuego("The Last of Us II","PS4",400,"Secuela de The Last of US, luego de unos años, Ellie y Joel se encuentran en el pueblo de Tommy, en una comunidad que ha sobrevivido, pero un evento desatará el caos.","https://image.api.playstation.com/vulcan/img/rnd/202010/2618/Y02ljdBodKFBiziorYgqftLE.png"))
        self.games.append(Videojuego("Overwatch: Legendary Edition","PS4",320," Videojuego de disparos en primera persona multijugador. Explora el mundo, monta un equipo y lucha por objetivos en emocionantes combates 6 contra 6. Elige a tu héroe. ","https://store-images.s-microsoft.com/image/apps.54257.14553281497432575.4e8710df-0a0b-4813-8d05-490c52019361.f7eb126c-0637-4b63-ad90-74a217d9bc28"))
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