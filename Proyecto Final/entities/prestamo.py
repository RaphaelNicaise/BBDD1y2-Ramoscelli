from entities.usuario import Usuario
from entities.libro import Libro
from entities.cuota import Cuota
import datetime as dt

class Prestamo:
    
    DIAS_LIMITE_PRESTAMO = 14
    
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
    def obtener_prestamo_por_id(cls, db, id_prestamo):
        query = "SELECT * FROM prestamos WHERE id = %s"
        db.cursor.execute(query, (id_prestamo,))
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

    
    @staticmethod
    def devolver_prestamo(db, id_prestamo)->bool:
        """
        _summary_

        Args:
            db (_type_): _description_
            id_prestamo (_type_): _description_

        Returns:
            _type_: _description_
        """
        query = "select * from prestamos where id = %s"
        db.cursor.execute(query, (id_prestamo,))
        result = db.cursor.fetchone()
        
        if result is None:
            print('No se encontro el prestamo')
            return False
        
        if result['fecha_devolucion'] is not None:
            print('El prestamo ya fue devuelto')
            return False
        
        query = "UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s"
        db.cursor.execute(query, (dt.date.today(), id_prestamo))
        db.conn.commit()
        
        prestamo = Prestamo.obtener_prestamo_por_id(db, id_prestamo)
        
        query = "SELECT calcular_multa(%s, %s, %s, %s) as multa" # Uso de funcion desde sql
        db.cursor.execute(query, (prestamo.fecha_prestamo, prestamo.fecha_devolucion, Prestamo.DIAS_LIMITE_PRESTAMO, Cuota.MONTO_CUOTA))
        
        multa = db.cursor.fetchone()['multa']
        
        if multa > 0:
            print(f'El usuario debe pagar una multa de ${multa}')
        
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
    def obtener_lista_prestamos_menu(cls,db):
        query = """
        SELECT * FROM prestamos ORDER BY fecha_prestamo
        """
        db.cursor.execute(query)
        prestamos = db.cursor.fetchall()
        print("ID | DNI USUARIO | LID | FECHA PRESTAMO | FECHA DEVOLUCION")
        for prestamo_dict in prestamos:
            prestamo = Prestamo.fromDict(prestamo_dict)
            print(f"{prestamo_dict['id']} {prestamo}")
    
    @classmethod
    def devolver_prestamo_menu(cls, db):
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
        
        if cls.devolver_prestamo(db, id_prestamo):
            print('Prestamo devuelto')
        
        
    
if __name__ == '__main__':
    pass