def is_prime(n):  # numeros negativos no admitidos... 
    if n < 0: return None 
    # por definicion, el 1 no es primo... 
    if n == 1: return False
    # si n = 2, es primo y el unico primo par... 
    if n == 2: return True 
    # si n no es 2 pero n es par, no es primo... 
    if n % 2 == 0: return False 
    # si llegamos aca, n es impar... por lo tanto no hace falta 
    # # probar si es divisible por numeros pares... 
    # # ... y alcanza con probar divisores hasta el valor pow(n, 0.5))... 
    raiz = int(pow(n, 0.5)) 
    for div in range(3, raiz + 1, 2): 
        if n % div == 0: 
            return False 
    return True

def next_prime(n):  # si n es menor a 2, el siguiente primo es 2... # ... no nos preocupa si n es negativo... buscamos primos naturales...
    if n < 2: 
        return 2 # Si n es par (puede ser n = 2, pero no nos afecta) entonces el # SIGUIENTE posible primo p no es 2... y es impar...
    # ahora p es impar... comenzar con el propio p # y buscar el siguiente impar que sea primo... 
    
    p = n + 1 
    if p % 2 == 0: 
        p += 1
    
    while not is_prime(p):
        p += 2  # ... y retornarlo 
    
    return p

def factorization(n):  # eliminamos casos no previstos... 
    if n < 0: 
        print('Se esperaba un numero positivo...') 
        return # si n es primo, o es el 1, mostrarlo y terminar... 
    
    if n == 1 or is_prime(n): 
        print(n, end=' ') 
        return # n no es primo... # ...probar a dividirlo por cada primo menor que n//2... 
    
    primo, producto = 2, 1 
    while primo <= n//2: # si primo es divisor de n, mostrarlo... # ... pero tantas veces como la division sea posible... 
        cociente_parcial = n 
        while cociente_parcial > 1 and cociente_parcial % primo == 0: 
            print(primo, end=' ') 
            producto *= primo 
            cociente_parcial //= primo 
            if producto == n: 
                return # ...en todos los casos, tomar el siguiente primo y seguir... 
        primo = next_prime(primo)

factorization(6)