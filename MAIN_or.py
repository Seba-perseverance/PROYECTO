from Usuario import *
from Boleta import *
from Venta import *
from trabajador import *
from cliente import *

class menu:

    def __init__():
        
        print("-----------Clientes---------")
        print("1.- Agregar cliente")
        print("2.- Mostrar clientes")
        print("3.- Modificar datos de cliente")
        print("4.- Eliminar cliente")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            print("Solicitando datos ...\n")
            
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            nuevoU =cliente(rut,nombre,apellido,edad,direccion,correo)
            nuevoU.create1()
            print("Usuario guardado exitosamente! \n")
        elif op==2:
            cliente.mostrar()
        elif op==3:
            
            cliente.mostrar()
            id=int(input("Ingrese el id del usuario..."))
            print("Solicitando datos de usuario ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            
            cliente.modificar(id,rut,nombre,apellido,edad,direccion,correo)
            
        if op==4:
            id =int(input("Ingrese id..."))
            
            cliente.eliminar(id)
    def menuProductos():
        print("-----------Productos---------")
        print("1.- Agregar producto")
        print("2.- Mostrar producto")
        print("3.- Modificar producto")
        print("4.- Eliminar cliente")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            print("Solicitando datos ...\n")
            nombre= input("Ingrese el nombre... ")
            marca=input("Ingrese la marca...")
            precio=int(input("Ingrese el precio..."))
            nuevoP = productos(nombre,marca,precio)
            nuevoP.creaP()
            print("Producto guardado exitosamente! \n")
        elif op==2:
            productos.mostrarP()
        elif op==3:
            id=int(input("Ingrese el id del usuario..."))
            print("Solicitando datos de usuario ...\n")
            nombre= input("Ingrese el nombre... ")
            marca=input("Ingrese la marca...")
            precio=int(input("Ingrese el precio..."))
            productos.modificarP(nombre,marca,precio)
            
        if op==4:
            id =int(input("Ingrese id..."))
            
            productos.eliminarP(id)
    def menuEmpleado():
        print("-----------Trabajadores---------")
        print("1.- Agregar trabajadores")
        print("2.- Mostrar trabajadores")
        print("3.- Modificar datos de trabajadores")
        print("4.- Eliminar trabajadores")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            print("Solicitando datos ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            especialidad =input("Ingrese la especialidad")
            nuevoU = trabajador(rut,nombre,apellido,edad,direccion,correo,especialidad)
            nuevoU.creaT()
            print("Usuario guardado exitosamente! \n")
        elif op==2:
            trabajador.mostrarT()
        elif op==3:
            id=int(input("Ingrese el id del usuario..."))
            print("Solicitando datos de usuario ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            
            
            trabajador.modificarT(id,rut,nombre,apellido,edad,direccion,correo)
            
        if op==4:
            id =int(input("Ingrese id..."))
            
            trabajador.eliminarT(id)

    
    def menuPRINCIPAL():
        print("-----------MENÚ---------")
        print("1.- trabajar con clientes")
        print("2.- trabajar con trabajadores")
        print("3.- trabajar con productos")
        print("0.- cerrar sesion...")
        op=int(input("Ingrese la opcione deseada:  "))
        if op == 1:
            menu.__init__()
        elif op == 2:
            menu.menuEmpleado()
        elif op == 3:
            menu.menuProductos()
        else:
            print("cerrado sesion...")    
menu.menuPRINCIPAL()