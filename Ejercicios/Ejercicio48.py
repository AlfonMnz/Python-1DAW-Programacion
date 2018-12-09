'''Ejercicio 48. Define un Anagrama una palabra con las letras de otra. Escribe una función que se pasen dos palabras y nos
diga si la segunda es un anagrama de la otra'''

def anagrama(palabra1,palabra2):
    return sorted(palabra1)== sorted(palabra2)


'''print(anagrama('hola','polla'))'''

print ("%s %10.s %5.s" %(anagrama, "hola", "polla"))