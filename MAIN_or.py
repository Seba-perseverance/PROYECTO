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
        print("4.- Eliminar cliente")
    
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
            nuevoU.crea()
            print("Usuario guardado exitosamente! \n")
        elif op==2:
            trabajador.mostrar()
        elif op==3:
            id=int(input("Ingrese el id del usuario..."))
            print("Solicitando datos de usuario ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            
            
            trabajador.modificar(id,rut,nombre,apellido,edad,direccion,correo)
            
        if op==4:
            id =int(input("Ingrese id..."))
            
            trabajador.eliminar(id)

    
    def menuPRINCIPAL():
        print("-----------MENÚ---------")
        print("1.- trabajar con clientes")
        print("2.- trabajar con trabajadores")
        print("0.- cerrar sesion...")
        op=int(input("Ingrese la opcione deseada:  "))
        if op == 1:
            menu.__init__()
        elif op == 2:
            menu.menuEmpleado()
        else:
            print("cerrado sesion...")    
menu.menuPRINCIPAL()