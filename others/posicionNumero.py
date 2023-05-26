numeros = (11,21,10,35,56,657,123,13432,2345,2342,41)

# Dos cosas
es_el_primero = True
mayor = 0

for num in numeros:  
     
    digit = str(num)
    primer_digit = digit[0]
    if primer_digit == '1':
        if es_el_primero:
            mayor = num
            es_el_primero = False
        elif num > mayor:
            mayor = num

print(mayor)