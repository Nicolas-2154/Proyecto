import os
from app.conexion.conexion_mysql import obtenerConexionInicial
from app.utils.seguridad import generarHash, generarSalt

def inicializar_bd():
    cone = None
    mensaje_admin = None
    try:
        cone = obtenerConexionInicial()
        if not cone:
            return None
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
        mensaje_admin = asegurar_admin(cursor, cone)
        print("Base de datos inicializada")
    except Exception as e:
        print("Error inicializando BD:", e)
    finally:
        if cone:
            cone.close()

    return mensaje_admin


def asegurar_admin(cursor, cone):
    try:
        cursor.execute("USE ecotech_db11")
        cursor.execute("SELECT COUNT(*) FROM usuario")
        total_usuarios = cursor.fetchone()[0]

        if total_usuarios == 0:
            salt = generarSalt()
            contrasena = "1234"
            hash_contrasena = generarHash(contrasena, salt)
            cursor.execute(
                """
                INSERT INTO usuario(idUsuario, nombre, direccion, telefono, correo, rol, hashContrasena, salt)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    1,
                    "Administrador",
                    "N/A",
                    "11111111",
                    "admin@admin.com",
                    "admin",
                    hash_contrasena,
                    salt,
                ),
            )
            cone.commit()
            return "Usuario de prueba creado: admin@admin.com / 1234"

        cursor.execute(
            "SELECT hashContrasena, salt FROM usuario WHERE correo=%s",
            ("admin@admin.com",),
        )
        registro = cursor.fetchone()

        if not registro:
            return None

        hash_actual, salt_actual = registro
        if not hash_actual or not salt_actual or len(hash_actual) != 64:
            salt = generarSalt()
            hash_contrasena = generarHash("1234", salt)
            cursor.execute(
                "UPDATE usuario SET hashContrasena=%s, salt=%s WHERE correo=%s",
                (hash_contrasena, salt, "admin@admin.com"),
            )
            cone.commit()
    except Exception:
        
        return None

    return None