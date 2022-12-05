from usuario import *
from Conectar import *
import os
class cliente(usuario):
    def __init__(self,rut,nombre,apellido,edad,direccion,correo):
        super().__init__(rut,nombre,apellido,edad,direccion,correo)
        
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion        
        self.correo = correo
    
    def create1(self):
        sql=f'INSERT INTO cliente (rut,nombre,apellido,edad,direccion,correo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}")'
        db=DataBase()
        db.insert(sql)
    def mostrar():
        sql=f'SELECT * FROM cliente'
        db=DataBase()
        db.list(sql)
        
    def modificar(idCli):
        while True:
            os.system('cls')
            print("-----------MENÚ---------")
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
                    rut=int(input("Ingrese el nuevo rut..."))
                    sql=f'UPDATE cliente SET rut={rut} WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)
                elif op ==2:
                    nombre=input("Ingrese el nuevo nombre...")
                    sql=f'UPDATE cliente SET nombre="{nombre}" WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)           
                elif op ==3:
                    apellido=input("Ingrese el nuevo apellido...")
                    sql=f'UPDATE cliente SET apellido="{apellido}" WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==4:
                    edad=int(input("Ingrese la nueva edad..."))
                    sql=f'UPDATE cliente SET edad={edad} WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==5:
                    direccion=input("Ingrese la nueva direccion...")
                    sql=f'UPDATE cliente SET direccion="{direccion}" WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==6:
                    correo=input("Ingrese el nuevo correo...")
                    sql=f'UPDATE cliente SET correo="{correo}" WHERE idcliente={idCli}'
                    db=DataBase()
                    db.modific(sql)  
                elif op ==7:
                    print("Cerrando MENÚ...")
                    break          
                else:
                    print("error")
                    continue
                    
            except Error as e:
                print (e)       
    def eliminar(id):
        sql=f'DELETE FROM cliente WHERE idcliente={id};'
        db=DataBase()
        db.Eliminar(sql)
    
    
        