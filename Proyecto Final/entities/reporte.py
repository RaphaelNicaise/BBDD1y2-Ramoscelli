class Reporte:
    
    @staticmethod
    def reporte_promedio_meses(db):
        query = """
        SELECT AVG(meses) as 'valor' FROM (
            SELECT COUNT(*) as meses
            FROM cuotas
            WHERE estado_pago = 'PENDIENTE'
            GROUP BY dni_usuario) as meses
        """
        db.cursor.execute(query)
        meses = db.cursor.fetchone()
        print(f"- El promedio de meses de los socios que no estan al dia con las cuotas es: {meses['valor']:.1f}")
        
    @staticmethod
    def reporte_cantidad_cuotas(db):
        query = """
        SELECT COUNT(*) as 'cantidad' ,sum(monto) as 'monto'
        FROM cuotas
        WHERE estado_pago = 'PENDIENTE'
        """
        db.cursor.execute(query)
        resultado = db.cursor.fetchone()
        print(f"- La cantidad de cuotas pendientes es: {resultado['cantidad']} con un valor total de ${resultado['monto']:.2f}")
        
    @staticmethod
    def reporte_socios_con_cuotas_pendientes(db):
        query = """
        SELECT us.dni, concat(us.nombre, ' ', us.apellido) as 'usuario', COUNT(c.id) as 'cuotas_pendientes'
        FROM usuarios us
        INNER JOIN cuotas c ON us.dni = c.dni_usuario
        WHERE c.estado_pago = 'PENDIENTE'
        GROUP BY us.dni, 'usuario'
        ORDER BY cuotas_pendientes DESC
        """
        db.cursor.execute(query)
        resultados = db.cursor.fetchall()
        print("- Socios con cuotas pendientes:")
        for resultado in resultados:
            print(f" {resultado['dni']} {resultado['usuario']} debe -> {resultado['cuotas_pendientes']}")