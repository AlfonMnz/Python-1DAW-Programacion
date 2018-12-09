'''Ejercicio 34. Escribir una función a la que se le de como parámetro una tupla de números enteros y
devuelva la suma de todos los elementos de dicha tupla.
a) Solución original'''


def suma_num(tupla):
    acum = 0
    for num in tupla:
        acum = acum + num
    return acum
