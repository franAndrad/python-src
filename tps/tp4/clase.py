class Ticket:
    def __init__(self, id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido):
        self.id = id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.cabina_pais = cabina_pais
        self.km_recorrido = km_recorrido

    def __str__(self):
        linea = "id:{:<15}patente:{:<13}tipo vehiculo:{:<7}forma pago:{:<7}cabina pais:{:<7}km recorrido:{:<7}"
        linea = linea.format(self.id, self.patente, self.tipo_vehiculo,
                             self.forma_pago, self.cabina_pais, self.km_recorrido)
        return linea
