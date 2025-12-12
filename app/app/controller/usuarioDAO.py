from app.conexion.conexion_mysql import obtenerConexion
from app.model.usuario import Usuario
from app.utils.seguridad import generarHash, generarSalt, verificarContrasena


def crearUsuario(usuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        salt = generarSalt()
        hash_contrasena = generarHash(usuario.getContrasena() or "", salt)
        sql = (
            "INSERT INTO usuario(idUsuario,nombre,direccion,telefono,correo,rol,hashContrasena,salt) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        )
        cursor.execute(
            sql,
            (
                usuario.getID(),
                usuario.getNombre(),
                usuario.getDireccion(),
                usuario.getTelefono(),
                usuario.getCorreo(),
                usuario.getRol(),
                hash_contrasena,
                salt,
            ),
        )
        cone.commit()
        return True

    except Exception as e:
        print("Error al crear usuario: ", e)

    finally:
        if cone:
            cone.close()


def listarUsuarios():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute(
            "SELECT idUsuario, nombre, direccion, telefono, correo, rol FROM usuario"
        )
        return cursor.fetchall()

    except Exception as e:
        print("Error al listar los usuarios: ", e)

    finally:
        if cone:
            cone.close()


def buscarUsuario(idUsuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute(
            "SELECT idUsuario, nombre, direccion, telefono, correo, rol "
            "FROM usuario WHERE idUsuario=%s",
            (idUsuario,),
        )
        return cursor.fetchone()

    except Exception as e:
        print("Error al buscar usuario: ", e)

    finally:
        if cone:
            cone.close()


def actualizarUsuario(usuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """
            UPDATE usuario
            SET nombre=%s,direccion=%s,telefono=%s,correo=%s,rol=%s
            WHERE idUsuario=%s
        """
        cursor.execute(
            sql,
            (
                usuario.getNombre(),
                usuario.getDireccion(),
                usuario.getTelefono(),
                usuario.getCorreo(),
                usuario.getRol(),
                usuario.getID(),
            ),
        )
        cone.commit()
        return True

    except Exception as e:
        print("Error al actualizar usuario: ", e)

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
        print("Error al eliminar usuario: ", e)

    finally:
        if cone:
            cone.close()


def LoginUsuario(correo, contrasena):
    try:
        con = obtenerConexion()
        if not con:
            return None

        cursor = con.cursor()
        cursor.execute(
            "SELECT idUsuario, nombre, rol, hashContrasena, salt FROM usuario WHERE correo=%s",
            (correo,),
        )
        dato = cursor.fetchone()

        if dato:
            idUsuario, nombre, rol, hash_guardado, salt = dato
            if not hash_guardado or not salt:
                return None

            if verificarContrasena(contrasena, salt, hash_guardado):
                return {
                    "idUsuario": idUsuario,
                    "nombre": nombre,
                    "rol": rol,
                }

        return None

    except Exception as e:
        print("Error de login:", e)
        return None

    finally:
        if con:
            con.close()