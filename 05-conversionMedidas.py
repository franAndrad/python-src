# ---------------------------------------------------------------#
#                       Andrade Francisco                        #
# ---------------------------------------------------------------#
#  EJERCICIO: Desarrolle un programa para convertir una medida   #
# dada en pies a sus equivalentes en:                            #
#     yardas                                                     #
#     pulgadas                                                   #
#     centímetros                                                #
#     metros                                                     #
#                                                                #                                   
# Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,           #
# 1 pulgada = 2.54 centímetros,                                  #
# 1 metro = 100 centímetros                                      #
# ---------------------------------------------------------------#

pies = float(input('\nIngrese medida en pies:'))
yarda = pies/3
pulgada = pies * 12
centimetro = 2.54*pulgada
metro = centimetro/100
print('\npies:',pies,'\nyarda:', yarda,'\npulgada:', pulgada,'\nmetro:',metro,'\ncentimetro:\n',centimetro)
