from entities.usuario import Usuario
from entities.libro import Libro
import datetime as dt

class Prestamo:
    
    DIAS_PRESTAMO = 30
    
    def __init__(self,usuario:str, libro:int,fecha_prestamo:dt.date= None, fecha_devolucion:dt.date= None):
        """_summary_

        Args:
            usuario (str): dni del usuario
            libro (str):  lid del libro
            fecha_prestamo (dt.date, optional): dt.date(yyyy,mm,dd). Como defecto se pone la fecha de prestamo
            fecha_devolucion (dt.date, optional): dt.date(yyyy,mm,dd). Como defecto se pone la fecha de prestamo + 30 dias
        """
        
        #TODO Comprobar que el usuario y el libro existen desde la app.py, porque no tenemos database aca
        self.__dni_usuario = usuario
            

        self.__lid = libro    
        
        
        self.fecha_prestamo = fecha_prestamo or dt.date.today()
        self.fecha_devolucion = fecha_devolucion or self.fecha_prestamo + dt.timedelta(days=Prestamo.DIAS_PRESTAMO)
        
    def __str__(self): 
        return f'Prestamo: {self.dni_usuario} - {self.lid} - {self.fecha_prestamo} - {self.fecha_devolucion}'
    
    @property
    def dni_usuario(self):
        return self.__dni_usuario
    
    @property
    def lid(self):
        return self.__lid
    
    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo
    
    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion
    
    @dni_usuario.setter
    def dni_usuario(self, dni):
        self.__dni_usuario = dni
        
    @lid.setter
    def lid(self, lid):
        self.__lid = lid
        
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha):
        self.__fecha_prestamo = fecha
        
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha):
        self.__fecha_devolucion = fecha    

    @classmethod
    def crear_prestamo(cls, db, usuario, libro):
        """

        Args:
            db (_type_): _description_
            usuario (_type_): objeto Usuario o dni del usuario
            libro (_type_): objeto Libro o lid del libro

        Returns:
            _type_: _description_
        """
        try:
            
            instanciaPrestamo = cls(usuario, libro)
        
            db.cursor.callproc('insertar_prestamo',(instanciaPrestamo.dni_usuario, instanciaPrestamo.lid, instanciaPrestamo.fecha_prestamo, instanciaPrestamo.fecha_devolucion))
            db.conn.commit()
            
        except ValueError as e:
            print(f'Error al crear prestamo: {e}')
            
        return instanciaPrestamo      
      
    @classmethod
    def obtener_prestamo(cls, db, id_prestamo):
        
        query = "SELECT * FROM prestamos WHERE id = %s"
        db.cursor.execute(query, (id_prestamo,))
        result = db.cursor.fetchone()
        
        if not result:
            return None
        
        return cls(result['dni_usuario'], result['lid'], result['fecha_prestamo'], result['fecha_devolucion'])
    
    
    
    
    