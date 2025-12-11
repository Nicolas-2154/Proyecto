from app.model.departamento import Departamento
from app.controller.departamentoDAO import *
import msvcrt, os

def menu_departamento():
    menu ="""MENÚ DEPARTAMENTOS
    1. Crear Departamento
    2. Listar Departamento
    3. Buscar Departamento
    4. Actualizar Departamento
    5. Eliminar Departamento
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
            crear_departamento()
        elif opc == "2":
            listar_departamentos()
        elif opc == "3":
            buscar_departamento()
        elif opc == "4":
            actualizar_departamento()
        elif opc == "5":
            eliminar_departamento()
        else:
            print("Opcion incorrecta")
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()

def crear_departamento():
    print("CREAR DEPARTAMENTO.")
    idDepartamento = int(input("Ingrese la ID del departamento: "))

    while True:
        nombre = input("Ingrese el nombre del departamento: ")
        if nombre.replace(" ","").isalpha():
            break
        print("Error! El nombre no puede estar vacio o conetener numeros.")

    idGerente = int(input("Ingrese la ID del gerente: "))

    if idGerente == 0:
        idGerente = None

    dep = Departamento(idDepartamento,nombre,idGerente)
    
    if crearDepartamento(dep):
        print("Departamento creado con exito.")
    else:
        print("Error al crear el departamento")


def listar_departamentos():
    print("LISTA DE DEPARTAMENTOS")
    datos = listarDepartamentos()
    if datos:
        for d in datos:
            print(d)


def buscar_departamento():
    print("BUSCAR DEPARTAMENTO")
    idDepartamento = int(input("Ingrse el ID del departamento: "))
    dato = buscarDepartamento(idDepartamento)
    if dato:
        print(dato)
    else:
        print("Departamento no existe")


def actualizar_departamento():
    print("ACTUALIZAR DEPARTAMENTO")
    idDepartamento = int(input("Ingrese la ID del departamento a actualizar: "))
    if not buscarDepartamento(idDepartamento):
        print("Error! Departamento no existe")
        return
    
    while True:
        nuevonombre = input("Ingrese el nuevo nombre del departamento: ")
        if nuevonombre.replace(" ","").isalpha():
             break
        print("Error! El nombre no puede estar vacio o tener numeros")

    nuevoIdGerente = int(input("Ingrese un nuevo ID de gerente: "))

    if nuevoIdGerente == 0:
            nuevoIdGerente = None

    dep =Departamento(idDepartamento,nuevonombre,nuevoIdGerente)
        
    if actualizarDepartamento(dep):
            print("Departamento actualizado con exito.")
    else:
            print("Error al actualizar departamento.")


def eliminar_departamento():
    print("ELIMINAR DEPARTAMENTO")
    idDepartamento=int(input("Ingrese el ID del departamento a eliminar: "))
    if eliminarDepartamento(idDepartamento):
        print("Departamento eliminado con exito.")
    else:
        print("Departamento no existe")
  

    