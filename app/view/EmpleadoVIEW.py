from app.controller.empleadoDAO import *
from app.model.empleado import Empleado
from datetime import datetime
import msvcrt,os

def menu_empleado():
    menu ="""MENÚ EMPLEADOS
    1. Crear Empleado
    2. Listar Empleado
    3. Buscar Usuario
    4. Actualizar Empleado
    5. Eliminar Empleado
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
            crear_empleado()
        elif opc == "2":
            listar_empleados()
        elif opc == "3":
            buscar_empleado()
        elif opc == "4":
            actualizar_empleado()
        elif opc == "5":
            eliminar_empleado()
        else:
            print("Opcion incorrecta")
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()

def crear_empleado():
    print("CREAR EMPLEADO.")
    idUsuario = int(input("Ingrese la ID del empleado: "))
    while True:
        nombre =input("Ingrese el nombre del empleado: ")
        if nombre.replace(" ","").isalpha():
            break
        print("Error!: El nombre no puede quedar vacio o contener numeros.")

    direccion = input("Ingrese la direccion: ")
    
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

    salario =float(input("Ingrese el salario del empleado: "))

    while True:
        fechaInicio = input("Ingrese la fecha de inicio de contrato: (dd/mm/yyyy) ")
        try:
            fecha_sql = datetime.strptime(fechaInicio,"%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except:
            print("Error: Por favor use el formato correcto dd/mm/yyyy")

    rol =input("Ingrese el rol del empleado")

    emp =Empleado(idUsuario,nombre,direccion,telefono,correo,salario,fechaInicio,rol)

    if crearEmpleado(emp):
        print("Empleado creado.")
    else:
        print("Error al crear empleado.")

def listar_empleados():
    print("LISTAR EMPLEADOS.")
    datos = listarEmpleados()
    if datos:
        for e in datos:
            print(e)

def buscar_empleado():
    print("BUSCAR EMPLEADOS.")
    idEmp = int(input("Ingrese la ID del empleado: "))
    dato = buscarEmpleado(idEmp)
    if dato:
        print(dato)
    else:
        print("Empleado no existe.")


def actualizar_empleado():
    print("ACTUALIZAR EMPLEADO.")
    idEmp = int(input("Ingrese la ID del empleado a actualizar: "))
    if not buscarEmpleado(idEmp):
        print("Empleado no existe")
        return
    
    while True:
        nuevoNombre = input("Ingrese el nuevo nombre del empleado: ")
        if nuevoNombre.replace(" ","").isalpha():
            break
        print("Error! Nombre invalido")

        nuevaDireccion = input("Ingrese la nueva direccion: ")

        while True:
            nuevoTelefono = input("Ingrese el nuevo telefono: ")
            if nuevoTelefono.isdigit() and 8 <= len(nuevoTelefono) <= 12:
                break
            print("Error! Telefono invalido")
        
        while True:
            nuevoCorreo = input("Ingrese el nuevo correo: ")
            if "@" and "." in nuevoCorreo:
                break
            print("Error! Formato de correo invalido")

        nuevoRol="Empleado"

        nuevoSalario = float(input("Ingrese el nuevo salario: "))

        while True:
            nuevaFechaInicio = input("Ingresa una nueva fecha de inicio de contrato: ")
            try:
                fecha_sql = datetime.strptime(nuevaFechaInicio,"%d/%m/%Y").strftime("%Y-%m-%d")
                break
            except:
                print("Error! Por favor use el formato correcto dd/mm/yyyy")

        emp = Empleado(idEmp,nuevoNombre,nuevaDireccion,nuevoTelefono,nuevoCorreo,nuevoSalario,nuevaFechaInicio,nuevoRol)

        if actualizarEmpleado(emp):
            print("Empleado actualizado con exito.")
        else:
            print("Error al actualizar al empleado.")


def eliminar_empleado():
    print("ELIMINAR EMPLEADO")
    idEmp = int(input("Ingrese la ID del empleado a eliminar: "))
    if eliminarEmpleado(idEmp):
        print("Empleado eliminado con exito")
    else:
        print("Empleado no existe.")