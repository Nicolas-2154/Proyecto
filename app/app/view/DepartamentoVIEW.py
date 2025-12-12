from app.controller.departamentoDAO import *
from app.controller.empleadoDAO import buscarEmpleado
from app.model.departamento import Departamento
import msvcrt
import os


def menu_departamento():
    menu = """MENÚ DEPARTAMENTOS
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
        opc = input("Elija una opcion: ")
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
    while True:
        idDepartamento = int(input("Ingrese la ID del departamento: "))
        if buscarDepartamento(idDepartamento):
            print("Error: la ID ya está registrada. Ingrese otra.")
            continue
        break

    while True:
        nombre = input("Ingrese el nombre del departamento: ")
        if nombre.replace(" ", "").isalpha():
            break
        print("Error! El nombre no puede estar vacio o conetener numeros.")

    while True:
        idGerente = int(input("Ingrese la ID del gerente (0 para omitir): "))
        if idGerente == 0:
            idGerente = None
            break
        if buscarEmpleado(idGerente):
            break
        print("Error: el gerente debe existir como empleado. Intente con otra ID.")

    dep = Departamento(idDepartamento, nombre, idGerente)

    if crearDepartamento(dep):
        print("Departamento creado con exito.")
    else:
        print("Error al crear el departamento")


def listar_departamentos():
    print("LISTA DE DEPARTAMENTOS")
    datos = listarDepartamentos()
    _formatear_departamentos(datos)


def buscar_departamento():
    print("BUSCAR DEPARTAMENTO")
    idDepartamento = int(input("Ingrse el ID del departamento: "))
    dato = buscarDepartamento(idDepartamento)
    if dato:
        _formatear_departamentos([dato])
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
        if nuevonombre.replace(" ", "").isalpha():
            break
        print("Error! El nombre no puede estar vacio o tener numeros")

    while True:
        nuevoIdGerente = int(input("Ingrese un nuevo ID de gerente (0 para omitir): "))
        if nuevoIdGerente == 0:
            nuevoIdGerente = None
            break
        if buscarEmpleado(nuevoIdGerente):
            break
        print("Error: el gerente debe existir como empleado. Intente con otra ID.")

    dep = Departamento(idDepartamento, nuevonombre, nuevoIdGerente)

    if actualizarDepartamento(dep):
        print("Departamento actualizado con exito.")
    else:
        print("Error al actualizar departamento.")


def eliminar_departamento():
    print("ELIMINAR DEPARTAMENTO")
    idDepartamento = int(input("Ingrese el ID del departamento a eliminar: "))
    if eliminarDepartamento(idDepartamento):
        print("Departamento eliminado con exito.")
    else:
        print("Departamento no existe")


def _formatear_departamentos(datos):
    if not datos:
        print("No hay departamentos registrados.")
        return

    encabezados = ["ID", "Nombre", "Gerente"]
    anchos = [10, 24, 16]
    borde = "+" + "+".join("-" * (a + 2) for a in anchos) + "+"

    print(borde)
    print(
        "|"
        + "|".join(
            f" {encabezados[idx].center(anchos[idx])} "
            for idx in range(len(encabezados))
        )
        + "|"
    )
    print(borde)

    for fila in datos:
        idDepartamento, nombre, idGerente = fila[:3]
        gerente = idGerente if idGerente is not None else "Sin asignar"
        columnas = [
            str(idDepartamento).center(anchos[0]),
            str(nombre)[: anchos[1]].ljust(anchos[1]),
            str(gerente).center(anchos[2]),
        ]
        print("|" + "|".join(f" {col} " for col in columnas) + "|")
    print(borde)
  

    