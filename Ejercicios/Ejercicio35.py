'''Ejercicio 35 apartado a) Que pase de Celsius a Farenheit
apartado b) escribe una función que genere aleatoriamente valores de temperatura entre -5º y 40 º
apartado c) Que genere 1200 temperaturas.
apartado d)cada 100 datos del c es un mes, hacer una media. devuelve una tupla de las medias mensuales
apartado e) hacer que traduzca la tupla de celsius a farenheht
nota: ajustar los valores para que sean creible'''

from random import randint


def conversion_CtoF(temperatura):
    return temperatura * (9 / 5) + 32


def conversion_FtoC(temperatura):
    return (temperatura - 32) * (5 / 9)


def aleatorio():
    return randint(-5, 40)


def temp():
    res = ()
    for temp in range(1200):
        res += aleatorio(),
    return res


def suma(mes):
    acum = 0
    for num in mes:
        for nume in num:
            acum = acum + nume
    return acum


def meses():
    cont = 0
    res = ()
    for mes in temp():
        while cont <= 100:
            res += temp(),
            cont += 1
        result = suma(res)
        return result
