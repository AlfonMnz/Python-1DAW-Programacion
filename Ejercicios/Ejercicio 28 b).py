'''Ejercicio 28 b) Igual que el ejercicio 28 pero de más a menos.'''

cad=input('introduce una frase o palabra\n')
lista = [cad[::-1]for pos in range(1,(len(cad)+1))]
print (lista)