#----------------------------------------------------------------#
#                       Andrade Francisco                        #
# ---------------------------------------------------------------#
#  Ejercicio: Plantear un script directamente en el shell de     #
# Python, que permita mostrar, para dos valores a y b, el valor  #
# del cuadrado del binomio.                                      #
#----------------------------------------------------------------#

print('\nPrograma para calcular binomios al cuadrado (a+b)^2 \n')
a = int(input('Ingrese el valor a: '))
b = int(input('Ingrese el valor b: '))
print('\nEl resultado de ('+str(a)+ str("+") +str(b)+')^2: ',(a**2)+(2*a*b)+(b**2))