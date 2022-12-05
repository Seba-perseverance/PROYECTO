from Conectar import *
import os
class productos:
    def __init__(self,nombre,marca,precio):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        

    def creaP(self):
        sql=f'INSERT INTO producto (nombre,marca,precio) VALUES ("{self.nombre}","{self.marca}",{self.precio})'
        db=DataBase()
        db.insert(sql)
    
    def mostrarP():
        sql=f'SELECT * FROM producto'
        db=DataBase()
        db.list(sql)
        
    def modificarP(idPro):
        while True:
            os.system('cls')
            print("-----------MENÚ---------")
            print("1.- cambiar nombre del producto...")
            print("2.- cambiar marca del producto...")
            print("3.- cambiar precio del producto...")
            print("4.- Salir...")
            op=int(input("Ingrese una opcion..."))
        
            try:
                if op==1:
                    nombre=int(input("Ingrese el nuevo nombre..."))
                    sql=f'UPDATE cliente SET nombre={nombre} WHERE idcliente={idPro}'
                    db=DataBase()
                    db.modific(sql)
                elif op ==2:
                    marca=input("Ingrese la nueva marca...")
                    sql=f'UPDATE cliente SET marca="{marca}" WHERE idcliente={idPro}'
                    db=DataBase()
                    db.modific(sql)           
                elif op ==3:
                    precio=input("Ingrese el nuevo precio...")
                    sql=f'UPDATE cliente SET precio="{precio}" WHERE idcliente={idPro}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==4:
                    print("Cerrando MENÚ...")
                    break          
                else:
                    print("error")
                    continue
                    
            except Error as e:
                print (e)    

    def eliminarP(id):
        sql=f'DELETE FROM producto WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)


