import mysql.connector

def obtenerConexion():
    try:
        return mysql.connector.connect(
            host ="localhost",
            user ="root",
            password ="",
            database ="ecoTech_db11"
        )
    except Exception as e:
        print("Error al conectarse a la base de datos:",e)
        return None

def obtenerConexionInicial():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
