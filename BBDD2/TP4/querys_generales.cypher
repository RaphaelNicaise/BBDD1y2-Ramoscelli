// devuelve todos los nodos
MATCH (n) RETURN n; 

// borra nodos
MATCH (n) DELETE n; 

// devuelve todos los nodos y relaciones
MATCH (n)-[r]->(m) RETURN n,r,m; 

// devuelve todos los nodos y relaciones
MATCH (n)-[r]->(m) DELETE n,r,m; 