from Productos import *
class compra:
    def __init__(self,producto_idproducto,boleta_idboleta):
        self.idProducto=producto_idproducto
        self.idBoleta=boleta_idboleta
    

    def ingresarCompra(self):
        sql=f'INSERT INTO compra (cliente_idcliente,producto_idproducto,boleta_idboleta) VALUES (1,{self.idProducto},1)'
        db=DataBase()
        db.insert(sql)