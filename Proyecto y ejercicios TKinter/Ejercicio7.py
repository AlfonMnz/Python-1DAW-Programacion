"""
Escribe una función a la que se le pasa un número de cliente y tiene que producir un listado con la lista
de los pedidos del cliente, la fecha y con la cuantía de ese pedido (precio * cantidad)(cuantity order, prize)
Un listado de los pagos efectuados de los clientes y la fecha de los pagos. Produzca la diferencia entre el total
de pagos y el total de los pedidos, status
B) Procesar toda la lista de clientes, totalizando para el conjunto de clientes de la lista.
"""

import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='classicmodels')
cursor = cnx.cursor()


def lista_de_cosas_a_partir_de_un_num_de_cliente(num_cliente):
    consulta = '''SELECT COUNT O.orderNumber,O.orderdate, od.quantityOrdered*od.priceEach as cuantia from orders O, 
orderdetails od WHERE customerNumber={}'''.format(num_cliente)
    cursor.execute(consulta)
    for cosicas in cursor:
        print(cosicas)
lista_de_cosas_a_partir_de_un_num_de_cliente(103)


