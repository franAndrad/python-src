# ----------------------------------------------------------------------------------------------------------#
#                                            Andrade Francisco                                              #
# ----------------------------------------------------------------------------------------------------------#
#  Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa    #
# la  cantidad de segundos que pasaron desde un evento dado.  El programa debe convertir esa cantidad de    #
# segundos  a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad      #
# de segundos  ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de    #
# 1 hora, 14 minutos  y 12 segundos. Pero la conversión solo debe mostrarse si la cantidad de horas         # 
# totales obtenida es menor o igual a 24. Si esa cantidad de horas totales es mayor a 24, el programa       #
# debe mostrar un mensaje de la forma "Excedido". Se le pedirá comprobar su programa para cuatro            #
# cantidades de segundos, que deberá cargar por teclado.                                                    #
#                                                                                                           #
# Además, el desafío incluye una consigna adicional, en la cual se le pedirá que haga el proceso inverso:   #
# deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos          #
# transcurridos desde un evento dado, y su programa deberá calcular la cantidad total de segundos a         #
# partir de esos datos. Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 #
# entonces el resultado a obtener es que la cantidad total de segundos es 16568.                            #
# ----------------------------------------------------------------------------------------------------------#


# Proceso normal
num = int(input('\nIngrese la cantidad de segundos: '))
h = int(num/3600)

if h<=24:
    m = int((num - (h*3600))/60)
    s = num -((h*3600) + (m*60))
    print('\n' + str(h) + ':' + str(m) + ':' + str(s) + '\n')
else:
    print('Excedido\n')


# Proceso inverso
hs = int(h*3600)
ms = int(m*60)
st = hs + ms + s

print(str(st) + '\n')