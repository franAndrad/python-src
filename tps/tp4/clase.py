def origen_patentes_pais(patente):
    if len(patente) != 7:
        return 'Otro'

    if patente[0] == ' ':
        if patente[1:5].isalpha() and patente[5:7].isnumeric():
            return 'Chile'
    elif patente[0:2].isalpha() and patente[2:5].isnumeric() and patente[5:7].isalpha():
        return 'Argentina'
    elif patente[0:3].isalpha() and patente[3].isnumeric() and patente[4].isalpha() and patente[5:7].isnumeric():
        return 'Brasil'
    elif patente[0:2].isalpha() and patente[2:7].isnumeric():
        return 'Bolivia'
    elif patente[0:4].isalpha() and patente[4:7].isnumeric():
        return 'Paraguay'
    elif patente[0:3].isalpha() and patente[3:7].isnumeric():
        return 'Uruguay'
    return 'Otro'


class Ticket:
    def __init__(self, id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido):
        self.id = id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.cabina_pais = cabina_pais
        self.km_recorrido = km_recorrido

    def __str__(self):
        linea = "id:{:<15}patente:{:<13}pais:{:<13}tipo vehiculo:{:<7}forma pago:{:<7}cabina pais:{:<7}km recorrido:{:<7}"
        linea = linea.format(self.id, self.patente, origen_patentes_pais(self.patente), self.tipo_vehiculo,
                             self.forma_pago, self.cabina_pais, self.km_recorrido)
        return linea
