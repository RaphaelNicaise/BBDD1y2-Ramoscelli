MATCH (p:Proyecto)<-[:LIDERA]-(l:Empleado),(e:Empleado)-[:ASIGNADO_EN]->(p)
RETURN p.nombre AS proycto, l.nombre AS Lider,collect(e.nombre) AS empleados;

MATCH (e:Empleado)-[a:ASIGNADO_EN]->(p:Proyecto) 
RETURN p.nombre, sum(a.horas_semanales);

MATCH (e:Empleado)-[:ASIGNADO_EN]->(p:Proyecto)
WITH e, COUNT(p) AS cant_proyectos
WHERE cant_proyectos > 1
RETURN e.nombre, cant_proyectos;