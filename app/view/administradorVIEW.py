import os, msvcrt
from app.view.UsuarioVIEW import * 
from app.view.exportacionVIEW import * 

def menu_administrador():
    menu="""MENU ADMINISTRADOR
1. Crear Usuario
2. Listar Usuarios
3. Buscar Usuario
4. Actualizar Usuario
5. Eliminar Usuario
6. Exportar usuarios a PDF/Excel
0. Cerrar sesión"""

    while True:
        os.system('cls')
        print(menu)
        opc = input("Elija una opcion: ")
        os.system('cls')

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
            exportar_usuarios()
        else:
            print("Opcion invalida.")

        print("\nPresione una tecla para continuar...")
        msvcrt.getch()