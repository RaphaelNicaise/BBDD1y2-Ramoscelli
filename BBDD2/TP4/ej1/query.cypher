MATCH (p:Proyecto)-[:LIDERADO_POR]->(l:Lider),
    (p)-[:ASIGNADO_A]->(e:Empleado)
RETURN p.nombre AS Proyecto, l.nombre AS Lider, collect(e.nombre) AS Empleados_Asignados