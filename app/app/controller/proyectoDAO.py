from app.conexion.conexion_mysql import obtenerConexion
from app.model.proyecto import Proyecto

def crearProyecto(proyecto):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """INSERT INTO proyecto(nombre, descripcion, fecha_inicio)
                 VALUES(%s,%s,%s)"""
        cursor.execute(sql,(proyecto.getNombre(),
                            proyecto.getDescripcion(),
                            proyecto.getFechaInicio()))
        cone.commit()
        return True
    except Exception as e:
        print("Error al crear proyecto:", e)
    finally:
        if cone:
            cone.close()


def listarProyectos():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM proyecto")
        return cursor.fetchall()
    except Exception as e:
        print("Error al listar proyectos:", e)
    finally:
        if cone:
            cone.close()


def buscarProyecto(idProyecto):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM proyecto WHERE idProyecto = %s",(idProyecto,))
        return cursor.fetchone()
    except Exception as e:
        print("Error al buscar proyecto:", e)
    finally:
        if cone:
            cone.close()


def actualizarProyecto(proyecto):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """UPDATE proyecto SET nombre=%s, descripcion=%s, fecha_inicio=%s
                 WHERE idProyecto=%s"""
        cursor.execute(sql,(proyecto.getNombre(),
                            proyecto.getDescripcion(),
                            proyecto.getFechaInicio(),
                            proyecto.getId()))
        cone.commit()
        return True
    except Exception as e:
        print("Error al actualizar proyecto:", e)
    finally:
        if cone:
            cone.close()


def eliminarProyecto(idProyecto):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM proyecto WHERE idProyecto=%s",(idProyecto,))
        cone.commit()
        return True
    except Exception as e:
        print("Error al eliminar proyecto:", e)
    finally:
        if cone:
            cone.close()
