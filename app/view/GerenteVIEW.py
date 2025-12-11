from app.controller.gerenteDAO import *
from app.model.gerente import Gerente
import msvcrt,os

def menu_gerente():
    menu ="""MENÚ GERENTES
    1. Crear Gerente
    2. Listar Gerente
    3. Buscar Gerente
    4. Actualizar Gerente
    5. Eliminar Gerente
    0. Volver
    """

    while True:
        os.system('cls')
        print(menu)
        opc = input("Elija una opcion")
        os.system('cls')

        if opc == "0":
            break
        elif opc == "1":
            crear_gerente()
        elif opc == "2":
            listar_gerentes()
        elif opc == "3":
            buscar_gerente()
        elif opc == "4":
            actualizar_gerente()
        elif opc == "5":
            eliminar_gerente()
        else:
            print("Opcion incorrecta")
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()

def crear_gerente():
    print("CREAR GERENTE")
    idUsuario = int(input("Ingrese la ID del usuario: "))
    idDepartamento = int(input("Ingrese la ID del departamento: "))

    ger = Gerente(idUsuario,None,None,None,None,"gerente",None,None,idDepartamento)

    if crearGerente(ger):
        print("Gerente creado")
    else:
        print("Error al crear gerente")
    
def listar_gerentes():
    print("LISTAR GERENTES")
    datos = listarGerentes()
    if datos:
        for g in datos:
            print(g)

def buscar_gerente():
    print("BUSCAR GERENTE")
    idUsuario=int(input("Ingrese la ID del usuario: "))

    dato = buscarGerente(idUsuario)
    if dato:
        print(dato)
    else:
        print("Gerente no existe")

def actualizar_gerente():
    print("ACTUALIZAR GERENTE")
    idUsuario = int(input("Ingrese el ID del usuario:"))
    
    if not buscarGerente(idUsuario):
        print("Gerente no existe!")
        return
    
    nuevoDepartamento =int(input("Ingrese nuevo ID departamento: "))
    ger = Gerente(idUsuario,None,None,None,None,'Gerente',None,None,nuevoDepartamento)


    if actualizarGerente(ger):
        print("Gerente actualizado con exito")
    else:
        print("Error al actualizar a gerente")

def eliminar_gerente():
    print("ELIMINAR GERENTE")
    idUsuario = int=input("Ingrese la ID del usuario a eliminar: ")
    if eliminarGerente(idUsuario):
        print("Gerente eliminado con exito")
    else:
        print("Gerente no existe")