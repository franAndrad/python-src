class Alumno:
    def __init__(self,dni,nombre,apellido,dni_tutor,importe,nivel_cursado):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.dni_tutor = dni_tutor
        self.importe = importe
        self.nivel_cursado = nivel_cursado

    def __str__(self):
        r = ''
        r += ' DNI Alumno: ' + str(self.dni)
        r += ' Nombre: ' + str(self.nombre)
        r += ' Apellido: ' + str(self.apellido)
        r += ' DNI Tutor: ' + str(self.dni_tutor)
        r += ' Importe ' + str(self.importe)
        r += ' Nivel: ' + str(self.nivel_cursado)
        return r
