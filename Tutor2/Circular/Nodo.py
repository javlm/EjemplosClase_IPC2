class Estudiante:
    def __init__(self, carnet, nombre, fecha):
        self.carnet = carnet
        self.nombre = nombre
        self.fecha_nac = fecha
        self.siguiente = None