
class Productos:
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.compras=[]

    def comprar1(self):
        self.compras.append(Honda_dio)
    def comprar2(self):
        self.compras.append(Honda_CB)
    def comprar3(self):
        self.compras.append(Susuki_ADD)
    def comprar4(self):
        self.compras.append(Susuki_GSX)    
    def datos_motos(self):
        return print(f"CODIGO: {self.codigo} NOMBRE: {self.nombre} PRECIO: {self.precio} ")
    def mostrar_moto(self):
        print("Vehiculos comprados:")
        for n in self.compras:
            n.datos_motos()

Honda_dio=Productos(1000,"Honda dio 125",1000000)
Honda_CB=Productos(1100,"Honda CB 300 R",1200000)
Susuki_ADD=Productos(1110,"Susuki Address 125",1300000)
Susuki_GSX=Productos(1111,"Susuki GSX-S125",2000000)