from entities.usuario import Usuario
from entities.libro import Libro
import datetime as dt

class Prestamo:
    
    DIAS_LIMITE_PRESTAMO = 30
    
    def __init__(self,usuario:str, libro:int,fecha_prestamo:dt.date= None, fecha_devolucion:dt.date= None):
        """

        Args:
            usuario (str): dni del usuario
            libro (str):  lid del libro
            fecha_prestamo (dt.date, optional): dt.date(yyyy,mm,dd). Como defecto se pone la fecha de prestamo
            fecha_devolucion (dt.date, optional): dt.date(yyyy,mm,dd). Como defecto se pone None
        """
        
        #TODO Comprobar que el usuario y el libro existen desde la app.py, porque no tenemos database aca
        self.__dni_usuario = usuario
            

        self.__lid = libro    
        
        
        self.__fecha_prestamo = fecha_prestamo or dt.date.today()
        self.__fecha_devolucion = fecha_devolucion
        
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
    
    @classmethod
    def existe_prestamo(cls, db, id_prestamo):
        query = "SELECT * FROM prestamos WHERE id = %s"
        db.cursor.execute(query, (id_prestamo,))
        result = db.cursor.fetchone()
        
        return result is not None

    
    
    def devolver_prestamo(self, db):
        """
        _summary_

        Args:
            db (_type_): _description_
            id_prestamo (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.fecha_devolucion = dt.date.today()
        
    
    @classmethod
    def calcular_multa(cls, db, id_prestamo):
        """
        _summary_

        Args:
            db (_type_): _description_
            id_prestamo (_type_): _description_

        Returns:
            _type_: _description_
        """
        query = """
        SELECT fecha_devolucion FROM prestamos WHERE id = %s
        """
        db.cursor.execute(query, (id_prestamo,))
        prestamo = db.cursor.fetchone()
        
        if not cls.existe_prestamo(db, id_prestamo):
            raise ValueError('El prestamo no existe')
        
        if prestamo['fecha_devolucion'] is None or prestamo['fecha_devolucion'] > dt.date.today():
            raise ValueError('El libro no ha sido devuelto o la fecha de devolucion es mayor a la fecha actual')
        
        fecha_devolucion = prestamo['fecha_devolucion']
        fecha_prestamo = prestamo['fecha_prestamo']
        
        dias_diferencia = (fecha_devolucion - fecha_prestamo).days
        
        
    #
    
    @classmethod
    def crear_prestamo_menu(cls, db):
        """
        _summary_

        Args:
            db (_type_): _description_

        Returns:
            _type_: _description_
        """
        
    
    @classmethod
    def obtener_prestamo_menu(cls, db):
        """
        _summary_

        Args:
            db (_type_): _description_

        Returns:
            _type_: _description_
        """
        pass
    
    @classmethod
    def calcular_multa_menu(cls, db):
        """
        _summary_

        Args:
            db (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            id_prestamo = int(input('Ingrese el id del prestamo: '))
        except ValueError:
            print('El id ingresado no es valido')
            return
        
        multa = cls.calcular_multa(db, id_prestamo)
        print(f'La multa a pagar es de ${multa}')
        
    @classmethod
    def obtener_lista_prestamos_menu(db):
        query = """
        SELECT * FROM prestamos
        """
        db.cursor.execute(query)
        prestamos = db.cursor.fetchall()
        print(prestamos)
    
    
    
if __name__ == '__main__':
    pass