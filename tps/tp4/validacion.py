import os


def validar_cadena(mensaje):
    """
    Valida que una cadena de texto tenga al menos un carácter.

    Parametros:
        mensaje (str): El mensaje que solicita la entrada al usuario.

    Retorno
        str: La cadena de texto validada.
    """
    
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            return cadena
        print("Debe tener al menos un carácter. Intenta de nuevo")


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
    
    while True:
        entrada = input(f"{mensaje}: ")
        if entrada.isdigit():
            numero = int(entrada)
            if (rango_max is None and numero >= rango_min) or (rango_min <= numero <= rango_max):
                return numero
        print('Ingrese un valor válido. Intenta de nuevo.')
            

def validar_existencia_archivo(fd):
    """
    Valida si un archivo existe en el sistema.

    Parametros:
        fd (str): Ruta del archivo a verificar.
    """
    
    if not os.path.exists(fd):
        print('El documento', fd, 'no existe!')
        return
