class Pelicula:
    def __init__(self, id, titulo, importe_invertido, tipo, pais):
        self.id = id
        self.titulo = titulo
        self.importe_invertido = importe_invertido
        self.tipo = tipo
        self.pais = pais
        
    def __str__(self):
        linea = '{:<5}{:<10}{:<10}{:<5}{:<5}'
        linea = linea.format(self.id, self.titulo, self.importe_invertido, self.tipo, self.pais)
        return linea