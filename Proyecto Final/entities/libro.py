
class Libro:
    def __init__(self, titulo:str, autor:str, genero:str=None, editorial:str=None, anio_publicacion=None,lid:str=None):
        
        self.validar_titulo(titulo)
        self.validar_autor(autor)
        
        if genero is not None:
            self.validar_genero(genero)
        if editorial is not None:
            self.validar_editorial(editorial)
        if anio_publicacion is not None:
            self.validar_fecha_publicacion(anio_publicacion)
        
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio_publicacion = anio_publicacion
        self.__lid = lid #Libro ID
        
    def __str__(self):
        return f"{self.lid} Libro: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Año de Publicación: {self.anio_publicacion}"  
    
    # Getters
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def editorial(self):
        return self.__editorial
    
    @property
    def anio_publicacion(self):
        return self.__anio_publicacion
    
    @property
    def lid(self):
        return self.__lid
    
    #Setters con validaciones
    @titulo.setter
    def titulo(self, titulo):
        self.validar_titulo(titulo)
        self.__titulo = titulo
        
    @autor.setter
    def autor(self, autor):
        self.validar_autor(autor)
        self.__autor = autor
        
    @genero.setter
    def genero(self, genero):
        self.validar_genero(genero)
        self.__genero = genero
        
    @editorial.setter
    def editorial(self, editorial):
        self.validar_editorial(editorial)
        self.__editorial = editorial
        
    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion):
        self.validar_fecha_publicacion(anio_publicacion)
        self.__anio_publicacion = anio_publicacion
        
    @lid.setter
    def lid(self, lid):
        
        self.__lid = lid
        
    @staticmethod
    def validar_titulo(titulo)->bool:
        pass
    
    @staticmethod
    def validar_autor(autor)->bool:
        pass
    
    @staticmethod
    def validar_genero(genero)->bool:
        pass
    
    @staticmethod
    def validar_editorial(editorial)->bool:
        pass
    
    @staticmethod
    def validar_fecha_publicacion(anio_publicacion)->bool:
        pass
    
    @classmethod
    def crear_libro(cls, db, titulo, autor, genero, editorial, anio_publicacion):
        
        if cls.existe_libro(db, titulo, autor):
            print(f"El libro {titulo} de {autor} ya existe")
            return None
        
        try:
            
            instanciaLibro = cls(titulo, autor, genero, editorial, anio_publicacion)
            db.cursor.callproc("insertar_libro",(titulo, autor, genero, editorial, anio_publicacion))
            db.conn.commit()
            
            # TODO: obtener el id del libro insertado
            db.cursor.execute("SELECT LAST_INSERT_ID()")
            instanciaLibro.lid = db.cursor.fetchone()['lid']
            
            
        except ValueError as e:
            print(f"Error al crear el libro: {e}")
            return None
        
        return instanciaLibro
    
    # TODO: classmethod para obtener un libro que ya existe en la base de datos, osea q tiene un id, por lo tanto lo podria devolver
    
    @staticmethod
    def existe_libro(db, titulo, autor=None)->bool:
        """
        Verifica si un libro ya existe en la base de datos"""
        query = """
        SELECT 1 FROM libros 
        WHERE titulo = %s
        """
        params = (titulo,)
        
        if autor is not None:
            query += " AND autor = %s"
            params += (autor,)
        db.cursor.execute(query, params)
        result = db.cursor.fetchone()
        
        if not result:
            return False
        
        return True 
    
    