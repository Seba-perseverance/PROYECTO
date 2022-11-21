from Conectar import *
class usuario:

    
    def __init__(self,rut,nombre,apellido,edad,direccion,correo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion        
        self.correo = correo
    
    def create(self):
        sql=f'INSERT INTO usuario (rut,nombre,apellido,edad,direccion,correo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}")'
        db=DataBase()
        db.insert(sql)
    def mostrar():
        db=DataBase()
        db.list()
        
    def modificar(self,id):

        sql=f'UPDATE usuario SET rut={self.rut},nombre="{self.nombre}",apellido="{self.apellido}",edad={self.edad},direccion="{self.direccion}",correo="{self.correo}" Where idusuario={id};'
        db=DataBase()
        db.modific(sql)

    

    def eliminar(id):
        sql=f'DELETE FROM usuario WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)