from app.conexion.inicializacionBD import inicializar_bd
from app.controller.usuarioDAO import *
from app.view.administradorVIEW import *
from app.view.loginVIEW import *
from app.view.UsuarioVIEW import *
from app.model.usuario import *

inicializar_bd()

def inicio():
    while True:
        user = login()
        if user:
            if user["rol"] == "admin":
                menu_administrador()
            else:
                menu_usuario()

inicio()
