use("empresa");

db.createUser(
    {
        user: "admin",
        pwd: "1234",
        roles: [
            "readWrite" // Permisos de lectura y escritura
        ]
    }
);

