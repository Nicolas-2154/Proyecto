from app.model.usuario import Usuario
from app.controller.usuarioDAO import (
    LoginUsuario,
    actualizarUsuario,
    buscarUsuario,
    crearUsuario,
    eliminarUsuario,
    listarUsuarios,
)
from app.controller.empleadoDAO import crearEmpleado
from app.view.DepartamentoVIEW import menu_departamento
from app.view.EmpleadoVIEW import menu_empleado
from app.view.ProyectoVIEW import menu_proyecto
from app.view.RegistroTiempoVIEW import menu_registroTiempo
from app.view.apiVIEW import MostrarClima, mostrarUF
from app.view.exportacionVIEW import menu_exportacion
from app.model.empleado import Empleado
import msvcrt
import os
from datetime import datetime


def _mostrar_menu(menu_title, opciones):
    barra = "=" * 50
    print(barra)
    print(f"{menu_title:^50}")
    print(barra)
    for numero, texto in opciones:
        print(f" {numero}. {texto}")
    print(barra)


def _formatear_usuarios(datos):
    if not datos:
        print("No hay usuarios registrados.")
        return

    encabezados = ["ID", "Nombre", "Dirección", "Teléfono", "Correo", "Rol"]
    ancho = [10, 18, 18, 14, 24, 12]
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
        idUsuario, nombre, direccion, telefono, correo, rol = fila[:6]
        columnas = [
            str(idUsuario).center(ancho[0]),
            str(nombre)[: ancho[1]].ljust(ancho[1]),
            str(direccion)[: ancho[2]].ljust(ancho[2]),
            str(telefono)[: ancho[3]].ljust(ancho[3]),
            str(correo)[: ancho[4]].ljust(ancho[4]),
            str(rol).center(ancho[5]),
        ]
        print("|" + "|".join(f" {col} " for col in columnas) + "|")
    print(borde)


def menu_usuario():
    opciones = [
        ("1", "Gestionar Empleados"),
        ("2", "Gestionar Departamentos"),
        ("3", "Gestionar Proyectos"),
        ("4", "Gestionar Registros de Tiempo"),
        ("5", "Exportar datos"),
        ("6", "Mostrar UF"),
        ("7", "Mostrar Clima"),
        ("0", "Cerrar sesión"),
    ]

    while True:
        os.system("cls")
        _mostrar_menu("MENÚ USUARIOS", opciones)
        opc = input("Elija una opcion: ")
        os.system("cls")

        if opc == "0":
            print("Cerrando sesión")
            break
        elif opc == "1":
            menu_empleado()
        elif opc == "2":
            menu_departamento()
        elif opc == "3":
            menu_proyecto()
        elif opc == "4":
            menu_registroTiempo()
        elif opc == "5":
            menu_exportacion()
        elif opc == "6":
            mostrarUF()
        elif opc == "7":
            MostrarClima()
        else:
            print("Opcion invalida")

        print("\nPresione una tecla para continuar...")
        msvcrt.getch()


def crear_usuario():
    print("CREAR USUARIO")
    while True:
        try:
            idUsuario = int(input("Ingrese la ID del usuario: "))
        except ValueError:
            print("Error: la ID debe ser un número entero.")
            continue

        if buscarUsuario(idUsuario):
            print("La ID ingresada ya está registrada. Por favor elija otra.")
            continue
        break

    while True:
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre.replace(" ", "").isalpha():
            break
        print("Error!: El nombre no puede quedar vacio o contener numeros.")
    direccion = input("Ingrese la direccion:")

    while True:
        telefono = input("Ingrese el numero de telefono (+569XXXXXXXX): ").strip()
        if telefono.startswith("+569") and telefono[4:].isdigit() and len(telefono) == 12:
            break
        print("Error! El telefono debe tener el formato +569XXXXXXXX (8 dígitos).")

    while True:
        correo = input("Ingrese el correo: ")
        if "@" in correo and "." in correo:
            break
        print("Error! Correo invalido")

    opc = input("Seleccione rol (1=admin, 2=empleado, 3=gerente): ")

    roles = {"1": "admin", "2": "empleado", "3": "gerente"}
    if opc not in roles:
        print("Error, opción inválida")
        return

    rol = roles[opc]

    contrasena = input("Ingrese la contraseña del usuario: ")

    salario = None
    fecha_sql = None
    if rol in ("empleado", "gerente"):
        while True:
            try:
                salario = float(input("Ingrese el salario del empleado: "))
                break
            except ValueError:
                print("Error: el salario debe ser un número.")

        while True:
            fecha_inicio = input("Ingrese la fecha de inicio de contrato (dd/mm/yyyy): ")
            try:
                fecha_sql = datetime.strptime(fecha_inicio, "%d/%m/%Y").strftime("%Y-%m-%d")
                break
            except Exception:
                print("Error: use el formato correcto dd/mm/yyyy")

    usu = Usuario(idUsuario, nombre, direccion, telefono, correo, rol, contrasena)

    if crearUsuario(usu):
        if rol in ("empleado", "gerente"):
            emp = Empleado(
                idUsuario,
                nombre,
                direccion,
                telefono,
                correo,
                rol,
                salario,
                fecha_sql,
                contrasena,
            )
            if crearEmpleado(emp):
                print("Usuario y registro de empleado creados.")
            else:
                print("Usuario creado, pero no se pudo registrar como empleado.")
        else:
            print("Usuario creado.")
    else:
        print("Error al crear usuario")


def listar_usuarios():
    print("LISTAR USUARIOS")
    datos = listarUsuarios()
    _formatear_usuarios(datos)


def buscar_usuario():
    print("BUSCAR USUARIO")
    try:
        idUsuario = int(input("Ingrese la ID del usuario: "))
    except ValueError:
        print("Error: la ID debe ser un número entero.")
        return
    dato = buscarUsuario(idUsuario)
    if dato:
        _formatear_usuarios([dato])
    else:
        print("Usuario no existe.")


def actualizar_usuario():
    print("ACTUALIZAR USUARIO")
    try:
        idUsuario = int(input("Ingrese la ID del usuario a actualizar: "))
    except ValueError:
        print("Error: la ID debe ser un número entero.")
        return

    if not buscarUsuario(idUsuario):
        print("Usuario no existe!")
        return
    while True:
        nuevoNombre = input("Ingrese un nuevo nombre de usuario: ")
        if nuevoNombre.replace(" ", "").isalpha():
            break
        print("Error! el nombre no puede estar vacio o contener numeros")

    nuevaDireccion = input("Ingrese una nueva direccion: ")

    while True:
        nuevoTelefono = input("Ingrese un nuevo telefono (+569XXXXXXXX): ").strip()
        if nuevoTelefono.startswith("+569") and nuevoTelefono[4:].isdigit() and len(nuevoTelefono) == 12:
            break
        print("Error! El telefono debe tener el formato +569XXXXXXXX (8 dígitos).")

    while True:
        nuevoCorreo = input("Ingrese un nuevo correo: ")
        if "@" in nuevoCorreo and "." in nuevoCorreo:
            break
        print("Error!Formato de correo invalido")

    nuevoRol = input("Ingrese un nuevo rol: ")

    usu = Usuario(
        idUsuario, nuevoNombre, nuevaDireccion, nuevoTelefono, nuevoCorreo, nuevoRol, None
    )

    if actualizarUsuario(usu):
        print("Usuario actualizado con exito")
    else:
        print("Error al actualizar el usuario")


def eliminar_usuario():
    print("ELIMINAR USUARIO")
    idUsuario = int(input("Ingrese la ID del usuario a eliminar: "))
    if eliminarUsuario(idUsuario):
        print("Usuario eliminado con exito")
    else:
        print("Usuario no existe")
        



