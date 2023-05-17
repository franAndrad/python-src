secuencia = (1,2,3,4,100,25,23)

# Nescesario
es_el_primero = True
menor = 0

for num in secuencia:
    if es_el_primero:
        menor = num
        es_el_primero = False
    elif num < menor:
        menor = num
        
print('El menor es:',menor)