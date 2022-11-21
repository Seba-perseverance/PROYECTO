from Usuario import usuario
from Boleta import *
from Venta import *

class menu:

    def __init__():
        
        print("-----------Clientes---------")
        print("1.- Agregar cliente")
        print("2.- Mostrar clientes")
        print("3.- Modificar datos de cliente")
        print("4.- Eliminar cliente")

        op=int(input("Eliga una opcion..."))
        if op ==1:
            print("Solicitando datos de usuario ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            nuevoU = usuario(rut,nombre,apellido,edad,direccion,correo)
            nuevoU.create()
            print("Usuario guardado exitosamente! \n")
        elif op==2:
            usuario.mostrar()
        elif op==3:
            id=int(input("Ingrese el id del usuario..."))
            print("Solicitando datos de usuario ...\n")
            rut = int(input("Ingrese rut ... "))
            nombre= input("Ingrese el nombre... ")
            apellido = input("Ingrese el apellido... ")
            edad= int(input("Ingrese la edad... "))
            direccion = input("Ingrese la direccion... ")
            correo = input("Ingrese el correo... ")
            
            
            usuario.modificar(id,rut,nombre,apellido,edad,direccion,correo)
            
        if op==4:
            id =int(input("Ingrese id..."))
            
            usuario.eliminar(id)
menu.__init__()