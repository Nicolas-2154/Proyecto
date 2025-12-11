from app.model.usuario import Usuario
from app.controller.usuarioDAO import * 
from app.view.DepartamentoVIEW import *
from app.view.EmpleadoVIEW import *
from app.view.ProyectoVIEW import *
from app.view.RegistroTiempoVIEW import *
from app.view.apiVIEW import *
from app.view.exportacionVIEW import *
from datetime import datetime
import msvcrt, os

def menu_usuario():
    menu ="""MENÚ USUARIOS
    1. Gestionar Empleados
    2. Gestionar Departamentos
    3. Gestionar Proyectos
    4. Gestionar Registros de Tiempo
    5. Exportar datos
    6. Mostrar UF
    7. Mostrar Clima
    0. Cerrar sesión
    """

    while True:
        os.system('cls')
        print(menu)
        opc = input("Elija una opcion")
        os.system('cls')

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
    idUsuario = int(input("Ingrese la ID del usuario: "))
    while True:
        nombre =input("Ingrese el nombre del empleado: ")
        if nombre.replace(" ","").isalpha():
            break
        print("Error!: El nombre no puede quedar vacio o contener numeros.")
    direccion = input("Ingrese la direccion:")

    while True:
        telefono =input("Ingrese el numero de telefono: ")
        if telefono.isdigit() and 9 <= len(telefono) <=12:
            break
        print("Error! Numero de telefono invalido.")

    while True:
        correo = input("Ingrese el correo: ")
        if "@" in correo and "." in correo:
            break
        print("Error! Correo invalido")

    opc = input("Seleccione rol (1=admin, 2=empleado, 3=gerente): ")

    if opc == "1":
        rol = "admin"
    elif opc == "2":
        rol = "empleado"
    elif opc == "3":
        rol = "gerente"
    else:
        print("Error, opción inválida")
        return


    contraseña = input("Ingrese la contraseña del usuario: ")

    usu = Usuario(idUsuario,nombre,direccion,telefono,correo,rol,contraseña)

    if crearUsuario(usu):
        print("Usuario creado.")
    else:
        print("Error al crear usuario")

def listar_usuarios():
    print("LISTAR USUARIOS")
    datos = listarUsuarios()
    if datos:
        for d in datos:
            print(d)

def buscar_usuario():
    print("BUSCAR USUARIO")
    idUsuario = int(input("Ingrese la ID del usuario"))
    dato = buscarUsuario(idUsuario)
    if dato:
        print(dato)
    else:
        print("Usuario no existe.")

def actualizar_usuario():
    print("ACTUALIZAR USUARIO")
    idUsuario = int(input("Ingrese la ID del usuario a actualizar: "))
    if not buscarUsuario(idUsuario):
        print("Usuario no existe!")
        return
    while True:
        nuevoNombre = input("Ingrese un nuevo nombre de usuario: ")
        if nuevoNombre.replace(" ","").isalpha():
            break
        print("Error! el nombre no puede estar vacio o contener numeros")

    nuevaDireccion = input("Ingrese una nueva direccion: ")

    while True:
        nuevoTelefono = input("Ingrese un nuevo telefono: ")
        if nuevoTelefono.isdigit() and 9 <=len(nuevoTelefono) <=12:
            break
        print("Error! Numero de telefono invalido")

    while True:
        nuevoCorreo = input("Ingrese un nuevo correo: ")
        if "@" and "." in nuevoCorreo:
            break
        print("Error!Formato de correo invalido")
        nuevoRol = input("Ingrese un nuevo rol")


        usu =Usuario(idUsuario,nuevoNombre,nuevaDireccion,nuevoTelefono,nuevoCorreo,nuevoRol,None)

        if actualizarUsuario(usu):
            print("Usuario actualizado con exito")
        else:
            print("Error al actualizar el usuario")

def eliminar_usuario():
    print("ELIMINAR USUARIO")
    idUsuario = int(input("Ingrese la ID del usuario a eliminar: "))
    if eliminarUsuario(idUsuario):
        print("Usuario eliminado con exito")
        



