CREATE 

        (e1:Estudiante {nombre: 'Rapha'}),
        (e2:Estudiante {nombre: 'Abner'}),
        (e3:Estudiante {nombre: 'Santi'}),

        (m1:Materia {nombre: 'Programacion 1'}),
        (m2:Materia {nombre: 'Base de Datos 1'}),
        (m3:Materia {nombre: 'Programacion 2'}),

        (c1:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Mañana'}),
        (c2:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Tarde'}),
        (c3:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Mañana'}),
        (c4:Cursada {anio: 2025, cuatrimestre: 1, turno: 'Tarde'}),
        (c5:Cursada {anio: 2025, cuatrimestre: 2, turno: 'Mañana'}),
        (c6:Cursada {anio: 2025, cuatrimestre: 2, turno: 'Tarde'}),

        (m1)-[:MATERIA_DE]->(c1),
        (m1)-[:MATERIA_DE]->(c2),
        (m2)-[:MATERIA_DE]->(c3),
        (m2)-[:MATERIA_DE]->(c4),
        (m3)-[:MATERIA_DE]->(c5),
        (m3)-[:MATERIA_DE]->(c6),

        (m1)-[:PRERREQUISITO_DE]->(m3), // necesitas progra 1 para progra 2

        (e1)-[:INSCRIPTO {nota_final: 9}]->(c1), // hace progra 1 a la mañana
        (e1)-[:INSCRIPTO {nota_final: 6}]->(c3), // hace base de datos 1 a la mañana
        (e2)-[:INSCRIPTO {nota_final: 7}]->(c2), // hace progra 1 a la tarde
        (e2)-[:INSCRIPTO {nota_final: 4}]->(c4), // hace base de datos 1 a la tarde
        (e3)-[:INSCRIPTO {nota_final: 5}]->(c5), // hace progra 2 a la mañana
        (e3)-[:INSCRIPTO {nota_final: 9}]->(c3) // recursa base de datos 1 a la mañana
        ; 