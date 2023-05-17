secuencia = (1,2,3,4,100,25,23)

# Nescesario
es_el_primero = True
mayor = 0

for num in secuencia:
    if es_el_primero:
        mayor = num
        es_el_primero = False
    elif num > mayor:
        mayor = num
        
print('El mayor es:',mayor)
    