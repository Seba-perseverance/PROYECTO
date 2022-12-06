from Productos import *

class compra:
    def __init__(self,cliente_idcliente,producto_idproducto):
        self.idCliente=cliente_idcliente
        self.idProducto=producto_idproducto
    

    def ingresarCompra(self):
        
        sql=f'INSERT INTO compra (cliente_idcliente, nombre_emp,producto_idproducto,fecha) VALUES({self.idCliente},"CONSTRUCTORA S.A",{self.idProducto},sysdate());'
        db=DataBase()
        db.insert(sql)
    
    def mostrarCompras():
        sql=f'SELECT * FROM compra'
        db=DataBase()
        db.list(sql)