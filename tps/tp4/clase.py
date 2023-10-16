import procesos

def origen_patentes_pais(patente):
    """
    Determina el origen del país mediante una cadena de caracteres.

    Parámetros:
        patente (str): Cadena de caracteres para determinar su origen.

    Retorno:
        str: Origen de la patente.
    """
    
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


def importe_acumulado_por_pagos(cabina_pais, tipo_vehiculo, forma_pago):
    """
    Calcula el importe total acumulado considerando cabina, tipo de vehículo y forma de pago.

    Parámetros:
        cabina_pais (int): Índice del país dentro del Mercosur.
        tipo_vehiculo (int): Índice que representa el tipo de vehículo.
        forma_pago (int): Índice que representa la forma de pago.

    Retorno:
        float: Importe total acumulado.
    """
    
    base, subtotal, total = 300, 0, 0
    
    paises_mercosur = 'Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay'
    if paises_mercosur[cabina_pais] == 'Brasil':
        base = 400
    elif paises_mercosur[cabina_pais] == 'Bolivia':
        base = 200
    
    if tipo_vehiculo == 0:
        subtotal = base - (50 * base) / 100
    elif tipo_vehiculo == 1:
        subtotal = base
    elif tipo_vehiculo == 2:
        subtotal = base + (60 * base) / 100
    
    if forma_pago == 1:
        total = subtotal
    elif forma_pago == 2:
        total = subtotal - (10 * subtotal) / 100
    
    return total


class Ticket:
    def __init__(self, codigo, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido):
        self.codigo = codigo
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.cabina_pais = cabina_pais
        self.km_recorrido = km_recorrido

    def __str__(self):
        linea = "| {:^12} | {:^10} ({:^10}) | {:^15} | {:^12} | {:^13} | {:^14} | ${:<10} |".format(
            self.codigo, 
            self.patente, 
            origen_patentes_pais(self.patente), 
            procesos.determinar_vehiculo(self.tipo_vehiculo),
            procesos.determinar_forma_pago(self.forma_pago),
            procesos.determinar_pais(self.cabina_pais),
            self.km_recorrido,
            importe_acumulado_por_pagos(self.cabina_pais, self.tipo_vehiculo, self.forma_pago)
        )
        return linea
