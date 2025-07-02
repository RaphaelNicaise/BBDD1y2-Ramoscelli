# Proyecto: Sistema de Inventario de Tienda

##
## Descripción

Sistema para la gestión de inventario en una tienda, permitiendo el control de productos, proveedores y movimientos de stock.

---

## Requerimientos

- **Catálogo de productos** con stock actual.
- **Registro de proveedores** y sus productos.
- **Movimientos** de entrada y salida de mercancía.
- **Alertas** de stock bajo.

---

## Funciones a Implementar

- `agregarProducto(producto)`  
    Añadir un producto al catálogo.

- `registrarMovimiento(movimiento)`  
    Registrar la entrada o salida de stock.

- `consultarStock(codigo)`  
    Consultar el stock actual de un producto.

- `productosStockBajo()`  
    Listar productos con stock por debajo del mínimo.

- `reporteMovimientos(fechaInicio, fechaFin)`  
    Generar un reporte de movimientos en un período específico.

---

## Instalación

```bash
pip install pymongo
```

---

## Criterios de Evaluación

- Correcta implementación de las operaciones **CRUD**
- Uso apropiado de **consultas** y **agregaciones**
- Manejo de **errores** y **validaciones**
- Estructura de datos eficiente
- Documentación clara del código

---

## Entrega

Cada proyecto debe incluir:

- Código fuente completo
- Script de inicialización de la base de datos
- Ejemplos de uso de todas las funciones
- README con instrucciones de instalación y uso
