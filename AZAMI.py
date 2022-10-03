
from tkinter import ttk
from tkinter import *



print ("AZAMI S.A.S")
print ("NIT 32435465")
print ("TEL: 3142769220")
print ("-" * 30)
print ("TERMINAL NEIVA HUILA")
print ("CAJERO: Bermeo Duero Valentina")

#LIBRERIA tiempo
import datetime
tiempo =datetime.datetime.now()
print(tiempo)
print("{}:{}:{}".format(tiempo.day,tiempo.month,tiempo.year))
print("{}:{}:{}".format(tiempo.hour,tiempo.minute,tiempo.second))


class Cliente:

    def __init__(self, root):
        self.wind = root
        self.wind.title("RECIBO")
        self.wind.geometry("850x600")
        self.wind.config(bg="teal")
        

    def __init__(self):
        self.nombrecli = " "
        self.cedulacli = " "


    def datos(self):
        print('--------------------------')
        print('CLIENTE')
        print('---------------------------')
        self.nombrecli = input( 'Digite el nombre del cliente: ')
        self.cedulacli = input( 'Digite la cedula del cliente: ')

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
        self.itbis_total = self.costo_total * 0.19

    def so_datos(self):
        print('-------------------------')
        print( 'PRODUCTO')
        print('--------------------------')
        self.nombre = input( 'Digite el nombre del producto: ')
        self.precio = float(input('Digite el precio del producto:$ '))
        self.cantidad = int(input( 'Digite la cantidad del producto: '))

class Factura:
    def __init__(self, cliente, lista_productos):
        self.lista_productos = lista_productos
        self.cliente = cliente
        self.monto = 0
    
    def re_productos(self):
        while True:
            print('Facturar un producto?')
            print('1 - SI')
            print('2 - NO')
            va = int(input('Digite la opcion deseada: '))
            if va == 2:
                print("Inicia de nuevo")
                break
            else:
                producto = Producto()
                producto.so_datos()
                producto.calcular_costo_total()
                self.lista_productos.append(producto)
        
        while True:
            print('Pagar con tarjeta')
            print('1 - SI')
            print('2 - NO')
            va = int(input( 'Digite la opcion deseada: '))
            if va == 1:
               print("No es permitido, estamos trabajando en ello")
            else:
                print("okay")
                break

    def procesar_fac(self):
        for producto in self.lista_productos:
            self.monto += producto.costo_total
        print ("=" * 35)
        print (f' NOMBRE : {self.cliente.nombrecli}')
        print (f' CEDULA : {self.cliente.cedulacli}') 
        #print (f' NOMBRE : {self.cliente.nombrecli}')   
        print(f'SUBTOTAL : {self.monto}')
        print('-' * 35)
        print(f'CANTIDAD PRODUCTO FACTURADOS: {len(self.lista_productos)}')
        print( 'LISTADO PRODUCTOS: ')
        print('-' * 30)
        for producto in self.lista_productos:
            print(f'NOMBRE: {producto.nombre} - PRECIO: {producto.precio} - CANTIDAD: {producto.cantidad} - TOTAL: {producto.costo_total} ')
        print(f'IVA FINAL : {self.monto  *  0.19}')
        print(f'TOTAL : {self.monto  + (self.monto*  0.19)}')
        print( '-' * 30)

    def fin (self):
        print('=' * 30)
        print( "EL EXITO.COM ")
        print('=' * 30)
        #self.datos()
        self.re_productos()
        self.procesar_fac()
        print('-' * 30)

factura=Cliente()
factura.datos()
factura = Factura( cliente=Cliente(), lista_productos=[])
#factura.datos()
#factura.registrar_productos()
#factura.procesar_factura()
factura.fin()


root = Tk()

root.title("RECIBO")

root.mainloop()


