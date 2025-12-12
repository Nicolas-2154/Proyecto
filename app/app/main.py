import os
from app.conexion.inicializacionBD import inicializar_bd
from app.controller.usuarioDAO import *
from app.view.administradorVIEW import *
from app.view.loginVIEW import *
from app.view.UsuarioVIEW import *
from app.model.usuario import *

mensaje_admin = inicializar_bd()

def inicio():
    os.system("cls" if os.name == "nt" else "clear")

    if mensaje_admin:
        print(mensaje_admin)

    while True:
        user = login()
        if user == "salir":
            print("Saliendo del programa. Hasta pronto.")
            break
        if user:
            if user["rol"] == "admin":
                menu_administrador()
            else:
                menu_usuario()

inicio()