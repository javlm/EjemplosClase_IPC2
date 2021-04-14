from flask import Flask, request, jsonify
from flask_cors import CORS

from Gestor import Gestor
from Videojuegos import Videojuego
app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

#Instancia de Gestor
gestor = Gestor()

#Generacion de los endpoints

@app.route('/')
def home():
    return "SERVER IS WORKING!!!!"

#Obtener usuarios
@app.route('/usuarios')
def obtener_usuarios():
    return gestor.obtener_usuarios()    

#Login
@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res ==None:
        return '{"data":false}'
    return '{"data":true}'

#Registro de usuarios
@app.route('/registro',methods=['POST'])
def registrar_usuario():
    dato=request.json
    gestor.crear_usuario(dato['nombre'],dato['password'],dato['usuario'],dato['apellido'])
    return '{"Estado":"Usuario Creado"}'

#Obtener games
@app.route('/obtenervideojuegos')
def obtenergames():
    return gestor.obtener_games()

#Eliminar game
@app.route('/games/<titulo>',methods=["DELETE"])
def eliminar_game(titulo):
    if(gestor.eliminar_game(titulo)):
        return 'Eliminado'
    return 'Error'
#Crear game

@app.route('/games',methods=['POST'])
def insertar_game():
    dato=request.json
    gestor.crear_game(Videojuego(dato['titulo'],dato['plataforma'],dato['precio'],dato['descripcion']))
    return '{"Estado":"Videojuego Creado"}'

#Actualizar game
@app.route('/games/<game>',methods=["PUT"])
def modificar_game(game):
    dato=request.json
    nuevo = Videojuego(dato['titulo'],dato['autor'],dato['imagen'],dato['descripcion'])
    if(gestor.modificar_game(game,nuevo)):
        return '{"Estado":"Vieojuego Actualizado"}'
    return '{"Estado":"No existe el Videojuego"}'

#Iniciar el servidor

if __name__ == "__main__":
    app.run(debug=True)
