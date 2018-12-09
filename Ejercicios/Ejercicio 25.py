'''Ejercicio 25. Introduce una lista que le metes un número y o ordena automáticamente'''
from random import randint

lista = []

num = int(input('introduce un número:\n'))
while num != 0:
    pos = 0
    if lista == []:
        lista.append(num)
        print('vacia')
    else:

        while pos < len(lista) and num > lista[pos]:
            pos += 1

        lista.insert(pos, num)
        print('insertado en la posición', pos)

print(lista)
