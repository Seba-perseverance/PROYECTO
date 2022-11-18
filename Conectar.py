from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        self.username= input("ingrese el usuario: ")
        self.password = input(" ingrese contraseña: ")

    def conectar(self):
        
        try:
            with connect(
                host="localhost",
                user=self.username,
                password=self.password,
                database="proyecto_nuevo1"
                
            ) as connection:
                print(connection)
                with connection.cursor() as cursor:
                    cursor.execute("insert into usuario (user_name,pass,nombre,apellido,direccion,edad,correo) VALUE ('root','123qwe','fernando','castro','rosario',27,'scastrof@');")
                    connection.commit()
                    
        except Error as e:
            print(e)
db=DataBase()
db.conectar()
