from app.controller.usuarioDAO import LoginUsuario
import os, msvcrt

def login():
    print("INICIO DE SESIÓN")

    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña :")

    usuario =LoginUsuario(correo,contrasena)

    if usuario:
        print(f"Bienvenido/a {usuario['nombre']}!")
        return usuario
    else:
        print("Credenciales invalidas.")
        return None