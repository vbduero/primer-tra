# Nombre: Yaniris Wilson
# Matricula: 1-20-9404
from tkinter import *
from tkinter import ttk

class Tienda:
    def __init__(self):
        self.nombre = " "
        self.telefono = " "
        self.rnc = " "
        self.direccion = " "

    def solicitar_datos(self):
        print('-----------------------------')
        print( 'Ingresar datos de la tienda')
        print('------------------------------')
        self.nombre = input( 'Digite el nombre de la tienda: ')
        self.telefone = input( 'Digite el telefono de la tienda: ')
        self.rnc = input( "Digite el RNC de la tienda: ")
        self.direccion = input( 'Digite la direccion de la tienda: ')

class Usuario:
    def __init__ (self):
        self.nombre = " "
        self.cargo = " "

    def solicitar_datos(self):
        print('---------------------------')
        print( 'Ingresar datos del usuario')
        print('---------------------------')
        self.nombre = input( 'Digite el nombre del usuario: ')
        self.cargo = input( 'Digite el cargo del usuario: ')

class Cliente:
    def __init__(self):
        self.nombre = " "
        self.telefono = " "
        self.codigo = " "

    def solicitar_datos(self):
        print('--------------------------')
        print('Ingresar datos del cliente')
        print('---------------------------')
        self.nombre = input( 'Digite el nombre del cliente: ')
        self.telefono = input( 'Digite el telefono del cliente: ')
        self.codigo = input('Digite el codigo del cliente: ')

class Producto:
     def _init_(self):
        self.cantidad = 0
        self.precio = 0
        self.nombre = " "
        self.costo_total = 0
        self.itbis_total = 0 

     def calcular_costo_total(self):
        self.costo_total = self.cantidad * self.precio
     def calcular_itbis_total(self):
        self.itbis_total = self.costo_total * 0.18

     def solicitar_datos(self):
        print('-------------------------')
        print( 'Ingresar datos del producto')
        print('--------------------------')
        self.nombre = input( 'Digite el nombre del producto: ')
        self.precio = float(input('Digite el precio del producto: '))
        self.cantidad = int(input( 'Digite la cantidad del pro: '))

class Factura:
    def __init__(self, tienda, usuario, cliente, lista_productos):
        self.tienda = tienda
        self.lista_productos = lista_productos
        self.cliente = cliente
        self.usuario = usuario
        self.monto = 0

    def obtener_datos_tienda(self):
        self.tienda.solicitar_datos()
    def obtener_datos_usuario(self):
        self.usuario.solicitar_datos()
    def obtener_datos_cliente(self):
        self.cliente.solicitar_datos()
    def registrar_productos(self):
        while True:
            print('Facturar un producto?')
            print('1 - SI')
            print('2 - NO')
            op = int(input('Digite la opcion deseada: '))
            if op == 2:
                break
            else:
                producto = Producto()
                producto.solicitar_datos()
                producto.calcular_costo_total()
                self.lista_productos.append(producto)

        while True:
            print('Pagar ITBIS?')
            print('1 - SI')
            print('2 - NO')
            op = int(input( 'Digite la opcion deseada: '))
            if op == 1:
               break
            else:
                self.costo_final = self.monto + (self.monto * 0.19)

    def procesar_factura(self):
        for producto in self.lista_productos:
            self.monto += producto.costo_total

    def imprimir_factura(self):
        print('=' * 30)
        print('FACTURA')
        print('=' * 30)

        print( 'DATOS TIENDA: ')
        print('-' * 30)
        print(f'NOMBRE: {self.tienda.nombre}')
        print(f'TELEFONO: {self.tienda.telefono}')
        print(f'RNC: {self.tienda.rnc}')
        print(f'DIRECCION: {self.tienda.direccion}')
        print('-' * 30)


        print( 'DATOS USUARIO: ')
        print('-' * 30)
        print(f'NOMBRE: {self.usuario.nombre}')
        print(f'CARGO: {self.usuario.cargo}')
        print('-' *  30)

        print( 'DATOS CLIENTE:')
        print('-' * 30)
        print (f' NOMBRE: {self.cliente.nombre}')
        print(f' TELEFONO: {self.cliente.telefono}')
        print(f'CODIGO: {self.cliente.codigo}')
        print('-' * 30)

        print( 'LISTADO PRODUCTOS: ')
        print('-' * 30)
        for producto in self.lista_productos:
            print(f'NOMBRE: {producto.nombre} - PRECIO: {producto.precio} - CANTIDAD: {producto.cantidad} - TOTAL: {producto.costo_total} - ITBIS: {producto.itbis_total}')

        print('RESUMEN:')
        print('-' * 30)
        print(f'CANTIDAD PRODUCTO FACTURADOS: {len(self.lista_productos)}')
        print(f'MONTO TOTAL : {self.monto}')
        print(f'ITBIS FINAL : {self.monto *  0.19}')
        print( '-' * 30)

    def facturar (self):
        print('=' * 30)
        print( "EL EXITO.COM ")
        print('=' * 30)
        self.obtener_datos_tienda()
        self.obtener_datos_usuario()
        self.obtener_datos_cliente()
        self.registrar_productos()
        self.procesar_factura()
        self.imprimir_factura()
        print('-' * 30)

factura = Factura(tienda=Tienda(), usuario=Usuario(), cliente=Cliente(), lista_productos=[])
factura.facturar()


Cliente = Tk()
    #Cliente = Cliente(root)
Cliente.mainloop()








