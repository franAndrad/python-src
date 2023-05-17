# Cantidad de numeros pares e impares

secuencia = (1,2,3,4,100,25,23)
pares = 0
impares = 0
for num in secuencia:
    # Par
    if num%2 == 0:
        pares += 1
    # Impar
    if num%2 == 1:
        impares += 1
    # Como tambien podriamor poner num%2 != 0 para impares

print('La cantidad de numeros pares son:', pares)
print('La cantidad de numeros impares son:', impares)