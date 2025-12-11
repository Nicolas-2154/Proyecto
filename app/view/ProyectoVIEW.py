from app.controller.proyectoDAO import *
from app.model.proyecto import Proyecto
from datetime import datetime
import msvcrt,os

def menu_proyecto():
    menu ="""MENÚ PROYECTOS
    1. Crear Proyecto
    2. Listar Proyectos
    3. Buscar Proyecto
    4. Actualizar Proyecto
    5. Eliminar Proyecto
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
            crear_proyecto()
        elif opc == "2":
            listar_proyectos()
        elif opc == "3":
            buscar_proyecto()
        elif opc == "4":
            actualizar_proyecto()
        elif opc == "5":
            eliminar_proyecto()
        else:
            print("Opcion incorrecta")
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()

def crear_proyecto():
    print("CREAR PROYECTO")
    idProyecto =int(input("Ingrese la ID del proyecto: "))
    while True:
        nombre = input("Ingrese el nombre del proyecto: ")
        if nombre.replace(" ","").isalpha():
            break
        print("Error! El nombre no puede estar vacio o contener numeros")

    descripcion = input("Ingrese la descripcion del proyecto: ")

    while True:
        fecha = input("Ingrese la fecha de inicio del proyecto: ")
        try:
            fecha_sql=datetime.strptime(fecha,"%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except:
            print("Error! Formato de fecha incorrecto")

    pro = Proyecto(idProyecto,nombre,descripcion,fecha)

    if crearProyecto(pro):
        print("Proyecto creado")
    else:
        print("Error al crear el proyecto")

def listar_proyectos():
    print("LISTAR PROYECTOS")
    datos = listarProyectos()
    if datos:
        for p in datos:
            print(p)

def buscar_proyecto():
    print("BUSCAR PROYECTO")
    idProyecto = int(input("Ingrese la ID del proyecto: "))
    dato = buscarProyecto(idProyecto)
    if dato:
        print(dato)
    else:
        print("Proyecto no existe")

def actualizar_proyecto():
    print("ACTUALIZAR PROYECTO")
    idProyecto = int(input("Ingrese la ID del proyecto a actualzar:"))
    if not buscarProyecto(idProyecto):
        print("Proyecto no existe")
        return
    while True:
        nuevoNombre = input("Ingrese un nuevo nombre para el proyecto: ")
        if nuevoNombre.replace(" ","").isalpha():
            break
        print("Error! EL nombre no puede estar vacio o contener numeros")

    nuevaDescripcion = input("Ingrese una nueva descripcion para el proyecto: ")

    while True:
        nuevaFecha = input("Ingrese una nueva fecha de inicio para el proyecto: ")
        try:
            fecha_sql=datetime.strptime(nuevaFecha,"%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except:
            print("Error! Formato de fecha incorrecto")

    pro=Proyecto(idProyecto,nuevoNombre,nuevaDescripcion,nuevaFecha)

    if actualizarProyecto(pro):
        print("Proyecto actualizado con exito")
    else:
        print("Error al actualizar el proyecto")

def eliminar_proyecto():
    print("ELIMINAR PROYECTO")
    idProyecto=int(input("Ingrese la ID del proyecto a eliminar"))
    if eliminarProyecto(idProyecto):
        print("Proyecto eliminado con exito")
    else:
        print("Proyecto no existe.")