from app.controller.registroTiempoDAO import *
from app.model.registroTiempo import RegistroTiempo
from datetime import datetime
import msvcrt,os

def menu_registroTiempo():
    menu ="""MENÚ REGISTROS DE TIEMPO
    1. Crear Registro de tiempo
    2. Listar Registros de tiempos
    3. Buscar Registro de tiempo
    4. Actualizar Registro de tiempo
    5. Eliminar Registro de tiempo
    0. Volver
    """

    while True:
        os.system('cls')
        print(menu)
        opc = input("Elija una opcion")
        os.system('cls')

        if opc == "0":
            break
        elif opc == "1":
            crear_registroTiempo()
        elif opc == "2":
            listar_registrosTiempo()
        elif opc == "3":
            buscar_registroTiempo()
        elif opc == "4":
            actualizar_registroTiempo()
        elif opc == "5":
            eliminar_registroTiempo()
        else:
            print("Opcion incorrecta")
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()


def crear_registroTiempo():
    print("CREAR REGISTRO DE TIEMPO")
    idRegistro = int(input("Ingrese la ID del registro de tiempo: "))

    while True:
        fecha = input("Ingrese la fecha del registro de tiempo: ")
        try:
            fecha_sql = datetime.strptime(fecha,"%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except:
            print("Error! Formato de fecha incorrecto")

    horas =float(input("Ingrese las horas trabajadas del empleado: "))
    descripcion =input("Ingrese la descripcion del registro de tiempo: ")
    idEmpleado = int(input("Ingrese la ID del empleado asociado al registro de tiempo: "))
    idProyecto=int(input("Ingrese la ID del proyecto asociado al registro de tiempo: "))

    reT=RegistroTiempo(idRegistro,fecha,horas,descripcion,idEmpleado,idProyecto)

    if crearRegistroTiempo(reT):
        print("Registro de tiempo creado.")
    else:
        print("Error al crear el registro de tiempo.")

def listar_registrosTiempo():
    print("LISTAR REGISTROS DE TIEMPO")
    datos = listarRegistrosTiempo()
    if datos:
        for r in datos:
            print(r)

def buscar_registroTiempo():
    print("BUSCAR REGISTRO DE TIEMPO")
    idRegistroTiempo=int(input("Ingrese la ID del registro de tiempo: "))
    dato = buscarRegistroTiempo(idRegistroTiempo)
    if dato:
        print(dato)
    else:
        print("Registro de tiempo no existe")

def actualizar_registroTiempo():
    print("ACTUALIZAR REGISTRO DE TIEMPO")
    idRegistro=int(input("Ingrese la ID del registro de tiempo a actualizar: "))
    if not buscarRegistroTiempo(idRegistro):
        print("Error! Registro de tiempo no existe")
        return
    while True:
        nuevaFecha=input("Ingrese una nueva fecha: ")
        try:
            fecha_sql = datetime.strptime(nuevaFecha,"%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except:
            print("Error! Formato de fecha incorrecto")

    nuevaHoras=input("Ingrese las nuevas horas trabajadas del empleado: ")
    nuevaDescripcion=input("Ingrese una nueva descripcion para el registro de tiempo: ")
    nuevoIdEmpleado=int(input("Ingrese un nuevo ID de empleado: "))
    nuevoIdProyecto=int(input("Ingrese un nuevo ID de proyecto: "))

    reT=RegistroTiempo(idRegistro,nuevaFecha,nuevaHoras,nuevaDescripcion,nuevoIdEmpleado,nuevoIdProyecto)

    if actualizarRegistroTiempo(reT):
            print("Registro de tiempo actualizado con exito")
    else:
            print("Error al actualizar el registro de tiempo")


def eliminar_registroTiempo():
    print("ELIMINAR REGISTRO DE TIEMPO")
    idRegistro=int(input("Ingrese la ID del registro de tiempo a eliminar"))
    if eliminarRegistroTiempo(idRegistro):
        print("Registro de tiempo eliminado con exito")
    else:
        print("Registro de tiempo no existe")