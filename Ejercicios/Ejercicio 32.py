'''Generar una lista por comprensión de 1000 numeros aleatorios comprendidos entre 1 y 100'''

from random import randint


def lista_aleatoria():
    '''Mete un número aleatorio en la lista, para x hasta rango 1000'''
    return [randint(1, 100) for x in range(1000)]


print(lista_aleatoria())