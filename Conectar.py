from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        try:
            aux= connect(
                host='localhost',
                user='root',
                password='Nokia2022',
                database="mydb1"
                
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
    
    def list(self,tabla):
        cursor =self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")
        resultado=cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.close()
    
    def modific(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)

    def Eliminar(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)
    def close(self):
        self.connection.close()
        print("la conexion fue cerrada...")
