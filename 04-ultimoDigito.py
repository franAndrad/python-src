# ----------------------------------------------------------------#
#                       Andrade Francisco                        #
# ---------------------------------------------------------------#
#  EJERCICIO: ¿Cómo usaría el operador resto (%) para obtener el #
# valor del último dígito de un número entero? ¿Y cómo obtendría #
# los dos últimos dígitos? Desarrolle un programa que cargue un  #
# número entero por teclado, y muestre el último dígito del mismo#
# (por un lado) y los dos últimos dígitos (por otro lado) [Ayuda:#
# ¿cuáles son los posibles restos que se obtienen de dividir un  #
# número cualquiera por 10?]                                     #
# ----------------------------------------------------------------#

entero = int(input('\nIngrese el numero a separar su ultimo digito: '))
unidad = entero % 10
decenas = entero % 100
print('Del entero',entero,'se separo', unidad , 'por un lado y', decenas, 'por otro\n')