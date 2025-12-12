from app.controller.usuarioDAO import LoginUsuario
import os, msvcrt


def login():
    while True:
        print("INICIO DE SESIÓN")
        print("1. Ingresar")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return "salir"
        if opcion != "1":
            print("Opción inválida. Intente nuevamente.\n")
            continue

        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña :")

        usuario = LoginUsuario(correo, contrasena)

        if usuario:
            print(f"Bienvenido/a {usuario['nombre']}!")
            return usuario
        else:
            print("Credenciales inválidas. Presione una tecla para reintentar o 0 para salir.")
            tecla = msvcrt.getch().decode("latin-1", errors="ignore") if msvcrt else ""
            if tecla == "0":
                return "salir"
            os.system("cls" if os.name == "nt" else "clear")