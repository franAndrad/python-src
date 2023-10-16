def validar_cadena(mensaje):
    """
    Valida que una cadena de texto tenga al menos un carácter.

    Parametros:
        mensaje (str): El mensaje que solicita la entrada al usuario.

    Retorno
        str: La cadena de texto validada.
    """
    
    cadena = input(mensaje)
    while len(cadena) == 0:
        print("Debe tener al menos un carácter. Intenta de nuevo")
        cadena = input(mensaje)

    return cadena


def validaciones(mensaje, rango_min, rango_max=None):
    """
    Valida una entrada numérica dentro de un rango especificado.

    Parametros:
        mensaje (str): El mensaje que solicita la entrada al usuario.
        rango_min (int): El valor mínimo permitido.
        rango_max (int, optional): El valor máximo permitido. Si no se proporciona, se valida solo el mínimo.

    Retorno:
        int: El valor numérico validado.
    """
    
    entrada = input(f"{mensaje}: ")
    while not entrada.isdigit() or \
        (rango_max is not None and not (rango_min <= int(entrada) <= rango_max)) or \
            (rango_max is None and int(entrada) < rango_min):
        print('Ingrese un valor válido. Intenta de nuevo.')
        entrada = input(f"{mensaje}: ")

    return int(entrada)
