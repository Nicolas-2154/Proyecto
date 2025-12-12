import os
import msvcrt
from app.view.UsuarioVIEW import *
from app.view.apiVIEW import MostrarClima, mostrarUF
from app.view.exportacionVIEW import *


def _mostrar_menu(menu_title, opciones):
    barra = "=" * 50
    print(barra)
    print(f"{menu_title:^50}")
    print(barra)
    for numero, texto in opciones:
        print(f" {numero}. {texto}")
    print(barra)


def menu_administrador():
    opciones = [
        ("1", "Crear Usuario"),
        ("2", "Listar Usuarios"),
        ("3", "Buscar Usuario"),
        ("4", "Actualizar Usuario"),
        ("5", "Eliminar Usuario"),
        ("6", "Exportar datos"),
        ("7", "Mostrar UF"),
        ("8", "Mostrar Clima"),
        ("0", "Cerrar sesión"),
    ]

    while True:
        os.system("cls")
        _mostrar_menu("MENÚ ADMINISTRADOR", opciones)
        opc = input("Elija una opcion: ")
        os.system("cls")

        if opc == "0":
            print("Cerrando sesion")
            msvcrt.getch()
            break
        elif opc == "1":
            crear_usuario()
        elif opc == "2":
            listar_usuarios()
        elif opc == "3":
            buscar_usuario()
        elif opc == "4":
            actualizar_usuario()
        elif opc == "5":
            eliminar_usuario()
        elif opc == "6":
            menu_exportacion()
        elif opc == "7":
            mostrarUF()
        elif opc == "8":
            MostrarClima()
        else:
            print("Opcion invalida.")

        print("\nPresione una tecla para continuar...")
        msvcrt.getch()
        