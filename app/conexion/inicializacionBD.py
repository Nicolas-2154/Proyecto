import os
from app.conexion.conexion_mysql import obtenerConexionInicial

def inicializar_bd():
    try:
        cone = obtenerConexionInicial()
        if not cone:
            return
        cursor = cone.cursor()

        ruta_sql = os.path.join(
            os.path.dirname(__file__),
            "baseDatos.sql"
        )

        with open(ruta_sql, "r", encoding="utf-8") as f:
            statements = f.read().split(';')
        
        for query in statements:
            q = query.strip()
            if q:
                cursor.execute(q)
        
        cone.commit()
        print("✔ Base de datos inicializada")
    except Exception as e:
        print("Error inicializando BD:", e)
    finally:
        if cone:
            cone.close()
