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
        
    def modificar(self):
        rut= int(input("ingrese el codigo del usuario: "))
        nombre=input("ingrese nombre:")
        apellido=input("ingrese apellido: ")
        edad=int(input("ingrese la edad: "))
        direccion=input("ingrese la direccion: ")
        correo= input("ingrese correo: ")
        for  it in self.usuario:
            if rut==it.rut:
                it.nombre=nombre
                it.apellido=apellido
                it.edad=edad
                it.direccion=direccion
                it.correo=correo
                
                return f'Se cambio datos del usuario: {it.nombre}'
        print("Cambio exitoso!.....")
    

    def eliminar(self):
        rut=int(input("ingrese rut: "))
        for it in self.usuario:
            if rut == it.rut:
                self.usuario.remove(it)
            print("Usuario eliminado...")
