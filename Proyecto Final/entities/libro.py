import datetime as dt
import msvcrt
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
        self.__genero = genero
        
    def __str__(self):
        return f"{self.lid} {self.titulo}({self.genero}): {self.autor} Editorial: {self.editorial} {self.anio_publicacion}"  
    
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
        if len(titulo) > 200 or titulo in ('',' '):
            raise ValueError("Titulo invalido")
    
    @staticmethod
    def validar_autor(autor)->bool:
        if len(autor) > 100 or autor in ('',' '):
            raise ValueError("Autor invalido")
    
    @staticmethod
    def validar_genero(genero)->bool:
        if len(genero) > 50 or genero in ('',' '):
            raise ValueError("Genero invalido")
    
    @staticmethod
    def validar_editorial(editorial)->bool:
        if len(editorial) > 100 or editorial in ('',' '):
            raise ValueError("Editorial invalido")
    
    @staticmethod
    def validar_fecha_publicacion(anio_publicacion)->bool:
        if anio_publicacion < 0 or anio_publicacion > dt.datetime.now().year:
            raise ValueError("Año de publicacion invalido")
    
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
            db.cursor.execute("SELECT lid FROM libros WHERE titulo = %s AND autor = %s", (titulo, autor))
            instanciaLibro.lid = db.cursor.fetchone()['lid']
            
            
        except ValueError as e:
            print(f"Error al crear el libro: {e}")
            return None
        
        return instanciaLibro
    
    
    @classmethod
    def obtener_libro(cls, db, lid)->'Libro':
        """
        Obtiene un libro de la base de datos con el id especificado
        """
        if not cls.existe_libro_id(db, lid):
            print(f"El libro con id {lid} no existe")
            return None
        
        query = """
        SELECT * FROM libros
        WHERE lid = %s
        """
        db.cursor.execute(query, (lid,))
        result = db.cursor.fetchone()
        
        if result:
            return cls(result['titulo'], result['autor'], result['genero'], result['editorial'], result['anio_publicacion'], result['lid'])
        return None
    
    @staticmethod
    def existe_libro(db, titulo, autor=None)->bool:
        """
        Verifica que un libro exista en la base de datos con el titulo y autor especificados
        
        Args:
            titulo (str): Titulo del libro
            autor (str, optional): Autor del libro
        Returns:
            bool: True si el libro existe, False si no
        """
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
    
    @staticmethod
    def existe_libro_id(db, lid)->bool:
        """
        Verifica que un libro exista en la base de datos con el id especificado
        Args:
            lid (str): ID del libro
        Returns:
            bool: True si el libro existe, False si no
            
        """
        query = """
        SELECT 1 FROM libros 
        WHERE lid = %s
        """
        params = (lid,)
        
        db.cursor.execute(query, params)
        result = db.cursor.fetchone()
        
        if not result:
            return False
        
        return True
    
    def actualizar_titulo(self, db, titulo_nuevo):
        try:
            query = """
            UPDATE libros
            SET titulo = %s
            where lid = %s
            """
            
            self.titulo = titulo_nuevo
            db.cursor.execute(query, (titulo_nuevo, self.lid))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al actualizar el titulo del libro: {e}")
    
    def actualizar_autor(self, db, autor_nuevo):
        try:
            query = """
            UPDATE libros
            SET autor = %s
            where lid = %s
            """
            
            self.autor = autor_nuevo
            db.cursor.execute(query, (autor_nuevo, self.lid))
            db.conn.commit()
        
        except ValueError as e:
            print(f"Error al actualizar el autor del libro: {e}")
    
    def actualizar_genero(self, db, genero_nuevo):
        try:
            query = """
            UPDATE libros
            SET genero = %s
            where lid = %s
            """
            
            self.genero = genero_nuevo
            db.cursor.execute(query, (genero_nuevo, self.lid))
            db.conn.commit()
        
        except ValueError as e:
            print(f"Error al actualizar el genero del libro: {e}")
    
    def actualizar_editorial(self, db, editorial_nueva):
        try:
            query = """
            UPDATE libros
            SET editorial = %s
            where lid = %s
            """
            
            self.editorial = editorial_nueva
            db.cursor.execute(query, (editorial_nueva, self.lid))
            db.conn.commit()
        
        except ValueError as e:
            print(f"Error al actualizar la editorial del libro: {e}")
    
    def actualizar_anio_publicacion(self, db, anio_publicacion_nuevo):
        try:
            query = """
            UPDATE libros
            SET anio_publicacion = %s
            where lid = %s
            """
            
            self.anio_publicacion = anio_publicacion_nuevo
            db.cursor.execute(query, (anio_publicacion_nuevo, self.lid))
            db.conn.commit()
        
        except ValueError as e:
            print(f"Error al actualizar el año de publicacion del libro: {e}")
    
    def eliminar_libro(self, db):
        # TODO CAMBIAR A CLASSMETHOD, QUE SE ELIMINE POR ID
        try:
            query = """
            DELETE FROM libros
            WHERE lid = %s
            """
            db.cursor.execute(query, (self.lid,))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al eliminar el libro: {e}")    
    
    
    # METODOS PARA EL MENU DE LA APP
    
    @classmethod
    def crear_libro_menu(cls,db):
        print("--- Ingresar datos del libro ---")
        while True:
            try:
                titulo = input("Ingrese el titulo del libro: ")
                Libro.validar_titulo(titulo)
                autor = input("Ingrese el autor del libro: ")
                Libro.validar_autor(autor)
                genero = input("Ingrese el genero del libro (opcional): ")
                Libro.validar_genero(genero)
                editorial = input("Ingrese la editorial del libro: ")
                Libro.validar_editorial(editorial)
                anio_publicacion = int(input("Ingrese el año de publicacion del libro: "))
                Libro.validar_fecha_publicacion(anio_publicacion)
                
                break
            
            except ValueError as e:
                print(f"Error al ingresar los datos del libro: {e}")

        instanciaLibro = cls.crear_libro(db, titulo, autor, genero, editorial, anio_publicacion)
        print(instanciaLibro)
        
    @classmethod
    def obtener_libro_menu(cls, db):
        print("--- Buscar libro ---")
        while True:
            try:
                lid = int(input("Ingrese el ID del libro: "))
                break
            except ValueError:
                print("ID invalido")
        
        
        instanciaLibro = cls.obtener_libro(db, lid)
        
        if instanciaLibro is not None:
            print(instanciaLibro)
            
        return instanciaLibro
    
    @staticmethod
    def listar_libros_menu(db):
        query = """
        SELECT * FROM libros
        """
        db.cursor.execute(query)
        lista_libros = db.cursor.fetchall()
        for libro in lista_libros:
            print(f"{libro['lid']} {libro['titulo']}({libro['genero']}): {libro['autor']} Editorial: {libro['editorial']} {libro['anio_publicacion']}")
            
    @classmethod
    def actualizar_titulo_menu(cls,db):
        print("--- Actualizar titulo ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        
        if instanciaLibro is not None:
            while True:
                try:
                    titulo_nuevo = input("Ingrese el nuevo titulo del libro: ")
                    instanciaLibro.actualizar_titulo(db, titulo_nuevo)
                    break
                except ValueError as e:
                    print(f"Error al actualizar el titulo: {e}")
    
    @classmethod
    def actualizar_autor_menu(cls,db):
        print("--- Actualizar autor ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        
        if instanciaLibro is not None:
            while True:
                try:
                    autor_nuevo = input("Ingrese el nuevo autor del libro: ")
                    instanciaLibro.actualizar_autor(db, autor_nuevo)
                    break
                except ValueError as e:
                    print(f"Error al actualizar el autor: {e}")
    
    @classmethod          
    def actualizar_genero_menu(cls,db):
        print("--- Actualizar genero ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        
        if instanciaLibro is not None:
            while True:
                try:
                    genero_nuevo = input("Ingrese el nuevo genero del libro: ")
                    instanciaLibro.actualizar_genero(db, genero_nuevo)
                    break
                except ValueError as e:
                    print(f"Error al actualizar el genero: {e}")
                    
    @classmethod                
    def actualizar_editorial_menu(cls,db):
        print("--- Actualizar editorial ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        
        if instanciaLibro is not None:
            while True:
                try:
                    editorial_nueva = input("Ingrese la nueva editorial del libro: ")
                    instanciaLibro.actualizar_editorial(db, editorial_nueva)
                    break
                except ValueError as e:
                    print(f"Error al actualizar la editorial: {e}")
    
    @classmethod     
    def actualizar_año_publicacion_menu(cls,db):
        print("--- Actualizar año de publicacion ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        
        if instanciaLibro is not None:
            while True:
                try:
                    anio_publicacion_nuevo = int(input("Ingrese el nuevo año de publicacion del libro: "))
                    instanciaLibro.actualizar_anio_publicacion(db, anio_publicacion_nuevo)
                    break
                except ValueError as e:
                    print(f"Error al actualizar el año de publicacion: {e}")
    
    @classmethod
    def eliminar_libro_menu(cls, db):
        print("--- Eliminar libro ---")
          
        instanciaLibro = cls.obtener_libro_menu(db)
        if instanciaLibro is None:
            return
        
        while True:
            confirmacion = input("Estas seguro que deseas eliminar el libro? (Y/N)")
            if confirmacion.lower() in ('y','n'):
                break
            else:
                print("Opcion invalida")
        
        if confirmacion.lower() == 'n':
            return
        
        instanciaLibro.eliminar_libro(db)
        print("Libro eliminado")
        
        