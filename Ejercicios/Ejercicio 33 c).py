'''Ejercicio 33 c). Le paso un punto y la función me devuelve el módulo'''
from math import sqrt


def modulo(x1, y1):
    x = (x1 ** 2) + (y1 ** 2)
    return sqrt(x)


x1 = int(input('introduce la coordenada x:\n'))
y1 = int(input('introduce la coordenada y:\n'))
print(modulo(x1, y1))
