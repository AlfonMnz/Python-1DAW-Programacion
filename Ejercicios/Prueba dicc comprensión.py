'''Crea un diccionario que tenga cada número con sus divisores. Suponer que existe la función divisores. 100 num
diccionario donde cada letra nos de su valor ascii'''

from Ejercicio37 import *

asc = ()
for x in range(65, 90):
    asc += chr(x),
diccionario = {x: divisores(x) for x in range(100)}
diccionario_ascii = {x: ord(x) for x in asc}
diccionario_cuadrados = {x: x ** 2 for x in range(100)}

import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
