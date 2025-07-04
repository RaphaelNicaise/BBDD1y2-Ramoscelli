MATCH (u1)-[c:CONOCE]->(u2) 
RETURN u1.nombre,count(c) as conocidos 
ORDER BY conocidos DESC;

MATCH (u)-[r:POSTEA]->(p:Post)
RETURN u.nombre,count(p) AS posts
ORDER BY posts DESC
LIMIT 2;

MATCH (u)-[e:ENDOSA]->(h:Habilidad)
RETURN h.nombre,count(e) AS cant_endosadas 
ORDER BY cant_endosadas DESC;

MATCH (h:Habilidad)
WHERE NOT (:Usuario {nombre: "rapha123"})-[:ENDOSA]->(h) // habilidades que rapha123 no endoso
RETURN h.nombre AS habilidades_no_endosadas;