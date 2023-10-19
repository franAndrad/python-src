class Profesional:
    def __init__(self, dni, nombre, importe, tipo_afiliacion, tipo_trabjo):
        self.dni = dni
        self.nombre = nombre
        self.importe = importe
        self.tipo_afiliacion = tipo_afiliacion
        self.tipo_trabjo = tipo_trabjo
        
    def __str__(self):
        linea = '{:^14} - {:^10} - {:^10} - {:^10} - {:^10}'
        linea = linea.format(self.dni, self.nombre, self.importe, self.tipo_afiliacion, self.tipo_trabjo)
        return linea