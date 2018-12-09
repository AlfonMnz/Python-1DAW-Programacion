'''Ejercicio 33. Escribe una función en la que le paso 2 puntos y te da la suma vectorial'''


def punto(p1, p2):
    puntototal = p1[0] + p2[0], p1[1] + p2[1]
    return puntototal


x1 = int(input('introduce la coordenada x del primer punto:\n'))
y1 = int(input('introduce la coordenada y del primer punto:\n'))
x2 = int(input('introduce la coordenada x del segundo punto:\n'))
y2 = int(input('introduce la coordenada y del segundo punto:\n'))
punto1 = x1, y1
punto2 = x2, y2
print(punto(punto1, punto2))
