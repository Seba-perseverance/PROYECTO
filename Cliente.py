
class cliente:

    
    def __init__(self,rut,nombre,apellido,edad,direccion,correo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion        
        self.correo = correo
        self.compra=[]
        self.clientes = []
    def datos(self):
        print(f"RUT: {self.rut} NOMBRE: {self.nombre} APELLIDO: {self.apellido} EDAD: {self.edad} DIRECCION: {self.direccion} CORREO: {self.correo}")
    def mostrar(self):
        for cliente in self.clientes:
            cliente.datos()
        
    def modificar(self):
        rut= int(input("ingrese el codigo del usuario: "))
        nombre=input("ingrese nombre:")
        apellido=input("ingrese apellido: ")
        edad=int(input("ingrese la edad: "))
        direccion=input("ingrese la direccion: ")
        correo= input("ingrese correo: ")
        for  it in self.clientes:
            if rut==it.rut:
                it.nombre=nombre
                it.apellido=apellido
                it.edad=edad
                it.direccion=direccion
                it.correo=correo
                
                return f'Se cambio datos del usuario: {it.nombre}'
        print("Cambio exitoso!.....")
    def create(self):
        rut = int(input("ingrese el rut: "))
        nom = input("ingrese nombre: ")
        ape = input("ingrese apellido: ")
        edad = int(input("ingrese la edad: "))
        direccion = input("ingrese la direccion: ")
        corr = input("ingrese correo: ")
        client=cliente(rut,nom,ape,edad,direccion,corr)
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
            print("Usuario eliminado...")
