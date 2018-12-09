'''Ejercicio 49. Una función que se le pasa un texto y produce un diccionario que tiene como clave letras que aparecen en el texto
y como valor el conjunto de las palabras en las que aparece estas palabras'''

import string
from abecedario import *
from Ejercicio42 import lista_palabras


def claves_diccionario(texto):
    texto = texto.lower()

    diccionario = dict()
    for letras_clave in texto:
        if letras_clave in string.ascii_lowercase:
            diccionario[letras_clave] = ""

    return diccionario


def palabras_in_texto(texto):
    texto = texto.lower()
    diccionario = claves_diccionario(texto)
    lista = lista_palabras(texto)
    for letra_pa_analizar in MINUSCULA:
        for palabras in lista:
            if letra_pa_analizar in palabras:
                if palabras in diccionario[letra_pa_analizar]:
                    pass
                else:
                    diccionario[letra_pa_analizar] += palabras + ' '
    return diccionario


print(palabras_in_texto('Python es la pera limonera jaja salidos'))
