from app.conexion.conexion_mysql import obtenerConexion
from app.model.departamento import Departamento

def crearDepartamento(departamento):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = "INSERT INTO departamento(nombre, idGerente) VALUES(%s,%s)"
        cursor.execute(sql, (departamento.getNombre(), departamento.getIdGerente()))
        cone.commit()
        return True

    except Exception as e:
        print("Error al crear departamento:", e)

    finally:
        if cone:
            cone.close()


def listarDepartamentos():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM departamento")
        return cursor.fetchall()

    except Exception as e:
        print("Error al listar departamentos:", e)

    finally:
        if cone:
            cone.close()


def buscarDepartamento(idDepartamento):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM departamento WHERE idDepartamento=%s", (idDepartamento,))
        return cursor.fetchone()

    except Exception as e:
        print("Error al buscar departamento:", e)

    finally:
        if cone:
            cone.close()


def actualizarDepartamento(departamento):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = "UPDATE departamento SET nombre=%s, idGerente=%s WHERE idDepartamento=%s"
        cursor.execute(sql, (departamento.getNombre(), departamento.getIdGerente(), departamento.getId()))
        cone.commit()
        return True

    except Exception as e:
        print("Error al actualizar departamento:", e)

    finally:
        if cone:
            cone.close()


def eliminarDepartamento(idDepartamento):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM departamento WHERE idDepartamento=%s", (idDepartamento,))
        cone.commit()
        return True

    except Exception as e:
        print("Error al eliminar departamento:", e)

    finally:
        if cone:
            cone.close()

def asignarGerenteDepartamento(idDepartamento, idGerente):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        
        cursor.execute("""
            UPDATE departamento SET idGerente = %s
            WHERE idDepartamento = %s
        """, (idGerente, idDepartamento))
        
        cone.commit()
        return True
    
    except Exception as e:
        print("Error asignando gerente:", e)
        return False
    
    finally:
        if cone:
            cone.close()
