def sucesion_collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1

def promedio(s,n):
    return round(s/n,1)

def mayor_lista(lista):
    may = lista[0]
    for n in lista:
        if n > may:
            may = n
    return may

valores = []

num = int(input('Ingrese un numero: '))

# tambien se puede hacer con un valores.append(num)
valores += [num]
sum_numeros = num

while num != 1:
    num = sucesion_collatz(num)
    valores += [num]
    sum_numeros += num

print('Orbita de n =', len(valores),'(valores calculados incluyendo al 13 y al 1):',valores)
print('Longitud de la orbita (cantidad de valores calculados hasta llegar al 1):',len(valores))
print('Promedio de todos los valores de la orbita',promedio(sum_numeros, len(valores)))
print('Mayor de los numeros en esa orbita',mayor_lista(valores))