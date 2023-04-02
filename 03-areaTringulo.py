#----------------------------------------------------------------#
#                       Andrade Francisco                        #
# ---------------------------------------------------------------#
#  EJERCICIO: Desarrolle un programa para calcular el área de un #
# triángulo, cargando por teclado el valor de la base, pero      #
# sabiendo que su altura es igual al cuadrado de la base.        #
# (Observar que la altura no es un dato... sólo se indica la     #
# forma de calcularla de acuerdo a la base que sí es un dato).   #                                 
#----------------------------------------------------------------#

print('\nPrograma para calcular el area del triangulo\n')
b = int(input('Ingrese el valor de la altura: '));
h = b**2
area = (b*h)/2
print('\nEl area del triangulo es:', area)