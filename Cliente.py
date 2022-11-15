
class cliente:

    
    def __init__(self,rut,nombre,apellido,correo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.compra=[]
        self.clientes = []
    def datos(self):
        print(f"RUT: {self.rut} NOMBRE: {self.nombre} APELLIDO: {self.apellido} CORREO: {self.correo}")
    def mostrar(self):
        for cliente in self.clientes:
            cliente.datos()
        
    def modificar(self):
        rut= int(input("ingrese el codigo del usuario: "))
        nombre=input("ingrese nombre:")
        apellido=input("ingrese apellido: ")
        correo= input("ingrese correo: ")
        for  it in self.clientes:
            if rut==it.rut:
                it.nombre=nombre
                it.apellido=apellido
                it.correo=correo
                return f'Se cambio nota de asignatura {it.nombre}'
        print("Cambio exitoso!.....")
    def create(self):
        rut = int(input("ingrese el rut: "))
        nom = input("ingrese nombre: ")
        ape = input("ingrese apellido: ")
        corr = input("ingrese correo: ")
        client=cliente(rut,nom,ape,corr)
        for it in self.clientes:
            if it.rut == client.rut:
                return 'ya existe el cliente en bd'
        self.clientes.append(client)
        print("ingresado con exito!....")

    def eliminar(self):
        rut=int(input("ingrese rut: "))
        for it in self.clientes:
            if rut == it.rut:
                self.clientes.remove(it)
            pass
