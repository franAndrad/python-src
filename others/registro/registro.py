class Empleado:
    pass

def init(leg, nom, direc, suel, ant):
    e = Empleado()
    e.legajo = leg
    e.nombre = nom
    e.direccion = direc
    e.sueldo = suel
    e.antiguedad = ant
    return e

def write(e):
    print("\nLegajo: ", e.legajo)
    print("Nombre: ", e.nombre)
    print("Direccion ", e.direccion)
    print("Sueldo: ", e.sueldo)
    print("Antiguedad: ", e.antiguedad)
