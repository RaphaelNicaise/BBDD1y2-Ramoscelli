CREATE 
        (e1:Estudiante {nombre: "rapha"}),
        (e2:Estudiante {nombre: "santi"}),
        (e3:Estudiante {nombre: "abner"}),

        (l1:Libro {autor: "joe reis & matt housley",nombre: "fundamentals of data engineering"}),
        (l2:Libro {autor: "jules verne",nombre:"viaje al centro de la tierra"}),
        (l3:Libro {autor: "mateo salvatto",nombre:"la batalla del futuro"}),
        (l4:Libro {autor: "george orwell",nombre:"la rebelion de la granja"}),

        (c1:Carrera {nombre: "Tecnicatura en Programacion"}),
        (c2:Carrera {nombre: "Ingenieria en Sistemas"}),

        (cat1:Categoria {nombre: "informatica"}),        
        (cat2:Categoria {nombre: "ficcion"}),
        (cat3:Categoria {nombre: "tecnologia"}),
        (cat4:Categoria {nombre: "Literatura Politica"}),

        (l1)-[:ES_CATEGORIA]->(cat1),
        (l2)-[:ES_CATEGORIA]->(cat2),
        (l3)-[:ES_CATEGORIA]->(cat3),
        (l4)-[:ES_CATEGORIA]->(cat4),
        

        (e1)-[:ESTUDIA]->(c1),
        (e2)-[:ESTUDIA]->(c1),
        (e3)-[:ESTUDIA]->(c2),

        (e1)-[:REALIZA]->(p1:Prestamo {fecha:"2025-07-01", estado:"Activo"})-[:CONTIENE]->(l2),
        (e2)-[:REALIZA]->(p2:Prestamo {fecha:"2025-06-27", estado:"Activo"})-[:CONTIENE]->(l3),
        (e3)-[:REALIZA]->(p3:Prestamo {fecha:"2025-07-02", estado:"Activo"})-[:CONTIENE]->(l1),
        (e1)-[:REALIZA]->(p4:Prestamo {fecha:"2025-06-11", estado:"Devuelto"})-[:CONTIENE]->(l4),
        (e2)-[:REALIZA]->(p5:Prestamo {fecha:"2025-05-31", estado:"Devuelto"})-[:CONTIENE]->(l1);


