from app.controller.empleadoDAO import *
from app.controller.usuarioDAO import buscarUsuario
from app.model.empleado import Empleado
from datetime import datetime
import msvcrt
import os


def _mostrar_menu(menu_title, opciones):
    barra = "=" * 50
    print(barra)
    print(f"{menu_title:^50}")
    print(barra)
    for numero, texto in opciones:
        print(f" {numero}. {texto}")
    print(barra)


def _formatear_empleados(datos):
    if not datos:
        print("No hay empleados registrados.")
        return

    encabezados = ["ID", "Nombre", "Correo", "Rol", "Salario", "Fecha inicio"]
    ancho = [8, 20, 28, 12, 14, 16]
    borde = "+" + "+".join("-" * (a + 2) for a in ancho) + "+"

    print(borde)
    print(
        "|"
        + "|".join(
            f" {encabezados[idx].center(ancho[idx])} "
            for idx in range(len(encabezados))
        )
        + "|"
    )
    print(borde)

    for fila in datos:
        idUsuario, nombre, correo, rol, salario, fecha_inicio = fila[:6]
        columnas = [
            str(idUsuario).center(ancho[0]),
            str(nombre)[: ancho[1]].ljust(ancho[1]),
            str(correo)[: ancho[2]].ljust(ancho[2]),
            str(rol).center(ancho[3]),
            f"${salario:.2f}".rjust(ancho[4]),
            str(fecha_inicio).center(ancho[5]),
        ]
        print("|" + "|".join(f" {col} " for col in columnas) + "|")
    print(borde)


def menu_empleado():
    opciones = [
        ("1", "Crear Empleado"),
        ("2", "Listar Empleado"),
        ("3", "Buscar Usuario"),
        ("4", "Actualizar Empleado"),
        ("5", "Eliminar Empleado"),
        ("0", "Volver"),
    ]

    while True:
        os.system("cls")
        _mostrar_menu("MENÚ EMPLEADOS", opciones)
        opc = input("Elija una opcion: ")
        os.system("cls")

        if opc == "0":
            break
        elif opc == "1":
            crear_empleado()
        elif opc == "2":
            listar_empleados()
        elif opc == "3":
            buscar_empleado()
        elif opc == "4":
            actualizar_empleado()
        elif opc == "5":
            eliminar_empleado()
        else:
            print("Opcion incorrecta")

        print("\nPresione una tecla para continuar...")
        msvcrt.getch()


def crear_empleado():
    print("CREAR EMPLEADO.")
    while True:
        try:
            idUsuario = int(input("Ingrese la ID del empleado: "))
        except ValueError:
            print("Error: la ID debe ser un número entero.")
            continue

        if buscarEmpleado(idUsuario):
            print("La ID ingresada ya está registrada. Elija otra.")
            continue
        break

    if not buscarUsuario(idUsuario):
        print("Primero debe existir un usuario con esta ID para asociarlo como empleado.")
        return

    while True:
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre.replace(" ", "").isalpha():
            break
        print("Error!: El nombre no puede quedar vacio o contener numeros.")

    while True:
        correo = input("Ingrese el correo: ")
        if "@" in correo and "." in correo:
            break
        print("Error! Correo invalido")

    while True:
        telefono = input("Ingrese el numero de telefono (+569XXXXXXXX): ").strip()
        if telefono.startswith("+569") and telefono[4:].isdigit() and len(telefono) == 12:
            break
        print("Error! El telefono debe tener el formato +569XXXXXXXX (8 dígitos).")

    salario = float(input("Ingrese el salario del empleado: "))

    while True:
        fecha_inicio = input("Ingrese la fecha de inicio de contrato: (dd/mm/yyyy) ")
        try:
            fecha_sql = datetime.strptime(fecha_inicio, "%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except Exception:
            print("Error: Por favor use el formato correcto dd/mm/yyyy")

    rol = input("Ingrese el rol del empleado: ")

    emp = Empleado(
        idUsuario,
        nombre,
        "",
        telefono,
        correo,
        rol,
        salario,
        fecha_sql,
    )

    if crearEmpleado(emp):
        print("Empleado creado.")
    else:
        print("Error al crear empleado.")


def listar_empleados():
    print("LISTAR EMPLEADOS.")
    datos = listarEmpleados()
    _formatear_empleados(datos)


def buscar_empleado():
    print("BUSCAR EMPLEADOS.")
    try:
        idEmp = int(input("Ingrese la ID del empleado: "))
    except ValueError:
        print("Error: la ID debe ser un número entero.")
        return
    dato = buscarEmpleado(idEmp)
    if dato:
        _formatear_empleados([dato])
    else:
        print("Empleado no existe.")


def actualizar_empleado():
    print("ACTUALIZAR EMPLEADO.")
    try:
        idEmp = int(input("Ingrese la ID del empleado a actualizar: "))
    except ValueError:
        print("Error: la ID debe ser un número entero.")
        return

    if not buscarEmpleado(idEmp):
        print("Empleado no existe")
        return

    while True:
        nuevoNombre = input("Ingrese el nuevo nombre del empleado: ")
        if nuevoNombre.replace(" ", "").isalpha():
            break
        print("Error! Nombre invalido")

    while True:
        nuevoCorreo = input("Ingrese el nuevo correo: ")
        if "@" in nuevoCorreo and "." in nuevoCorreo:
            break
        print("Error! Formato de correo invalido")

    while True:
        nuevoTelefono = input("Ingrese el nuevo telefono (+569XXXXXXXX): ").strip()
        if nuevoTelefono.startswith("+569") and nuevoTelefono[4:].isdigit() and len(nuevoTelefono) == 12:
            break
        print("Error! El telefono debe tener el formato +569XXXXXXXX (8 dígitos).")

    nuevoRol = "Empleado"

    nuevoSalario = float(input("Ingrese el nuevo salario: "))

    while True:
        nuevaFechaInicio = input("Ingresa una nueva fecha de inicio de contrato (dd/mm/yyyy): ")
        try:
            fecha_sql = datetime.strptime(nuevaFechaInicio, "%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except Exception:
            print("Error! Por favor use el formato correcto dd/mm/yyyy")

    emp = Empleado(
        idEmp,
        nuevoNombre,
        "",
        nuevoTelefono,
        nuevoCorreo,
        nuevoRol,
        nuevoSalario,
        fecha_sql,
    )

    if actualizarEmpleado(emp):
        print("Empleado actualizado con exito.")
    else:
        print("Error al actualizar al empleado.")


def eliminar_empleado():
    print("ELIMINAR EMPLEADO")
    try:
        idEmp = int(input("Ingrese la ID del empleado a eliminar: "))
    except ValueError:
        print("Error: la ID debe ser un número entero.")
        return
    if eliminarEmpleado(idEmp):
        print("Empleado eliminado con exito")
    else:
        print("Empleado no existe.")