'''Ejercicio 29 b) Escribe una lista que ponga los números múltiplos de 3, de 5 y de 7'''

lista = [num for num in range(1000) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0]
print(lista)