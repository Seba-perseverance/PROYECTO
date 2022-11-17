from Usuario import cliente
from motos import *
from Venta import *
u1=cliente(' '," "," ","","","")
moto=Ventas(' ','','')

def option_client():
    print("-----------Clientes---------")
    print("1.- Agregar cliente")
    print("2.- Mostrar clientes")
    print("3.- Modificar datos de cliente")
    print("4.- Eliminar cliente")
def motos():
    print("-----------MOTOS---------")
    print("1.- Honda dio 125")
    print("2.- Honda CB 300 R")
    print("3.- Susuki Address 125")
    print("4.- Susuki  GSX-S125")
    print("5.- Mostrar carrito")

op = 0      
while op != 5:
    option_client()
    op=int(input("ingrese un numero"))
    if op == 1:
        u1.create()
    elif op == 2:
        u1.mostrar()
    elif op == 3:
        
        u1.modificar()
    elif op == 4:
        u1.eliminar()
opcion = 0
while opcion != 6:
    motos()
    opcion=int(input("ingrese el modelo a comprar: "))
    if opcion == 1:
        moto.agregar1()
    elif opcion == 2:
        moto.agregar2()
    elif opcion == 3:
        moto.agregar3()
    elif opcion == 4:
        moto.agregar4()    
    elif opcion == 5:
        moto.mostrar_moto()