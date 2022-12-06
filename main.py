#Modulos importados
from Usuario import *
from trabajador import *
from cliente import *
from Conectar import *
from compras import *
import os
    
class menu:
        #CRUD de clientes
    def __init__():
        
        print("----------- Trabajar Cliente---------")
        print("1.- Agregar cliente.")
        print("2.- Mostrar clientes.")
        print("3.- Modificar datos de cliente.")
        print("4.- Eliminar cliente.")
        print("5.- Regresar al MENÚ principal.")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            #Agregar clientes
            os.system('cls')
            print("Solicitando datos ...\n")
            rut = int(input("Ingrese rut ..."))
            nombre= input("Ingrese el nombre...")
            apellido = input("Ingrese el apellido...")
            edad= int(input("Ingrese la edad..."))
            direccion = input("Ingrese la direccion...")
            correo = input("Ingrese el correo...")
            nuevoU =cliente(rut,nombre,apellido,edad,direccion,correo)
            nuevoU.create1()
            print("Cliente guardado exitosamente!...")
            
        elif op==2:
            #Mostrar clientes
            os.system('cls')
            cliente.mostrar()
            
        elif op==3:
            #Actualizar un cliente
            os.system('cls')
            cliente.mostrar()
            idCli=int(input("Ingrese el id del cliente..."))
            while True:
                os.system('cls')
                print("-----------Modificar datos del cliente---------")
                print("1.- cambiar rut...")
                print("2.- cambiar nombre...")
                print("3.- cambiar apellido...")
                print("4.- cambiar edad...")
                print("5.- cambiar direccion...")
                print("6.- cambiar correo...")
                print("7.- Salir...")
                op=int(input("Ingrese una opcion..."))
        
                try:
                    if op==1:
                        u='rut'
                        op1=int(input("Ingrese el nuevo rut..."))
                        cliente.modificar1(idCli,op1,u)
                    elif op ==2:
                        u='nombre'
                        op1=input("Ingrese el nuevo nombre...")
                        cliente.modificar2(idCli,op1,u)       
                    elif op ==3:
                        u='apellido'
                        op1=input("Ingrese el nuevo apellido...")
                        cliente.modificar2(idCli,op1,u)         
                    elif op ==4:
                        u='direccion'
                        edad=input("Ingrese la nueva edad...")
                        cliente.modificar2(idCli,op1,u)          
                    elif op ==5:
                        u='edad'
                        op1=input("Ingrese la nueva direccion...")
                        cliente.modificar2(idCli,op1,u)          
                    elif op ==6:
                        u='correo'
                        op1=input("Ingrese el nuevo correo...")
                        cliente.modificar2(idCli,op1,u)
                    elif op ==7:
                        print("Cerrando MENÚ...")
                        break          
                    else:
                        print("error")
                        continue
                        
                except Error as e:
                    print (e) 
                
        elif op==4:
            #Eliminar un cliente
            os.system('cls')
            cliente.mostrar()
            id =int(input("Ingrese id... "))
            cliente.eliminar(id)
            #Regresar al menù
        elif op==5:
            os.system('cls')
            print("Regresaste al MENÚ principal...")
            menu.menuPrincipal()
        else:
            print("error...")
            
        #CRUD DE productos
    def menuProductos():
        print("-----------Trabajar producto---------")
        print("1.- Agregar producto.")
        print("2.- Mostrar producto.")
        print("3.- Modificar producto.")
        print("4.- Eliminar producto.")
        print("5.- Regresar al MENÚ principal.")
        op=int(input("Eliga una opcion..."))
        #Agregar producto
        if op ==1:
            os.system('cls')
            print("Solicitando datos ...\n")
            nombre= input("Ingrese el nombre... ")
            marca=input("Ingrese la marca...")
            precio=int(input("Ingrese el precio..."))
            nuevoP = productos(nombre,marca,precio)
            nuevoP.creaP()
            print("Producto guardado exitosamente! \n")
            input('Presione enter para continuar...')
        #Mostrar todos los productos
        elif op==2:
            os.system('cls')
            productos.mostrarP()
            input('Presione enter para continuar...')
        #Modificar un producto elegido
        elif op==3:
            os.system('cls')
            productos.mostrarP()
            idPro=int(input("Ingrese el id del cliente..."))
            while True:
                os.system('cls')
                print("-----------Modificar datos del producto---------")
                print("1.- cambiar nombre del producto...")
                print("2.- cambiar marca del producto...")
                print("3.- cambiar precio del producto...")
                print("4.- Salir...")
                op=int(input("Ingrese una opcion..."))
                #u=nombre de la columna
                try:
                    if op==1:
                        u='nombre'
                        op1=int(input("Ingrese el nuevo nombre..."))
                        productos.modificarP2(idPro,op1,u)
                    elif op ==2:
                        u='marca'
                        op1=input("Ingrese la nueva marca...")
                        productos.modificarP2(idPro,op1,u)       
                    elif op ==3:
                        u='precio'
                        op1=input("Ingrese el nuevo precio...")
                        productos.modificarP1(idPro,op1,u)               
                    elif op ==4:
                        print("Cerrando MENÚ...")
                        break          
                    else:
                        print("error")
                        break
                        
                except Error as e:
                    print (e)    
        #Eliminar producto
        elif op==4:
            os.system('cls')
            productos.mostrarP()
            id =int(input("Ingrese id..."))
            productos.eliminarP(id)
            input('Presione enter para continuar...')
    def menuEmpleado():
        
        print("-----------Trabajar trabajador---------")
        print("1.- Agregar trabajadores.")
        print("2.- Mostrar trabajadores.")
        print("3.- Modificar datos de trabajadores.")
        print("4.- Eliminar trabajadores.")
        try:
            op=int(input("Eliga una opcion..."))
            if op ==1: # ingresar trabajador
                os.system('cls')
                print("Solicitando datos ...\n")
                rut = int(input("Ingrese rut ..."))
                nombre= input("Ingrese el nombre...")
                apellido = input("Ingrese el apellido...")
                edad= int(input("Ingrese la edad... "))
                direccion = input("Ingrese la direccion...")
                correo = input("Ingrese el correo...")
                cargo =input("Ingrese el cargo...")
                nuevoU = trabajador(rut,nombre,apellido,edad,direccion,correo,cargo)
                nuevoU.creaT()
                print("Usuario guardado exitosamente! \n")
                input('Presione enter para continuar...')
            elif op==2:#mostrar todos los trabajadores
                os.system('cls')
                trabajador.mostrarT()
                input('Presione enter para continuar...')
            elif op==3:#modificar  dato del trabajdor
                os.system('cls')
                trabajador.mostrarT()
                idTra=int(input("Ingrese el id del trabajador..."))
                while True:
                    os.system('cls')
                    print("-----------Modificar datos del trabajador---------")
                    print("1.- cambiar rut...")
                    print("2.- cambiar nombre...")
                    print("3.- cambiar apellido...")
                    print("4.- cambiar edad...")
                    print("5.- cambiar direccion...")
                    print("6.- cambiar correo...")
                    print("7.- cambiar cargo...")
                    print("8.- Salir...")
                    op=int(input("Ingrese una opcion..."))
                
                    try:
                        if op==1:
                            u='rut'
                            op1=int(input("Ingrese el nuevo rut..."))
                            trabajador.modificarT1(idTra,op1,u)
                        elif op ==2:
                            u='nombre'
                            op1=input("Ingrese el nuevo nombre...")
                            trabajador.modificarT2(idTra,op1,u)         
                        elif op ==3:
                            u='apellido'
                            op1=input("Ingrese el nuevo apellido...")
                            trabajador.modificarT2(idTra,op1,u)            
                        elif op ==4:
                            u='edad'
                            op1=int(input("Ingrese la nueva edad..."))
                            trabajador.modificarT1(idTra,op1,u)           
                        elif op ==5:
                            u='direccion'
                            op1=input("Ingrese la nueva direccion...")
                            trabajador.modificarT2(idTra,op1,u)            
                        elif op ==6:
                            u='correo'
                            op1=input("Ingrese el nuevo correo...")
                            trabajador.modificarT2(idTra,op1,u)
                        elif op ==7:
                            u='cargo'
                            op1=input("Ingrese el nuevo cargo...")
                            trabajador.modificarT2(idTra,op1,u) 
                        elif op ==8:
                            print("Cerrando MENÚ...")
                            break          
                        else:
                            print("error")
                            continue
                            
                    except Error as e:
                        print (e)  
            elif op==4:#eliminar trabajador
                os.system('cls')
                trabajador.mostrarT()
                id =int(input("Ingrese id..."))
                trabajador.eliminarT(id)
                input('Presione enter para continuar...')
            else:
                print("error...")
                
        except Error as e:
            print(e)
    def menuCompras():#compras
        while True:
            os.system('cls')
            print("-----------MENÚ productos-------------")
            print("1.- Comprar producto.")
            print("2.- Mostrar compras.")
            print("3.- Volver al menù")
            op=int(input("Ingrese una de las opciones..."))
            if op == 1:
                os.system('cls')
                cliente.mostrar()
                idcli=int(input("Ingrese el id del cliente..."))
                print("-----------Productos---------")
                print("1.- Honda dio 125.")
                print("2.- Honda CB 300 R.")
                print("3.- Susuki Address 125.")
                print("4.- Susuki GSX-S125.")
                print("0.- Cerrar sesion...")
                idPro=int(input("Eliga un producto..."))
                c=compra(idcli,idPro)
                c.ingresarCompra()
                input('Presione enter para continuar...')
            elif op == 2:
                os.system('cls')
                compra.mostrarCompras()
                input('Presione para continuar...')
            elif op == 3:
                break
            else:
                break
            
    def menuPrincipal():
        while True:
            os.system('cls')
            print("-----------MENÚ---------")
            print("1.- Trabajar con clientes.")
            print("2.- Trabajar con trabajadores.")
            print("3.- Trabajar con productos.")
            print("4.- Comprar productos.")
            print("0.- Cerrar sesion...")
            try:
                op=int(input("Ingrese una de las opciones:  "))
                if op == 1:
                    os.system('cls')
                    menu.__init__()
                    input('Presione enter para continuar...')
                elif op == 2:
                    os.system('cls')
                    menu.menuEmpleado()
                    input('Presione enter para continuar...')
                elif op == 3:
                    os.system('cls')
                    menu.menuProductos()
                    input('Presione enter para continuar...')
                elif op == 4:
                    os.system('cls')
                    menu.menuCompras()
                    input('Presione enter para continuar...')
                
                elif op ==0:
                    os.system('cls')
                    print("Sesion cerrada....")
                    break
                else:
                    os.system('cls')
                    print("Ingrese a una de las opciones del MENÚ...")
                    input('Presione enter para continuar...')  
            except  :
                input("Eliga una de las opciones del MENÚ...")  
                continue
u=menu.menuPrincipal()
#menu