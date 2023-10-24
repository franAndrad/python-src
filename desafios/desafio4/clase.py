import math

class Point:
    def __init__(self, cx, cy, desc = 'p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc
    
    def __str__(self):
        linea = '{:<15} - ({:<5},{:<5})'
        linea = linea.format(self.descripcion, self.x, self.y)
        return linea
    
    