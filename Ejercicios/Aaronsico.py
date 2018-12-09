'''Ejercicio de Aarón'''

from random import *


def generar_aleatorios(inicio, final):

    if final < 10:
        print('Los números tienen que ser mayor de 10')
    else:
        num_a_acertar = randint(inicio, final)

def pruebas(numero):
    generar_aleatorios(inicio,final)
    probador = int(input('Introduce un número comprendido entre el inicio y el final:\n'))
    while probador!=generar_aleatorios():
        probador = int(input('Introduce un número comprendido entre el inicio y el final:\n'))


inicio=int(input('Introduce un número inicial'))
final=int(input('introduce un número final'))