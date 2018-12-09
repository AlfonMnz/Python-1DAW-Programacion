'''Ejercicio 41. Crear un diccionario que va a contener como clave una tupla de 2 números y como valor va a tener la distancia al origen de ese punto
Escribir una función donde se le pasa un punto y devuelve la distancia.
Vamos a escribir una serie de puntos en el rango entre -100 y 100 50 puntos al azar'''
from math import *
from random import randint


def diccionario(x, y):
    distancia[(x, y)] = modulo(x, y)


def modulo(x1, y1):
    return hypot(x1, y1)


def puntosaleatorios():
    for z in range(50):
        diccionario(randint(-100, 100), randint(-100, 100))


distancia = dict()
