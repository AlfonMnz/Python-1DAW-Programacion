'''Ejercicio 29 c) que sean multiplos de 3 y de 7 a la vez'''

lista = [num for num in range(1000) if num % 3 == 0 if num % 7 == 0]
print(lista)
