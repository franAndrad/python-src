class Trabajo:
    def __init__(self,id,descripcion,tipo,importe,cant_personal):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.cant_personal = cant_personal
        
    def __str__(self):
        r = ''
        r += ' id: ' + str(self.id)
        r += ' descripcion: ' + str(self.descripcion)
        r += ' tipo: ' + str(self.tipo)
        r += ' importe: ' + str(self.importe)
        r += ' cantidad personal: ' + str(self.cant_personal)
        return r