from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        try:
            variable=connect(
                host='localhost',
                database='proyecto_nuevo1',
                usuario='root',
                contrasenia=getpass("ingrese su contraseña: ")
            )
        except Error as e:
            print("Error " + e)
        self.variable=variable


    def insert(self,sql):
        variable2=self.variable.cursor()
        variable2.execute(sql)
        self.variable.commit()
        self.close()
    def close(self):
        self.variable.close()
        print("la conexion se ha cerrado...")
db=DataBase()
db.insert(f'')