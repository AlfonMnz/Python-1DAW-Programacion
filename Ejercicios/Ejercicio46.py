'''Ejercicio 46. Creamos un diccionario que cuente cuantas veces ocurre cada caracter del texto. La función tiene como entrada una cadena
que contiene un texto y como salida la función devuelve un diccionario que tiene por clave un caracter y por valor, el contador de cada
caracter
Apartado b) Creamos un diccionario que te cuente palabras y devuelve un diccionario con cada palabra del texto como clave.
usar str.split()
Apartado c) Que reconozca un conjunto de separadores
Apartado d) Hacer lo mismo pero con el mismo ejercicio.'''

import string


'''def cuenta_letras(texto):
    diccionario = dict()
    texto = texto.lower()
    c = 0
    for letra_a_comprobar in string.ascii_lowercase:
        for letra_de_texto in texto:
            if letra_de_texto == letra_a_comprobar:
                c += 1
        if c:
            diccionario[letra_a_comprobar] = c
        c = 0

    return diccionario'''


def cuenta_palabras(texto):
    separadores = set('. :;,()[]')
    texto = texto.lower() + " "
    c = 0
    inicio = 0
    diccionario = dict()
    for letra in texto:
        c += 1
        for separador in separadores:
            if letra == separador:
                if texto[inicio:c - 1] not in diccionario.keys():
                    diccionario[texto[inicio:c - 1]] = 1
                else:
                    diccionario[texto[inicio:c - 1]] += 1
                inicio = c

    return diccionario


texto = input('Introduce un texto:\n')
print(cuenta_palabras(texto))
