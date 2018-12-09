'''Ejercicio 47. Queremos escribir un programa al que le vamos dando palabras de forma interactiva. Este programa guardará dichas palabras
y calculará y almacenará todas las palabras posibles que se puedan formar con las combinaciones posibles de todas las letras de cada palabara
introducida.'''

'''def almacenador(texto):
    tupla_letras=()
    contador = len(tupla_letras)
    contador_key = 1
    diccionario_resultado=dict()
    for cada_letra in texto:
        tupla_letras += cada_letra,
    for letra_pa_juntar in tupla_letras:
        while letra_pa_juntar != contador:
            diccionario_resultado[contador_key]=(letra_pa_juntar + tupla_letras[contador]),
            contador - 1
    return diccionario_resultado'''


def combinaciones(texto):
    lista_combinaciones = []
    posicion = 0
    for letra_fija in texto:
        palabra = ''

        palabra += texto[posicion:]
        posicion += 1

        lista_combinaciones.append(palabra)
    return lista_combinaciones
def alternador():
    print('hola')

print(combinaciones('hola'))
