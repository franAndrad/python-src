class Reserva:

    def __init__(self, cod, nombre, edad, tipo, inv, monto):
        self.codigo = cod
        self.nombre = nombre
        self.edad = edad
        self.tipo_servicio = tipo
        self.cant_invitados = inv
        self.monto = monto

    def __str__(self):
        return 'Cod: {} - Nombre: {} - Edad: {} - Tipo: {} - Cant. Inv: {} - Monto: $ {}'\
            .format(self.codigo, self.nombre, self.edad, self.tipo_servicio, self.cant_invitados, self.monto)