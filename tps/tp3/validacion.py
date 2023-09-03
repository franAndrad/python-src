def id(codigo):
    if codigo > 0 and codigo < 9999999999:
        return True
    return False 

def patente(matricula):
    pass

def tipo_vehiculo(vehiculo):
    if 0 <= vehiculo <= 2:
        return True
    return False 

def forma_pago(pago):
    if 1 <= pago <= 2:
        return True
    return False

def cabina_pais(cabina):
    if 0 <= cabina <= 4:
        return True
    return False

def distancia(km):
    if 0 <= km <= 999:
        return True
    return False