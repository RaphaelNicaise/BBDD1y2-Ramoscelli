import mysql.connector

class Database:
    def __init__(self):
        try:
            # CAMBIAR LAS CREDENCIALES DE ACUERDO A SU CONFIGURACIÓN
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="1234",
                database="biblioteca", # NO MODIFICAR
                port=3306,
                )
           
            
            self.cursor = self.conn.cursor(dictionary=True)  
        
        except Exception as e:
            raise Exception("Error en la conexión a la base de datos")
        
        
    def close(self):
        self.cursor.close()
        self.conn.close()