'''Ejercicio 34 b). Le vamos a pasar una tupla, nos devuelve el número de elementos que contiene una tupla, la suma de todos los
elementos y la media'''


def suma(tupla):
    acum = 0
    for num in tupla:
        acum = acum + num
    return acum


def todo(tupla):
    return len(tupla)


def media(tupla):
    return suma(tupla) / todo(tupla)


def resumen(tupla):
    print('Pa que te lo goses')
    return todo(tupla), suma(tupla), media(tupla)
