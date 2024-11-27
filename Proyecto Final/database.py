import mysql.connector

class Database:
    def __init__(self):
        
        self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="1234",
                database="biblioteca",
                port=3306,
                )
            
        self.cursor = self.conn.cursor(dictionary=True)
        
    def close(self):
        self.cursor.close()
        self.conn.close()