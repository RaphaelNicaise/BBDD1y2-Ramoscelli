from pymongo import MongoClient

conn = "mongodb://127.0.0.1:27017/"

client = MongoClient(conn)

db = client.get_database('tiendaOnline')

ventas = db['ventas']
productos = db['productos']

#docs_ventas = [doc for doc in ventas.find()]

#docs_productos = [doc for doc in productos.find()]

pipeline = [
    {
        "$group": {
            "_id": "$categoria",
            "max": {"$max": "$precio" }, 
            "min": {"$min": "$precio" },
            "prom": {"$avg": "$precio" }
        }
    },
    {
        "$sort":{
            "prom": -1
        }
    }
]

if __name__ == "__main__":
    print(productos.aggregate(pipeline=pipeline).to_list())