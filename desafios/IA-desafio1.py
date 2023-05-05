# Función para convertir segundos a hh:mm:ss
def segundos_a_hhmmss(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# Función para convertir hh:mm:ss a segundos
def hhmmss_a_segundos(hhmmss):
    horas, minutos, segundos = map(int, hhmmss.split(":"))
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Ejemplo de uso
segundos = 3661
hhmmss = "01:01:01"

print(f"{segundos} segundos son {segundos_a_hhmmss(segundos)}")
print(f"{hhmmss} son {hhmmss_a_segundos(hhmmss)} segundos")
