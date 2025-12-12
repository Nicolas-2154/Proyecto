import os, msvcrt
from app.controller.usuarioDAO import *
from app.controller.empleadoDAO import *
from app.controller.departamentoDAO import *
from app.controller.proyectoDAO import *
from app.controller.registroTiempoDAO import *
from app.utils.serializacion import *

def menu_exportacion():
    menu="""EXPORTACIÓN DE DATOS
1. Exportar Usuarios
2. Exportar Empleados
3. Exportar Departamentos
4. Exportar Proyectos
5. Exportar Registros de Tiempo
0. Volver
"""

    while True:
        os.system('cls')
        print(menu)
        opc = input("Elija una opcion: ")
        os.system('cls')

        if opc == "0":
            break
        elif opc == "1":
            exportar_usuarios()
        elif opc == "2":
            exportar_empleados()
        elif opc == "3":
            exportar_departamentos()
        elif opc == "4":
            exportar_proyectos()
        elif opc == "5":
            exportar_registrosTiempo()


def exportar_usuarios():
    datos = listarUsuarios()
    encabezados = ["ID","Nombre","Direccion","Telefono","Correo","Rol"]

    ok_excel = exportar_excel("usuarios.xlsx",encabezados,datos)
    ok_pdf = exportar_pdf("usuarios.pdf","Listado de Usuarios",encabezados, datos)

    if ok_excel:
        print("Archivo usuarios.xslx creado")
    if ok_pdf:
        print("Archivo usuarios.pdf creado")

def exportar_empleados():
    datos = listarEmpleados()
    encabezados = ["ID","Nombre","Dirección","Telefono","Correo","Salario","Fecha inicio"]

    ok_excel = exportar_excel("empleados.xlsx",encabezados,datos)
    ok_pdf = exportar_pdf("empleados.pdf","Listado de Empleados",encabezados,datos)

    if ok_excel:
        print("Archivo empleados.xlsx creado con exito")
    if ok_pdf:
        print("Archivo empleados.pdf creado cn exito")

def exportar_departamentos():
    datos = listarDepartamentos()
    encabezados = ["ID","Nombre","ID Gerente"]

    ok_excel = exportar_excel("departamentos.xlsx",encabezados,datos)
    ok_pdf = exportar_pdf("departamentos.pdf","Listado de Departamentos",encabezados,datos)

    if ok_excel:
        print("Archivo departamentos.xlsx creado")
    if ok_pdf:
        print("Archivo departamentos.pdf creado") 

def exportar_proyectos():
    datos = listarProyectos()
    encabezados = ["ID","Nombre","Descripcion","Fecha Inicio"]

    ok_excel = exportar_excel("proyectos.xlsx",encabezados,datos)
    ok_pdf = exportar_pdf("proyectos.pdf","Listado de Proyectos",encabezados,datos)

    if ok_excel:
        print("Archivo departamentos.xlsx creado")
    if ok_pdf:
        print("Archivo departamentos.pdf creado con exito")

def exportar_registrosTiempo():
    datos = listarRegistrosTiempo()
    encabezados = ["ID","Fecha","Horas","Descripcion","ID empleado","ID proyecto"]

    ok_excel = exportar_excel("registroTiempo.xlsx",encabezados,datos)
    ok_pdf = exportar_pdf("registroTiempo.pdf","Registros de Tiempo",encabezados,datos)

    if ok_excel:
        print("Archivo registroTiempo.xlsx creado")
    if ok_pdf:
        print("Archivo registroTiempo.pdf creado")    