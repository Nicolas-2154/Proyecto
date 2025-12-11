from app.conexion.conexion_mysql import obtenerConexion
from app.model.usuario import Usuario
from app.utils.seguridad import *

def crearUsuario(usuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        salt = generarSalt()
        hashContrasena = generarHash(usuario.getContrasena(), salt) 
        sql = """INSERT INTO usuario(idUsuario,nombre,direccion,telefono,correo,rol,hashContraseña,salt) 
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (usuario.getID(),usuario.getNombre(),usuario.getDireccion(),usuario.getTelefono(),usuario.getCorreo(),usuario.getRol(),usuario.getContrasena(),salt))
        cone.commit()
        return True
    
    except Exception as e:
        print("Error al crear usuario: ",e)

    finally:
        if cone:
            cone.close()


def listarUsuarios():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM departamento")
        return cursor.fetchall()

    except Exception as e:
        print("Error al listar los usuarios: ",e)

    finally:
        if cone:
            cone.close()


def buscarUsuario(idUsuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM usuario WHERE idUsuario=%s", (idUsuario,))
        return cursor.fetchone()
    
    except Exception as e:
        print("Error al buscar usuario: ",e)

    finally:
        if cone:
            cone.close()


def actualizarUsuario(usuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = "UPDATE usuario SET idUsuario=%s,nombre=%s,direccion=%s,telefono=%s,correo=%s,rol=%s"
        cursor.execute(sql,(usuario.getID(),usuario.getNombre(),usuario.getDireccion(),usuario.getTelefono(),usuario.getCorreo(),usuario.getRol()))
        cone.commit()
        return True
    
    except Exception as e:
        print("Error al actualizar usuario: ",e)

    finally:
        if cone:
            cone.close()


def eliminarUsuario(idUsuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM usuario WHERE idUsuario=%s", (idUsuario,))
        cone.commit()
        return True

    except Exception as e:
        print("Error al eliminar usuario: ",e)
    
    finally:
        if cone:
            cone.close()

def LoginUsuario(correo, contrasena):
    try:
        con = obtenerConexion()
        if not con:
            return None

        cursor = con.cursor()
        cursor.execute("SELECT idUsuario, nombre, rol, hashContrasena FROM usuario WHERE correo=%s", (correo,))
        dato = cursor.fetchone()

        if dato:
            idUsuario, nombre, rol, hash_guardado = dato

            # === LOGIN SIN HASH (SOLO PRUEBAS) ==================
            # si la contraseña que ingresas es igual al campo hashContrasena
            # dejamos entrar
            if contrasena == hash_guardado:
                return {
                    "idUsuario": idUsuario,
                    "nombre": nombre,
                    "rol": rol
                }
            # ======================================================

        return None

    except Exception as e:
        print("Error de login:", e)
        return None

    finally:
        if con:
            con.close()