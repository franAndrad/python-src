DEPORTE = 'Natacion', 'Basquet', 'Karate', 'Futbol', 'Patin'    

class Cuota:
    def __init__(self, socio, deporte, dia, valor_cuota):
        self.socio = socio
        self.deporte = deporte
        self.dia = dia
        self.valor_cuota = valor_cuota
        
    def __str__(self):
        r = ''
        r += ' Socio: ' + str(self.socio)
        r += ' Deporte: ' + DEPORTE[self.deporte]
        r += ' Dia: ' + str(self.dia)
        r += ' valor_cuota: ' + str(self.valor_cuota)
        return r
    
    def a_csv(self):
        linea = "{},{},{},{}"
        linea = linea.format(self.socio, self.deporte, self.dia, self.valor_cuota)
        return linea