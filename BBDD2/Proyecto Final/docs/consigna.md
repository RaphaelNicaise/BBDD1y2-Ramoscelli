# Proyecto 4: Sistema de Inventario de Tienda


## Descripción
Sistema para la gestión de inventario en una tienda, incluyendo productos, proveedores y movimientos de stock.

## Requerimientos

- Catálogo de productos con stock actual
- Registro de proveedores y sus productos
- Movimientos de entrada y salida de mercancía
- Alertas de stock bajo

## Estructura de Datos

### Colección: `productos`
```json
{
    _id: ObjectId,
    codigo: "PROD001",
    nombre: "Laptop HP",
    categoria: "Electrónicos",
    precio: 799.99,
    stockActual: 15,
    stockMinimo: 5,
    proveedorId: ObjectId,
    fechaUltimaActualizacion: ISODate
}
```

### Colección: `movimientos`
```json
{
    _id: ObjectId,
    productoId: ObjectId,
    tipo: "entrada", // "entrada" o "salida"
    cantidad: 10,
    motivo: "Compra a proveedor",
    fecha: ISODate,
    usuario: "admin"
}
```

### Colección: `proveedores`
```json
{
    _id: ObjectId,
    nombre: "Distribuidora Tech",
    contacto: "Juan López",
    telefono: "+1234567890",
    email: "ventas@distritech.com",
    productosOfrecidos: ["PROD001", "PROD002"]
}
```

## Funciones a Implementar

- `agregarProducto(producto)` - Añadir producto al catálogo
- `registrarMovimiento(movimiento)` - Registrar entrada/salida de stock
- `consultarStock(codigo)` - Ver stock actual de un producto
- `productosStockBajo()` - Listar productos con stock por debajo del mínimo
- `reporteMovimientos(fechaInicio, fechaFin)` - Reporte de movimientos en período

## Instalación

```bash
pip install pymongo
```

## Criterios de Evaluación

- Correcta implementación de las operaciones CRUD
- Uso apropiado de consultas y agregaciones
- Manejo de errores y validaciones
- Estructura de datos eficiente
- Documentación del código

## Entrega

Cada proyecto debe incluir:

- Código fuente completo
- Script de inicialización de la base de datos
- Ejemplos de uso de todas las funciones
- README con instrucciones de instalación y uso
