'''Ejercicio 31. En una empresa hay 15 trabajadores . Se quiere hacer un torneo de ajedrez. Escribe una función al que se le pasa una lista
de todos los empleados de la empresa. La función devuelve una lista de todas las partidas posibles entre los empleados
Apartado B) Vamos a sacar esas parejas al azar y generamos un número al azar del tamaño de la lista. Sacamos una pareja la metemos en otra
lista y borramos la pareja de la lista inicial'''

from random import randint


def torneo():
    '''Crea una lista con parejas aleatorias.'''
    x = ['Paco', 'Lucía', 'Antonio', 'Otro Paco', 'El paquillo', 'Nieves', 'Irene', 'la otra lusi', 'El Farlitas',
         'yo que se']
    lista = [jug1 + ' VS ' + jug2 for jug1 in x for jug2 in x if jug1 != jug2]

    return lista


def partidos():
    '''Crea números aleatorios, le mete a la lista 2 una pareja aleatoria de la lista 1'''
    lista = torneo()
    lista2 = []

    while lista != []:
        y = randint(0, len(lista) - 1)
        lista2.append(lista[y])
        del (lista[y])
    return lista2


print(partidos())
