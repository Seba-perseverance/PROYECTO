from Usuario import *
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
        
    def modificar1(idCli,op1,u):
        sql=f'UPDATE cliente SET {u}={op1} WHERE idcliente={idCli}'
        db=DataBase()
        db.modific(sql)
    def modificar2(idCli,op1,u):
        sql=f'UPDATE cliente SET {u}="{op1}" WHERE idcliente={idCli}'
        db=DataBase()
        db.modific(sql)
    def eliminar(id):
        sql=f'DELETE FROM cliente WHERE idcliente={id};'
        db=DataBase()
        db.Eliminar(sql)
    
    
        