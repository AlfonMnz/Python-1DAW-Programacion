"""
Hay que crear la clase ColeccionClientes ControlBD Cliente
"""

import mysql.connector


class Cliente:
    def __init__(self, direccion, telefono, num_cliente, nombre, medida_del_pene=18):
        self.direccion = direccion
        self.telefono = telefono
        self.num_cliente = num_cliente
        self.medida_del_pene = medida_del_pene
        self.nombre = nombre


class ColeccionClientes:
    def __init__(self):
        self.dic_cliente = dict()

    def obtener_cliente(self, num_cliente):
        cdb = ControlBD()
        cdb.obtener_cliente(num_cliente)


    def cargar_clientes(self):
        return self.dic_cliente

    def nuevo_cliente(self, direccion, telefono, num_cliente, nombre, medida_del_pene=18):
        cliente = Cliente(direccion,telefono,num_cliente,nombre)
        cdb = ControlBD()
        cdb.insertar_cliente(cliente)

    def modificar_cliente(self, num_cliente, new_num):
        self.dic_cliente[new_num] = self.dic_cliente[num_cliente]
        del self.dic_cliente[num_cliente]


class ControlBD:
    def __init__(self):
        pass

    def crear_conexion(self, usuario='root', password='1234', host='127.0.0.1', database='classicmodels'):
        self.cnx = mysql.connector.connect(user=usuario, password=password, host=host, database=database)

    def cerrar_conexion(self):
        self.cnx.close()
    def obtener_cliente(self,num_cliente):
        self.crear_conexion()
        query = '''SELECT * from customers WHERE customerNumber = {}'''.format(num_cliente)
        c = self.cnx.cursor()
        c.execute(query)
        print(c.fetchall())
        self.cerrar_conexion()
    def insertar_cliente(self,cliente):
        self.crear_conexion()
        c = self.cnx.cursor()

        query = '''INSERT INTO customers (addressLine1,phone,customerNumber,customerName) VALUES ("{}","{}",{},"{}")''' \
            .format(cliente.direccion,cliente.telefono,cliente.num_cliente,cliente.nombre)
        c.execute(query)
        self.cnx.commit()
        self.cerrar_conexion()
def cargar_clientes():
    cdb.crear_conexion()
    c = cnx.cursor()
    query = '''SELECT * FROM customers'''
    c.execute(query)
    for hurfles in c:
        print('hola')
        coll.dic_cliente[hurfles[0]] = hurfles[1:]
    self.cerrar_conexion()
import mysql.connector

def papilla():
    dic_polla = {}
    cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='classicmodels')
    c = cnx.cursor()
    query= '''SELECT * FROM customers'''
    c.execute(query)
    migue = c.fetchmany(5)
    for hurflas in migue:
        print('Numero: {} \n Nombre: {}\n Direccion: {}'.format(hurflas[0],hurflas[1],hurflas[2]))

    print(dic_polla)
papilla()
