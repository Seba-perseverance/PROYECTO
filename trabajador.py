from Usuario import *
from Conectar import *
import os
class trabajador(usuario):
    def __init__(self, rut, nombre, apellido, edad, direccion, correo,especialidad):
        super().__init__(rut, nombre, apellido, edad, direccion, correo)
        self.especialidad=especialidad

    def creaT(self):
        sql=f'INSERT INTO trabajador (rut,nombre,apellido,edad,direccion,correo,cargo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}","{self.especialidad}")'
        db=DataBase()
        db.insert(sql)
    
    def mostrarT():
        sql=f'SELECT * FROM trabajador'
        db=DataBase()
        db.list(sql)
        
    def modificarT(idTra):
        while True:
            os.system('cls')
            print("-----------MENÚ---------")
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
                    rut=int(input("Ingrese el nuevo rut..."))
                    sql=f'UPDATE cliente SET rut={rut} WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)
                elif op ==2:
                    nombre=input("Ingrese el nuevo nombre...")
                    sql=f'UPDATE cliente SET nombre="{nombre}" WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)           
                elif op ==3:
                    apellido=input("Ingrese el nuevo apellido...")
                    sql=f'UPDATE cliente SET apellido="{apellido}" WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==4:
                    edad=int(input("Ingrese la nueva edad..."))
                    sql=f'UPDATE cliente SET edad={edad} WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==5:
                    direccion=input("Ingrese la nueva direccion...")
                    sql=f'UPDATE cliente SET direccion="{direccion}" WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)            
                elif op ==6:
                    correo=input("Ingrese el nuevo correo...")
                    sql=f'UPDATE cliente SET correo="{correo}" WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql)
                elif op ==7:
                    cargo=input("Ingrese el nuevo cargo...")
                    sql=f'UPDATE cliente SET cargo="{cargo}" WHERE idtrabajador={idTra}'
                    db=DataBase()
                    db.modific(sql) 
                elif op ==8:
                    print("Cerrando MENÚ...")
                    break          
                else:
                    print("error")
                    continue
                    
            except Error as e:
                print (e)   

    def eliminarT(id):
        sql=f'DELETE FROM usuario WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)