from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        try:
            aux= connect(
                host='localhost',
                user='root',
                password=getpass("ingrese la contraseña"),
                database="proyecto1casa"
                
            ) 
            print("correcto..")
            self.connection=aux
                    
        except Error as e:
            print( 'error'+str(e))

    def insert(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)
    
    def list(self):
        cursor =self.connection.cursor()
        cursor.execute("SELECT * FROM Usuario;")
        resultado=cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.close()

    def close(self):
        self.connection.close()
        print("la conexion fue cerrada...")
DataBase()