class Ticket:
    def __init__(self, id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido):
        self.id = id
        self.patente = patente.upper()
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.cabina_pais = cabina_pais
        self.km_recorrido = km_recorrido
    
    def __str__(self):
        r = ' '
        r += ' {:<20}'.format('id: '+ str(self.id))
        r += ' {:<20}'.format('patente: ' + str(self.patente))
        r += ' {:<20}'.format('tipo vehiculo: ' + str(self.tipo_vehiculo))
        r += ' {:<20}'.format('forma pago: '+ str(self.forma_pago))
        r += ' {:<20}'.format('cabina pais: '+ str(self.cabina_pais))
        r += ' {:<20}'.format('km recorrido: '+ str(self.km_recorrido))
        return r