"""Funciones básicas para el planteo del Desafío 03 [AED 2015].

Lista de funciones incluidas:
:is_prime(n): Determina si n es primo o no.
:next_prime(n): Obtiene el primer primo mayor que n.
:vector_unknown_range(n): Genera un arreglo con n números fijos en rango desconocido.
:vector_known_range(n): Genera un arreglo con n números fijos en el intervalo [0, n-1].
"""

__author__ = 'Catedra de AED'


import math


def is_prime(n):
    """Determina si el número n es primo.

    Aplica el algoritmo de divisiones sucesivas para determinar si
    n es primo o no. Retorna True en caso de serlo, o False en caso
    contrario.

    :param n: el número cuya primalidad se desea chequear.
    :return: True si n es primo, False en caso contrario.
    """

    # numeros negativos no admitidos...
    if n < 0:
        return None

    # por definicion, el 1 no es primo...
    if n == 1:
        return False

    # si n = 2, es primo y el único primo par...
    if n == 2 :
        return True

    # si no es n = 2 pero n es par, no es primo...
    if n % 2 == 0 :
        return False

    # si llegamos aca, n es impar... por lo tanto no hace falta
    # probar si es divisible por números pares...
    # ... y alcanza con probar divisores hasta el valor sqrt(n)...
    raiz = int(math.sqrt(n))
    for div in range(3, raiz + 1, 2):
        if n % div == 0:
            return False
    return True


def next_prime(n):
    """Obtiene el primer número primo mayor a n.

    Busca y retorna el primer número primo que sea mayor
    que n. El propio n puede ser primo, y de todos modos
    retornará el siguiente primo mayor que n.

    :param n: el número a partir del cual se busca el siguiente primo.
    :return: El primer primo mayor que n.
    """

    # si n es menor a 2, el siguiente primo es 2...
    # ... no nos preocupa si n es negativo... buscamos primos naturales
    if n < 2:
        return 2

    # Si n es par (puede ser n = 2, pero no nos afecta) entonces el
    # SIGUIENTE primo no es 2... y es impar...
    p = n + 1
    if p % 2 == 0:
        p += 1

    # p es impar... buscar el siguiente primo impar...
    while not is_prime(p):
        p += 2
    else:
        return p


def vector_unknown_range(n):
    """Crea un arreglo con n valores fijos en rango desconocido.

    Calcula n valores fijos (no aleatorios). En principio,
    se desconoce en qué rango de valores están esos números.
    Retorna el arreglo creado.

    :param n: Cantidad de elementos a almacenar en el arreglo.
    :return: el arreglo creado con los n valores fijos.
    """
    if n <= 0:
        return None

    v = []
    for i in range(1, n+1):
        x = int(math.fabs(math.sin(i)) * math.sqrt(n))
        v.append(x)

    return v


def vector_known_range(n):
    """Crea un arreglo con n valores fijos en rango conocido.

    Calcula n valores fijos (no aleatorios). Los números almacenados
    en el arreglo pertenecen todos al intervalo [0, n-1].
    Retorna el arreglo creado.

    :param n: Cantidad de elementos a almacenar en el arreglo.
    :return: el arreglo creado con los n valores fijos.
    """
    if n <= 0:
        return None

    v = []
    p = next_prime(n)
    for i in range(1, n+1):
        x = int(math.fabs(math.sin(i)) * p)
        v.append(x % n)

    return v
