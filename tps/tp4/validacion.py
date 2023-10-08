import os


def validar_tamaño_mayor_0(mensaje):
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            return cadena
        print("Debe tener al menos un carácter. Intenta de nuevo")


def validaciones(mensaje, rango_min, rango_max=None):
    while True:
        entrada = input(f"{mensaje}: ")
        if entrada.isdigit():
            numero = int(entrada)
            if (rango_max is None and numero >= rango_min) or (rango_min <= numero <= rango_max):
                return numero
        print('Ingrese un valor válido. Intenta de nuevo.')
            

def validar_existencia_archivo(fd):
    if not os.path.exists(fd):
        print('El documento', fd, 'no existe!')
        return
