from Conectar import *
class usuario:

    
    def __init__(self,id,rut,nombre,apellido,edad,direccion,correo):
        self.id=id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion        
        self.correo = correo
    
    def create(self):
        sql=f'INSERT INTO cliente (idcliente,rut,nombre,apellido,edad,direccion,correo) VALUES ({self.id}{self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}")'
        db=DataBase()
        db.insert(sql)
    def mostrar():
        db=DataBase()
        db.list()
        
    def modificar(id,rut,nombre,apellido,edad,direccion,correo):

        sql=f'UPDATE usuario SET rut={rut},nombre="{nombre}",apellido="{apellido}",edad={edad},direccion="{direccion}",correo="{correo}" Where idusuario={id};'
        db=DataBase()
        db.modific(sql)

    

    def eliminar(id):
        sql=f'DELETE FROM usuario WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)