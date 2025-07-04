MATCH (e:Estudiante)- [i:INSCRIPTO]->(c:Cursada)<-[:MATERIA_DE]-(m:Materia) // notas de rapha
WHERE e.nombre = "Rapha"
RETURN 
  m.nombre AS materia,
  c.anio AS año,
  c.cuatrimestre AS cuatrimestre,
  c.turno AS curno,
  i.nota_final AS nota;

MATCH (prer:Materia)-[:PRERREQUISITO_DE]->(:Materia {nombre: "Programacion 2"})
WHERE NOT EXISTS {
  MATCH (:Estudiante {nombre: "Santi"})-[r:INSCRIPTO]->(:Cursada)-[:MATERIA_DE]->(prer)
  WHERE r.nota_final >= 6
}
RETURN COUNT(prer) = 0 AS puede_inscribirse;

MATCH (e:Estudiante)-[i:INSCRIPTO]->(c:Cursada) 
RETURN e.nombre,avg(i.nota_final);

MATCH (e:Estudiante)-[i:INSCRIPTO]->(c:Cursada)<-[md:MATERIA_DE]-(m:Materia) 
WITH m.nombre as nombre, avg(i.nota_final) AS promedio
WHERE promedio < 7
RETURN nombre, promedio;


