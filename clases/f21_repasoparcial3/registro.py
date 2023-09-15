class Factura:
    def __init__(self, numero,importe,tipo_factura, apellido_persona, tipo_perfume):
        self.numero = numero
        self.importe = importe
        self.tipo_factura = tipo_factura
        self.apellido_persona = apellido_persona
        self.tipo_perfume = tipo_perfume
        
    def __str__(self):
        r = ''
        r += ' Numero: ' + str(self.numero)
        r += ' Importe: ' + str(self.importe)
        r += ' Tipo: ' + str(self.tipo_factura)
        r += ' Apellido: ' + str(self.apellido_persona)
        r += ' Tipo Perfume: ' + str(self.tipo_perfume)
        return r