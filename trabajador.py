from usuario import *
from Conectar import *
import os
class trabajador(usuario):
    def __init__(self, rut, nombre, apellido, edad, direccion, correo,cargo):
        super().__init__(rut, nombre, apellido, edad, direccion, correo)
        self.cargo=cargo

    def creaT(self):
        sql=f'INSERT INTO trabajador (rut,nombre,apellido,edad,direccion,correo,cargo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}","{self.cargo}")'
        db=DataBase()
        db.insert(sql)
    
    def mostrarT():
        sql=f'SELECT * FROM trabajador'
        db=DataBase()
        db.list(sql)
        
    def modificarT1(idTra,op1,u):
        sql=f'UPDATE trabajador SET {u}={op1} WHERE idtrabajador={idTra}'
        db=DataBase()
        db.modific(sql) 
    def modificarT2(idTra,op1,u):
        sql=f'UPDATE trabajador SET {u}="{op1}" WHERE idtrabajador={idTra}'
        db=DataBase()
        db.modific(sql) 

    def eliminarT(id):
        sql=f'DELETE FROM trabajador WHERE idtrabajador={id};'
        db=DataBase()
        db.Eliminar(sql)