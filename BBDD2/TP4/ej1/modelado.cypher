CREATE  
        (e1:Empleado {nombre: "rapha"}),
        (e2:Empleado {nombre: "santi"}),
        (e3:Empleado {nombre: "abner"}),

        (d1:Departamento {nombre:"rrhh"}),
        (d2:Departamento {nombre:"sistemas"}),
        (d3:Departamento {nombre:"comercial"}),

        (p1:Proyecto {nombre: "proyecto1"}),
        (p2:Proyecto {nombre: "proyecto2"}),

        (e1)-[:PERTENECE_A]->(d1),
        (e2)-[:PERTENECE_A]->(d2),
        (e3)-[:PERTENECE_A]->(d3),

        (e1)-[:ASIGNADO_EN {horas_semanales: 30}]->(p1),
        (e2)-[:ASIGNADO_EN {horas_semanales: 35}]->(p2),
        (e3)-[:ASIGNADO_EN {horas_semanales: 30}]->(p1),
        (e3)-[:ASIGNADO_EN {horas_semanales: 25}]->(p2),
        
        (e1)-[:LIDERA]->(p1),
        (e2)-[:LIDERA]->(p2);