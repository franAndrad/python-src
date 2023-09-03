def id(codigo):
    if codigo > 0 and codigo < 9999999999:
        return False
    return True 

def patente(matricula):
   if len(matricula) == 7:  # tendrá 7(siete) caracteres
       return False
   return True

def tipo_vehiculo(vehiculo):
    if 0 <= vehiculo <= 2:
        return False
    return True 

def forma_pago(pago):
    if 1 <= pago <= 2:
        return False
    return True

def cabina_pais(cabina):
    if 0 <= cabina <= 4:
        return False
    return True

def distancia(km):
    if 0 <= km <= 999:
        return False
    return True