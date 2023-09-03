class Empleado:
    # Un constructor dentro de la clase Empleado
    def __init__(self, leg, nom, direc, suel, ant):
        self.legajo = leg
        self.nombre = nom
        self.direccion = direc
        self.sueldo = suel
        self.antiguedad = ant
    
    def __str__(self):
        r = str(self.legajo) + " - "
        return r
