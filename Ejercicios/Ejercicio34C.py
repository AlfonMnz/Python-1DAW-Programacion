'''Ejercicio 34 c) y d). Genera notas al azar 10-20 notas, en tuplas'''
from random import randint
from Ejercicio34B import *


def notas_aleatorias():
    """
    Genera una tupla de notas aleatorias entre 1 y 10
    """
    num_notas = randint(10, 20)
    tupla_notas = ()
    for notas in range(num_notas):
        tupla_notas = tupla_notas + (randint(0, 10),)
    return tupla_notas


def num_alumnos():
    """
    
    """
    result = ()
    for i in range(50):
        result += notas_aleatorias(),
    return result


i = 1
for element in num_alumnos():
    print('las notas del alumno', i, 'son:\n', element, '\nSiendo su resumen: ', resumen(element))
    i += 1
