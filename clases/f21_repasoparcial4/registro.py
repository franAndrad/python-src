class Venta:
    def __init__(self,pasaporte,nombre,codigo_destino,codigo_clase,monto):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.codigo_destino = codigo_destino
        self.codigo_clase = codigo_clase
        self.monto = monto

    def __str__(self):
        r = ''
        r += ' Pasaporte:' + str(self.pasaporte)
        r += ' Nombre: ' + str(self.nombre)
        r += ' Codigo destino: ' + str(self.codigo_destino)
        r += ' Monto: ' + str(self.monto)
        r += ' Monto: ' + str(self.monto)
        return r
