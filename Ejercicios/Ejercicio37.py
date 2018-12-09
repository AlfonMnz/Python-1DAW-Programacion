'''Ejercicio 37.  Crear utilidades matemáticas:
    a) Escribir una función a la que se le pasa un número y devuelve una tupla con sus divisores
    b) Se define un número primo como aquel que no tiene más divisores queél msimo y la unidad. Escribir una función
que nos devuelva un True en caso de que sea número primo
    c) Crea una función a la que se le pasa un límite y nos devuelve una lista con todos los números primos por debajo
    d) Escribir una función a la que le vamos a pasar como parámetro un número que indicará una potencia de 10. Imprimirá la cantidad
    de primos y el porcentaje de números primos hasta el límite
    e) Creamos una lista de tuplas que nos diga entre segemntos primos(limite,ancho) (limite superior, inf y el num de pr)'''


def divisores(num):
    lista=[]
    for i in range(2, num):
        if num % i == 0:
            lista.append(i)
    return lista


def primos(num):
    res = ()
    es_primo = True
    if num < 2:
        es_primo = False
    for i in range(2, int((num) / 2) + 1):
        if num % i == 0:
            es_primo = False
        if not es_primo:
            return es_primo
    return es_primo


def contador_primos(num):
    res = 0
    for i in range(num):
        if primos(i):
            res += 1
    return res


def limite(num):
    res = []
    for i in range(1, num + 1):
        if primos(i):
            res.append(i)
    return res


def estadistica_primos(num):
    cantidad = contador_primos(10 ** num)
    porcentaje = round(((cantidad * 100) / 10 ** num),2)

    print('la cantidad de primos que hay en el rango de', 10 ** num, 'es', cantidad)
    print('El porcentaje es', porcentaje, '%')


def segmentos(lim, ancho):
    lista=[]
    for i in range(0, lim, ancho):
        tupla = (i, (i + ancho))
        res = contador_primos((i + ancho)) - contador_primos(i)
        tupla += res,
        lista.append(tupla)
    return lista




