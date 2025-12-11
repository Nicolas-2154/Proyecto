from app.conexion.conexion_mysql import obtenerConexion
from app.model.empleado import Empleado

def crearEmpleado(empleado):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()

        sql = """INSERT INTO empleado(nombre, direccion, telefono, email, salario, fecha_inicio)
                 VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (empleado.getNombre(),
                             empleado.getDireccion(),
                             empleado.getTelefono(),
                             empleado.getEmail(),
                             empleado.getSalario(),
                             empleado.getFechaInicio()))
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
        cursor.execute("SELECT * FROM empleado")
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
        cursor.execute("SELECT * FROM empleado WHERE idEmpleado=%s", (idEmp,))
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
        sql = """UPDATE empleado 
                 SET nombre=%s, direccion=%s, telefono=%s, email=%s, salario=%s 
                 WHERE idEmpleado=%s"""
        cursor.execute(sql, (empleado.getNombre(),
                             empleado.getDireccion(),
                             empleado.getTelefono(),
                             empleado.getEmail(),
                             empleado.getSalario(),
                             empleado.getId()))
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
        cursor.execute("DELETE FROM empleado WHERE idEmpleado=%s", (idEmp,))
        cone.commit()
        return True

    except Exception as e:
        print("Error al eliminar empleado:", e)

    finally:
        if cone:
            cone.close()
