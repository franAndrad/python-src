#------------------------------------------------------------------
#Programa para calcular el permitro y superficie de un rectangulo
# Nombre: Andrade Francisco
#-------------------------------------------------------------------

print('\nPrograma para calcular perimetro y superficie de un rectangulo\n')

#Ingreso de datos
b = float(input('\nIngrese la base en m: '))
a = float(input('Ingrese la alto en m: '))

#Procesos
per = 2*(b+a)
sup = b*a

#Salida de resultados
print('\nEl perimetro es: ',per)
print('La superficie es:  \n',sup)
