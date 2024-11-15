from entities.usuario import Usuario

class Cuota:
    def __init__(self,dni_usuario:str, monto:float ,mes:int ,anio:int, estado_pago:str=None, id_cuota:int=None):
        
        self.validar_monto(monto)
        self.validar_mes(mes)
        self.validar_anio(anio)
        
        if estado_pago is not None:
            self.validar_estado(estado_pago)
        
        self.__dni_usuario = dni_usuario
        self.__monto = monto
        self.__mes = mes
        self.__anio = anio
        self.__estado_pago = estado_pago
        self.__id_cuota = id_cuota
    
    
    def __str__(self):
        return f'Cuota: {self.__id_cuota} - DNI Usuario: {self.__dni_usuario} - Monto: {self.__monto} - Mes: {self.__mes} - Año: {self.__anio} - Estado de Pago: {self.__estado_pago}'
    
    # Getters    
    @property
    def dni_usuario(self):
        return self.__dni_usuario
    
    @property
    def monto(self):
        return self.__monto
    
    @property
    def mes(self):
        return self.__mes
    
    @property
    def anio(self):
        return self.__anio
    
    @property
    def estado_pago(self):
        return self.__estado_pago
    
    @property
    def id_cuota(self):
        return self.__id_cuota
    
    # Setters
    
    @monto.setter
    def monto(self,monto:float):
        self.validar_monto(monto)
        self.__monto = monto
        
    @mes.setter
    def mes(self,mes:int):
        self.validar_mes(mes)
        self.__mes = mes
        
    @anio.setter
    def anio(self,anio:int):
        self.validar_anio(anio)
        self.__anio = anio
        
    @estado_pago.setter
    def estado_pago(self,estado:str):
        self.validar_estado(estado) 
        self.__estado_pago = estado
        
    @id_cuota.setter
    def id_cuota(self,id_cuota:int):
        self.__id_cuota = id_cuota
    # Validaciones
    
    @staticmethod
    def validar_monto(monto:float):
        if not isinstance(monto,float) and not isinstance(monto,int):
            raise ValueError('El monto de la cuota debe ser un valor numérico')
        
        if monto <= 0:
            raise ValueError('El monto de la cuota debe ser mayor a 0')
    
    @staticmethod
    def validar_mes(mes:int):
        if not isinstance(mes,int):
            raise ValueError('El mes de la cuota debe ser un valor entero')
        if mes < 1 or mes > 12:
            raise ValueError('El mes de la cuota debe ser un valor entre 1 y 12')
        
    @staticmethod
    def validar_anio(anio:int):
        if not isinstance(anio,int):
            raise ValueError('El año de la cuota debe ser un valor entero')
        if anio < 1900:
            raise ValueError('El año de la cuota debe ser mayor a 1900')
    
    @staticmethod
    def validar_estado(estado:str):
        if estado not in ['PENDIENTE','PAGADO']:
            raise  ValueError('El estado de la cuota debe ser PENDIENTE o PAGADO')
        
    @classmethod
    def crear_cuota(cls,db,dni_usuario:str, monto:float ,mes:int ,anio:int, estado_pago:str='PENDIENTE'):
        
        if cls.existe_cuota(db,dni_usuario,mes,anio):
            raise ValueError('Ya existe una cuota registrada para el mes y año indicados')
        
        instanciaCuota = cls(dni_usuario, monto, mes, anio)
        
        db.cursor.callproc('insertar_cuota',(dni_usuario, monto, mes, anio))
        db.conn.commit()
         
        db.cursor.execute("SELECT id FROM cuotas WHERE dni_usuario = %s AND mes = %s AND anio = %s",(dni_usuario,mes,anio))   

        instanciaCuota.id_cuota = db.cursor.fetchone()['id']
        return instanciaCuota
    
    @classmethod
    def existe_cuota(cls,db,id_usuario,mes,anio)->bool:
        query = """
        SELECT 1 FROM cuotas WHERE dni_usuario = %s AND mes = %s AND anio = %s
        """
        
        db.cursor.execute(query,(id_usuario,mes,anio))
        return db.cursor.fetchone() is not None
        
    
    @classmethod
    def registrar_pago_cuota(cls,db,id_usuario,mes,anio):
        query = 'UPDATE cuotas SET estado_pago = "PAGADO" WHERE dni_usuario = %s AND mes = %s AND anio = %s'
        db.cursor.execute(query,(id_usuario,mes,anio))
        db.conn.commit()
        
    @classmethod
    def obtener_cuota(cls,db,id_usuario,mes,anio):
        query = 'SELECT * FROM cuotas WHERE dni_usuario = %s AND mes = %s AND anio = %s'
        db.cursor.execute(query,(id_usuario,mes,anio))
        result = db.cursor.fetchone()
        print(result)
    
    # MENU
    
    @classmethod 
    def crear_cuota_menu(cls,db):
        
        print('--- Crear Cuota ---')
        while True:
            try:
                dni_usuario = input('Ingrese el DNI del usuario: ')
                # Verificamos si el usuario existe en la base de datos
                if not Usuario.existe_usuario(db, dni_usuario):
                    print("El usuario con el DNI ingresado no existe.")
                    continue  # Volver a pedir el DNI
                
                # Pedimos el monto y lo validamos
                monto = float(input('Ingrese el monto de la cuota: '))
                cls.validar_monto(monto)
                
                # Pedimos el mes y lo validamos
                mes = int(input('Ingrese el mes de la cuota: '))
                cls.validar_mes(mes)
                
                # Pedimos el año y lo validamos
                anio = int(input('Ingrese el año de la cuota: '))
                cls.validar_anio(anio)

                # Crear la cuota y registrarla en la base de datos
                instanciaCuota = cls.crear_cuota(db, dni_usuario, monto, mes, anio)
                print("Cuota creada exitosamente:", instanciaCuota)
                break  # Salimos del bucle si todo fue correcto
            
            except ValueError as e:
                print(f"Hubo un error al crear la cuota: {e}")
        
    @classmethod
    def obtener_cuota_menu(cls,db):
        pass
    
    @classmethod
    def registrar_pago_cuota_menu(cls,db):
        pass
    
    
        