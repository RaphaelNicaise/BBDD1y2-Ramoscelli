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
        
        self.__fecha_prestamo = fecha_prestamo if fecha_prestamo is not None else dt.date.today()
        self.__fecha_devolucion = fecha_devolucion
        
    def __str__(self): 
        return f'{self.dni_usuario} - {self.lid} - {self.fecha_prestamo} - {self.fecha_devolucion if self.fecha_devolucion is not None else "No devuelto"}'
    
    @classmethod
    def fromDict(cls, dict):
        return cls(dict['dni_usuario'], dict['lid'], dict['fecha_prestamo'], dict['fecha_devolucion'])
    
    def toDict(self):
        return {
            'dni_usuario': self.dni_usuario,
            'lid': self.lid,
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion
        }
    
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
        
            db.cursor.callproc('insertar_prestamo',(instanciaPrestamo.dni_usuario, instanciaPrestamo.lid, instanciaPrestamo.fecha_prestamo))
            db.conn.commit()
            
        except ValueError as e:
            print(f'Error al crear prestamo: {e}')
            
        return instanciaPrestamo      
      
    @classmethod
    def obtener_prestamo(cls, db, dni_usuario, lid):
        
        query = "SELECT * FROM prestamos WHERE dni_usuario = %s AND lid = %s"
        db.cursor.execute(query, (dni_usuario,lid))
        result = db.cursor.fetchone()
        
        if not result:
            return None
        
        return cls(result['dni_usuario'], result['lid'], result['fecha_prestamo'], result['fecha_devolucion'])
    
    @classmethod
    def existe_prestamo(cls, db, dni_usuario, lid):
        query = "SELECT * FROM prestamos WHERE dni_usuario = %s AND lid = %s"
        db.cursor.execute(query, (dni_usuario,lid))
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
        pass
        
    
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
        pass
        
        

    
    @classmethod
    def crear_prestamo_menu(cls, db):
        """
        _summary_

        Args:
            db (_type_): _description_

        Returns:
            _type_: _description_
        """
        usuario = Usuario.obtener_usuario_menu(db)
        libro = Libro.obtener_libro_menu(db)
        
        if cls.existe_prestamo(db, usuario.dni, libro.lid):
            print('El usuario ya tiene un prestamo de ese libro')
            return
        
        prestamo = cls.crear_prestamo(db, usuario.dni, libro.lid)
        print(f'Prestamo creado: {prestamo}')
        
    @classmethod
    def obtener_prestamo_menu(cls, db):
        
        usuario = Usuario.obtener_usuario_menu(db)
        libro = Libro.obtener_libro_menu(db)
        
        prestamo = cls.obtener_prestamo(db, usuario.dni, libro.lid)
        
        if prestamo is None:
            print('No se encontro prestamo')
        else:
            print(f'Prestamo encontrado: {prestamo}')
    
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
    def obtener_lista_prestamos_menu(cls,db):
        query = """
        SELECT * FROM prestamos
        """
        db.cursor.execute(query)
        prestamos = db.cursor.fetchall()
        print("DNI USUARIO | LID | FECHA PRESTAMO | FECHA DEVOLUCION")
        for prestamo_dict in prestamos:
            prestamo = Prestamo.fromDict(prestamo_dict)
            print(prestamo)
    
    
    
if __name__ == '__main__':
    pass