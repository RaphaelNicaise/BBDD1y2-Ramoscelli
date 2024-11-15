import datetime as dt

class Usuario:
    def __init__(self, dni:str, nombre:str, apellido: str, email:str, telefono:str,fecha_registro:dt.datetime=dt.datetime.now().strftime('%Y-%m-%d')):
        """_summary_

        Args:
            dni (str): _description_
            nombre (str): _description_
            apellido (str): _description_
            email (str): _description_
            telefono (str): _description_
            fecha_registro (dt.datetime, optional): formato YYYY-MM-DD.
        """
        
        self.validar_dni(dni)
        self.validar_nombre(nombre)
        self.validar_apellido(apellido)
        self.validar_email(email)
        self.validar_telefono(telefono)
        self.validar_fecha_registro(fecha_registro)
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__fecha_registro = fecha_registro
    
    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido} - {self.email} - {self.telefono} - {self.fecha_registro}"
    
    def __eq__(self, otroUsuario):
        return self.dni == otroUsuario.dni
    
    # Getters
    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def fecha_registro(self):
        return self.__fecha_registro
    
    # Setters con validacion de datos
    @nombre.setter
    def nombre(self, nombre):
        self.validar_nombre(nombre)
        self.__nombre = nombre
        
    @apellido.setter
    def apellido(self, apellido):
        self.validar_apellido(apellido)
        self.__apellido = apellido
        
    @email.setter
    def email(self, email):
        self.validar_email(email)
        self.__email = email
        
    @telefono.setter
    def telefono(self, telefono):
        self.validar_telefono(telefono)
        self.__telefono = telefono
    
    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self.validar_fecha_registro(fecha_registro)
        self.__fecha_registro = fecha_registro
    
    # METODOS DE VALIDACION DE DATOS
    @staticmethod
    def validar_dni(dni):
        if len(dni) > 20 or dni in ['',' ']:
            raise ValueError("DNI invalido")
        
    @staticmethod
    def validar_nombre(nombre):
        if len(nombre) > 50 or nombre in ['',' '] or not nombre.isalpha():
            raise ValueError("Nombre invalido")
        
    @staticmethod
    def validar_apellido(apellido):
        if len(apellido) > 50 or apellido in ['',' '] or not apellido.isalpha():
            raise ValueError("Apellido invalido")
        
    @staticmethod
    def validar_email(email):
        if len(email) > 100 or email in ['',' '] or not '@' in email:
            raise ValueError("Email invalido")
        
    @staticmethod
    def validar_telefono(telefono):
        if len(telefono) > 15 or telefono in ['',' '] or not telefono.isdigit():
            raise ValueError("Telefono invalido") 
        
    @staticmethod
    def validar_fecha_registro(fecha_registro):
        # Validar que la fecha_Registro sea de este formato YYYY-MM-DD
        if isinstance(fecha_registro, dt.date):
            fecha_registro = fecha_registro.strftime('%Y-%m-%d')
        
        try:
        # Intentar convertir la cadena a un objeto datetime con el formato 'YYYY-MM-DD'
            dt.datetime.strptime(fecha_registro, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Fecha de registro inválida, debe estar en el formato YYYY-MM-DD")
    
    @classmethod
    def crear_usuario(cls, db, dni, nombre, apellido, email, telefono)->'Usuario':
        """
        Crear un nuevo objeto usuario e insertarlo en la base de datos, mediante un procedimiento almacenado
        
        Args:
            db (Database): Conexion a la base de datos
            dni (str): DNI del usuario
            nombre (str): Nombre del usuario
            apellido (str): Apellido del usuario
            email (str): Email del usuario
            telefono (str): Telefono del usuario
        Returns: Retorna un objeto Usuario
        """
        
        
        if cls.existe_usuario(db, dni):
            print(f"Usuario con DNI {dni} ya existe.")
            return None

        try:
            instanciaUsuario = cls(dni, nombre, apellido, email, telefono) # Creamos el objeto y que valide los datos
            # USO DE PROCEDIMIENTOS ALMACENADO insertar_usuario
            db.cursor.callproc('insertar_usuario', (dni, nombre, apellido, email, telefono)) # Insertamos el usuario
            db.conn.commit()

            
        except ValueError as e:
            print(f"Error al crear el usuario: {e}")
            return None
        
        return instanciaUsuario # Retornamos el objeto creado
    
    @classmethod
    def obtener_usuario(cls, db, dni)->'Usuario':
        """
        Obtener un usuario de la base de datos a partir de su DNI
        Args:
            db (Database): Conexion a la base de datos
            dni (str): DNI del usuario
        Returns: Retorna un objeto Usuario si lo encuentra, sino None
        """
        
        if not cls.existe_usuario(db, dni):
            print(f"Usuario con DNI {dni} no existe.")
            return None
        
        query ="""
            SELECT * FROM Usuarios
            WHERE dni = %s
            """
        db.cursor.execute(query, (dni,))
        result = db.cursor.fetchone()
    
        
        if result:
            return cls(result['dni'], result['nombre'], result['apellido'], result['email'], result['telefono'],result['fecha_registro'])
        return None
    
    
    def eliminar_usuario(self,db):
        """
        Eliminar un usuario de la base de datos
        Args:
            db (Database): Conexion a la base de datos
            dni (str): DNI del usuario
        """
        
        if not Usuario.existe_usuario(db, self.dni):
            print(f"Usuario con DNI {self.dni} no existe.")
            return
        
        query = """
        DELETE FROM Usuarios
        WHERE dni = %s
        """
        
        db.cursor.execute(query, (self.dni,))
        db.conn.commit()
    
    @staticmethod
    def existe_usuario(db, dni)->bool:
        """
        Verifica si un usuario existe en la base de datos
        Args:
            db (Database): Conexion a la base de datos
            dni (str): DNI del usuario
        Returns: Retorna True si el usuario existe, False en caso contrario
        """
        query = """
        SELECT 1 FROM Usuarios
        WHERE dni = %s
        """
        db.cursor.execute(query, (dni,))
        result = db.cursor.fetchone()
        
        if result is None:
            return False
        
        return True
                       
    def actualizar_nombre(self, db, nombre_nuevo):
        """ Actualizar nombre de usuario """
        
        try:
            query = """
            UPDATE Usuarios
            SET nombre = %s
            WHERE dni = %s
            """
            
            self.nombre = nombre_nuevo
            db.cursor.execute(query, (nombre_nuevo, self.dni))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al actualizar el nombre: {e}")
        
    def actualizar_apellido(self, db, apellido_nuevo):
        """ Actualizar apellido de usuario """
        try:
            query = """
            UPDATE Usuarios
            SET apellido = %s
            WHERE dni = %s
            """
            
            self.apellido = apellido_nuevo
            db.cursor.execute(query, (apellido_nuevo, self.dni))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al actualizar el apellido: {e}")
    
    def actualizar_telefono(self, db, telefono_nuevo):
        """ Actualizar telefono de usuario """
        try:
            query = """
            UPDATE Usuarios
            SET telefono= %s
            WHERE dni = %s
            """
            self.telefono = telefono_nuevo
            db.cursor.execute(query, (telefono_nuevo, self.dni))
            db.conn.commit()
            
        except ValueError as e:
            
            print(f"Error al actualizar el telefono: {e}")

    def actualizar_email(self, db, email_nuevo):
        """"
        Actualizar email de usuario
        Args:
            db (Database): Conexion a la base de datos
            email_nuevo (str): Nuevo email del usuario
            
        """
        try:
            query = """
            UPDATE Usuarios
            SET email = %s
            WHERE dni = %s
            """
            self.email = email_nuevo
            db.cursor.execute(query, (email_nuevo, self.dni))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al actualizar el email: {e}")
    
    def actualizar_fecha_registro(self, db, fecha_registro_nueva):
        """"
        Actualizar fecha de registro de usuario
        Args:
            db (Database): Conexion a la base de datos
            fecha_registro_nueva (str): Nueva fecha de registro del usuario
            
        """
        try:
            query = """
            UPDATE Usuarios
            SET fecha_registro = %s
            WHERE dni = %s
            """
            self.fecha_registro = fecha_registro_nueva
            db.cursor.execute(query, (fecha_registro_nueva, self.dni))
            db.conn.commit()
            
        except ValueError as e:
            print(f"Error al actualizar la fecha de registro: {e}")
    
    
    @classmethod
    def crear_usuario_menu(cls,db):
        print("--- Ingresar datos del usuario ---")
        while True:
            try:
                dni = input("Ingrese DNI: ")
                cls.validar_dni(dni)
                if cls.existe_usuario(db, dni):
                    raise ValueError(f"DNI:{dni} ya existe")
                nombre = input("Ingrese Nombre: ")
                cls.validar_nombre(nombre)
                apellido = input("Ingrese Apellido: ")
                cls.validar_apellido(apellido)
                email = input("Ingrese Email: ")
                cls.validar_email(email)
                telefono = input("Ingrese Telefono: ")
                cls.validar_telefono(telefono)
                
                break
            
            except ValueError as e:
                print(f"Error al ingresar datos del usuario: {e}")
                
        instanciaUsuario = cls.crear_usuario(db, dni, nombre, apellido, email, telefono)
        if instanciaUsuario is not None:
            print(instanciaUsuario)
        
                    
                    
    @classmethod
    def obtener_usuario_menu(cls,db):
        while True:
            try:
                dni = input("Ingrese DNI: ")
                Usuario.validar_dni(dni)
                break
            except ValueError as e:
                print(f"Error al ingresar DNI: {e}")
                
        instanciaUsuario = cls.obtener_usuario(db, dni)
        
        if instanciaUsuario is not None:
            print(instanciaUsuario)
            
        return instanciaUsuario
        

    @classmethod
    def actualizar_nombre_menu(cls,db):
        print("--- Actualizar nombre ---")
        
        instanciaUsuario = cls.obtener_usuario_menu(db)
        # 53242345
        if instanciaUsuario is not None:
            while True:
                try:
                    nombre_nuevo = input("Ingrese nuevo nombre: ")
                    instanciaUsuario.actualizar_nombre(db, nombre_nuevo)
                    
                    break
                
                except ValueError as e:
                    print(f"Error al ingresar nuevo nombre: {e}")

        print(instanciaUsuario)
        
    @classmethod
    def actualizar_apellido_menu(cls,db):
        print("--- Actualizar apellido ---")
        
        instanciaUsuario = cls.obtener_usuario_menu(db)
        if instanciaUsuario is not None:
            while True:
                try:
                    apellido_nuevo = input("Ingrese nuevo apellido: ")
                    instanciaUsuario.actualizar_apellido(db, apellido_nuevo)
                    
                    break
                
                except ValueError as e:
                    print(f"Error al ingresar nuevo apellido: {e}")
        print(instanciaUsuario)
    
    @classmethod
    def actualizar_email_menu(cls,db):
        print("--- Actualizar email ---")
        
        instanciaUsuario = cls.obtener_usuario_menu(db)
        if instanciaUsuario is not None:
            while True:
                try:
                    email_nuevo = input("Ingrese nuevo email: ")
                    instanciaUsuario.actualizar_email(db, email_nuevo)
                    
                    break
                
                except ValueError as e:
                    print(f"Error al ingresar nuevo email: {e}")
        print(instanciaUsuario)

    @classmethod
    def actualizar_telefono_menu(cls,db):
        print("--- Actualizar telefono ---")
        
        instanciaUsuario = cls.obtener_usuario_menu(db)
        if instanciaUsuario is not None:
            while True:
                try:
                    telefono_nuevo = input("Ingrese nuevo telefono: ")
                    instanciaUsuario.actualizar_telefono(db, telefono_nuevo)
                    
                    break
                
                except ValueError as e:
                    print(f"Error al ingresar nuevo telefono: {e}")
        print(instanciaUsuario)
        
    @classmethod
    def eliminar_usuario_menu(cls,db):
        print("--- Eliminar usuario ---")
        
        instanciaUsuario = cls.obtener_usuario_menu(db)
        if instanciaUsuario is None:
            return
        
        while True:
            confirmacion = input("Estas seguro que deseas eliminar el usuario? (Y/N): ").lower()
            if confirmacion.lower() in ['y','n']:
                break
            else:
                print("Opcion invalida")
                
        if confirmacion.lower() == 'n':
            return
        
        instanciaUsuario.eliminar_usuario(db)
        print("Usuario eliminado")
        
    @staticmethod
    def listar_usuarios_menu(db):
        query = """
        SELECT * FROM Usuarios
        """
        db.cursor.execute(query)
        lista_usuarios = db.cursor.fetchall()
        
        for usuario in lista_usuarios:
            print(f"{usuario['dni']} {usuario['nombre']} {usuario['apellido']}, {usuario['email']} - {usuario['telefono']} - {usuario['fecha_registro']}")
            
    @staticmethod
    def buscar_usuario_filtrado_menu(db):
        filtro = input("Ingrese una busqueda: ").lower()
        query = f"""
        SELECT * FROM usuarios
        WHERE LOWER(dni) LIKE '%{filtro}%' OR LOWER(nombre) LIKE '%{filtro}%' OR LOWER(apellido) LIKE '%{filtro}%' OR LOWER(email) LIKE '%{filtro}%' OR LOWER(telefono) LIKE '%{filtro}%'
        """

        db.cursor.execute(query)
        usuarios = db.cursor.fetchall()
    
        if usuarios == []:
            print("No se encontraron libros")
            return
        
        for usuario in usuarios:
            print(f"{usuario['dni']} {usuario['nombre']} {usuario['apellido']}, {usuario['email']} - {usuario['telefono']} - {usuario['fecha_registro']}")