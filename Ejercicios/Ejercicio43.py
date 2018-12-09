'''Ejercicio 43. Queremos construir un diccionario que contenga los divisores de un número.
    La clave del diccionario será el número y el valor de una tupla de los divisores de dicho número.
    Vamos a hcaerlo para los 1000 primeros números.
    b) A partir del diccionario anterior queremos construir un segundo diccionario que tenga el significado inverso. Es decir
    , la vlace será un número y el valor de uuna lista con todos los múltiplos de dicho número.'''

from Ejercicio37 import *


def diccionario_divisores(num):
    dicc = dict()
    for x in range(2, num):
        dicc[x] = divisores(x)
    return dicc


def nuevo_dicc(num):
    res = diccionario_divisores(num)
    return res

def pillar_numeros(diccionario):
    diccionario_final = dict()
    for numero_a_comprobar in diccionario.keys():
        lista_de_su_puta_madre = ()
        for numero_llave in diccionario.keys():
            if numero_a_comprobar in diccionario[numero_llave]:
                lista_de_su_puta_madre += numero_llave,

            diccionario_final[numero_a_comprobar] = lista_de_su_puta_madre
    return diccionario_final





print(pillar_numeros(nuevo_dicc(100)))
