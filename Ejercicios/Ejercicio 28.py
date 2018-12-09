'''Ejercicio 28. Queremos construir una lista por comprensión que contenga, de un texto dado, guarde los caracteres de la cadena
según su posición'''

cad = input('introduce algo:\n')
lista = [reversed(cad[0:pos]) for pos in range(1, len(cad))]
print(lista)
