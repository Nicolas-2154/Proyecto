from app.conexion.conexion_mysql import obtenerConexion
from app.model.gerente import Gerente

def crearGerente(gerente):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()

        sql = """INSERT INTO gerente(idUsuario,idDepartamento)
                VALUES(%s,%s)"""
        cursor.execute(sql, (gerente.idUsuario,gerente.getDepartamento(),))
        cone.commit()
        return True
    
    except Exception as e:
        print("Error al crear gerente: ",e)
    
    finally:
        if cone:
            cone.close()

def listarGerentes():
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM gerente")
        return cursor.fetchall()
    
    except Exception as e:
        print("Error al listar gerentes: ", e)

    finally:
        if cone:
            cone.close()

def buscarGerente(idGerente):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM gerente WHERE idGerente=%s", (idGerente,))
        return cursor.fetchone()
    
    except Exception as e:
        print("Error al buscar gerente: ",e)

    finally:
        if cone:
            cone.close()

def actualizarGerente(gerente):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        sql = """UPDATE gerente
                SET idDepartamento =%s WHERE idUsuario =%s"""
        cursor.execute(sql, (gerente.getidDepartamento(),gerente.getidUsuario()))
        cone.commit()
        return True

    except Exception as e:
        print("Error al actualizar gerente:",e)

    finally:
        if cone:
            cone.close()

def eliminarGerente(idUsuario):
    try:
        cone = obtenerConexion()
        if not cone:
            return
        cursor = cone.cursor()
        cursor.execute("DELETE FROM gerente WHERE idUsuario=%s",(idUsuario,))
        cone.commit()
        return True
    
    except Exception as e:
        print("Error al eliminar gerente: ",e)


    finally:
        if cone:
            cone.close()
