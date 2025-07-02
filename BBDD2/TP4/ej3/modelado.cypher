CREATE 
        (u1:Usuario {nombre:"rapha123"}),
        (u2:Usuario {nombre:"xXSantuchoXx"}),
        (u3:Usuario {nombre:"Abner777"}),
        (u4:Usuario {nombre:"NicoCrack"}),

        (u1)-[:CONOCE]->(u4),
        (u1)<-[:CONOCE]-(u4),
        (u1)-[:CONOCE]->(u2),
        (u1)<-[:CONOCE]-(u2),
        (u1)-[:CONOCE]->(u3),
        (u1)<-[:CONOCE]-(u3),
        (u2)-[:CONOCE]->(u3),
        (u2)<-[:CONOCE]-(u3),

        (u1)-[:POSTEA]->(p1:Post {descripcion: "Foto de mi gato"}),
        (u2)-[:POSTEA]->(p2:Post {descripcion: "<3"}),
        (u3)-[:POSTEA]->(p3:Post {descripcion: "Foto con mi primo"}),
        
        (u1)-[:TIENE]->(h1:Habilidad {nombre: "Cocinar"}),
        (u1)-[:TIENE]->(h2:Habilidad {nombre: "Programar"}),
        (u2)-[:TIENE]->(h3:Habilidad {nombre: "Cocinar"}),
        (u2)-[:TIENE]->(h4:Habilidad {nombre: "Socializar"}),
        (u3)-[:TIENE]->(h5:Habilidad {nombre: "Bueno en Deportes"}),
        (u3)-[:TIENE]->(h6:Habilidad {nombre: "Diseñar"}),
        (u4)-[:TIENE]->(h7:Habilidad {nombre: "Negociar"}),        
        (u4)-[:TIENE]->(h8:Habilidad {nombre: "Dibujar"}),


        (u1)-[:ENDOSA]->(h8),
        (u2)-[:ENDOSA]->(h2),
        (u3)-[:ENDOSA]->(h2);