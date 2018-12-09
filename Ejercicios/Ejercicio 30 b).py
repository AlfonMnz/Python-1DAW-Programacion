'''Ejercicio 30 a) y b). Tenemos que crear palabras de 2 sílabas con todas las combinaciones del apartado anterior'''


def combinaciones():
    return [cons + vocal for cons in 'BCDFGHJKLMNÑPQRSTVWXYZ' for vocal in 'aeiou']


def palabras():
    return [sil1 + sil2 for sil1 in combinaciones() for sil2 in combinaciones()]


print(len(palabras()))
print(palabras())
