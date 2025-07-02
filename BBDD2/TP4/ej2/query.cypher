MATCH (p:Prestamo {estado: "Activo"})-[r:CONTIENE]->(l:Libro) 
RETURN l.nombre;

MATCH (e:Estudiante)-[:REALIZA]->(p:Prestamo) 
RETURN e.nombre,count(p) as cant_prestamos;

MATCH (p:Prestamo)-[r1:CONTIENE]->(:Libro)-[r2:ES_CATEGORIA]->(c:Categoria) 
RETURN c.nombre,count(p) AS cant_prestamos 
ORDER BY cant_prestamos DESC;

MATCH (e:Estudiante) 
WHERE NOT (e)-[:REALIZA]->(:Prestamo {estado: "Activo"}) 
RETURN e.nombre;
