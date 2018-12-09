'''Ejercicio 45. Vamos a crear un diccionario español inglés, cada palabra en español va a contener la palabra equivalente en inglés
la función se va a llamar traduce aprende(dic, cast, ingles) aprende introduce en la clave castellano la palabra en inglés
Vamos a crear una lista de tuplas de palabra castellano inglés (pares)'''


def aprende(dic, castellano, ingles):
    dic[castellano] = ingles


def traducción(pal_esp):
    if pal_esp in diccionario.keys():
        return diccionario[pal_esp]
    else:
        print('Recuerda las mayúsculas')


def aprende_lista(dic, pares_palabras):
    for par in pares_palabras:
        aprende(dic, par[0], par[1])


diccionario = dict()
dias_semana = [('Lunes', 'Monday'), ('Martes', 'Tursday'), ('Miercoles', 'Wednesday')
    , ('Jueves', 'Thursday'), ('Viernes', 'Friday'), ('Sábado', 'Saturday'), ('Domingo', 'Sunday')]
aprende_lista(diccionario, dias_semana)

texto_traducir = input('introduce algo a traducir:\n')
print(traducción(texto_traducir))
