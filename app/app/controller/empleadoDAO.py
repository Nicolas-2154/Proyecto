from app.conexion.conexion_mysql import obtenerConexion


def crearEmpleado(empleado):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()

        sql = (
            "INSERT INTO empleado(idUsuario, salario, fecha_inicio, idDepartamento) "
            "VALUES(%s,%s,%s,%s)"
        )
        cursor.execute(
            sql,
            (
                empleado.getID(),
                empleado.getSalario(),
                empleado.getFechaInicio(),
                None,
            ),
        )
        cone.commit()
        return True

    except Exception as e:
        print("Error al crear empleado:", e)

    finally:
        if cone:
            cone.close()


def listarEmpleados():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute(
            """
            SELECT u.idUsuario, u.nombre, u.correo, u.rol, e.salario, e.fecha_inicio
            FROM empleado e
            JOIN usuario u ON u.idUsuario = e.idUsuario
            """
        )
        return cursor.fetchall()

    except Exception as e:
        print("Error al listar empleados:", e)

    finally:
        if cone:
            cone.close()


def buscarEmpleado(idEmp):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute(
            """
            SELECT u.idUsuario, u.nombre, u.correo, u.rol, e.salario, e.fecha_inicio
            FROM empleado e
            JOIN usuario u ON u.idUsuario = e.idUsuario
            WHERE e.idUsuario=%s
            """,
            (idEmp,),
        )
        return cursor.fetchone()

    except Exception as e:
        print("Error al buscar empleado:", e)

    finally:
        if cone:
            cone.close()


def actualizarEmpleado(empleado):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()

        sql_usuario = (
            "UPDATE usuario SET nombre=%s, telefono=%s, correo=%s, rol=%s WHERE idUsuario=%s"
        )
        sql_empleado = "UPDATE empleado SET salario=%s, fecha_inicio=%s WHERE idUsuario=%s"

        cursor.execute(
            sql_usuario,
            (
                empleado.getNombre(),
                empleado.getTelefono(),
                empleado.getCorreo(),
                empleado.getRol(),
                empleado.getID(),
            ),
        )
        cursor.execute(
            sql_empleado,
            (empleado.getSalario(), empleado.getFechaInicio(), empleado.getID()),
        )
        cone.commit()
        return True

    except Exception as e:
        print("Error al actualizar empleado:", e)

    finally:
        if cone:
            cone.close()


def eliminarEmpleado(idEmp):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM empleado WHERE idUsuario=%s", (idEmp,))
        cone.commit()
        return True

    except Exception as e:
        print("Error al eliminar empleado:", e)

    finally:
        if cone:
            cone.close()
