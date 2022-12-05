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
        
    def modificarP1(idPro,op1,u):
        sql=f'UPDATE producto SET {u}={op1} WHERE idproducto={idPro}'
        db=DataBase()
        db.modific(sql)
    def modificarP2(idPro,op1,u):
        sql=f'UPDATE producto SET {u}="{op1}" WHERE idproducto={idPro}'
        db=DataBase()
        db.modific(sql)

    def eliminarP(id):
        sql=f'DELETE FROM producto WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)


