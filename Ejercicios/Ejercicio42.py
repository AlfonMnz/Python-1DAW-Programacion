'''Ejercicio 42. Escribir un programa que lea un texto y devuelva un diccionario conteniendo en cada valor todas las palabras de una longitud determinada
Esta longitud será la clave'''


def lista_palabras(texto):
    palabra = ''
    palabras = []
    inicio = 0
    c = 0
    for x in texto:
        c += 1
        if x == ' ' or x == ',':
            palabra = texto[inicio: c - 1]
            inicio = c
            palabras.append(palabra)
        elif c == (len(texto)):
            palabra = (texto[inicio:c + 1])
            inicio = c
            palabras.append(palabra)
    return palabras




def diccionario_palabras():
    diccionario = dict()
    for pal in lista_palabras(texto):
        tamano_palabra = len(pal)
        if tamano_palabra in diccionario:
            diccionario[tamano_palabra].append(pal)
        else:
            diccionario[tamano_palabra] = [pal]
    return diccionario




