from app.conexion.conexion_mysql import obtenerConexion
from app.model.registroTiempo import RegistroTiempo

def crearRegistroTiempo(registroTiempo):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """INSERT INTO registroTiempo(fecha, horas, descripcion, idEmpleado, idProyecto)
                 VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(sql,(registroTiempo.getFecha(),
                            registroTiempo.getHoras(),
                            registroTiempo.getDescripcion(),
                            registroTiempo.getIdEmpleado(),
                            registroTiempo.getIdProyecto()))
        cone.commit()
        return True
    except Exception as e:
        print("Error al crear registro:", e)
    finally:
        if cone:
            cone.close()


def listarRegistrosTiempo():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM registroTiempo")
        return cursor.fetchall()
    except Exception as e:
        print("Error al listar registros:", e)
    finally:
        if cone:
            cone.close()


def buscarRegistroTiempo(idRegistro):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM registroTiempo WHERE idRegistro=%s",(idRegistro,))
        return cursor.fetchone()
    except Exception as e:
        print("Error al buscar registro:", e)
    finally:
        if cone:
            cone.close()


def actualizarRegistroTiempo(registroTiempo):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """UPDATE registroTiempo
                 SET fecha=%s, horas=%s, descripcion=%s, idEmpleado=%s, idProyecto=%s
                 WHERE idRegistro=%s"""
        cursor.execute(sql,(registroTiempo.getFecha(),
                            registroTiempo.getHoras(),
                            registroTiempo.getDescripcion(),
                            registroTiempo.getIdEmpleado(),
                            registroTiempo.getIdProyecto(),
                            registroTiempo.getId()))
        cone.commit()
        return True
    except Exception as e:
        print("Error al actualizar registro:", e)
    finally:
        if cone:
            cone.close()


def eliminarRegistroTiempo(idRegistro):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM registroTiempo WHERE idRegistro=%s",(idRegistro,))
        cone.commit()
        return True
    except Exception as e:
        print("Error al eliminar registro:", e)
    finally:
        if cone:
            cone.close()
