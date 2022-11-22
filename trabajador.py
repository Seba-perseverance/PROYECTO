from Usuario import *
class trabajador(usuario):
    def __init__(self, rut, nombre, apellido, edad, direccion, correo,especialidad):
        super().__init__(rut, nombre, apellido, edad, direccion, correo)
        self.especialidad=especialidad

    def crea(self):
        sql=f'INSERT INTO trabajador (rut,nombre,apellido,edad,direccion,correo,especialidad) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}","{self.especialidad}")'
        db=DataBase()
        db.insert(sql)