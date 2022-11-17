from getpass import getpass


class DataBase:
    def __init__(self,user,password):
        self.user=user
        self.password=password
    
    def conectar(self):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database="proyecto_nuevo1"

            ) as connection