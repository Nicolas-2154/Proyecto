from app.model.empleado import Empleado

class Administrador(Empleado):
    __privilegios = None

    def __init__(self,idEmpleado,nombre,direccion,telefono,correo,salario,fechaInicio,privilegios,rol):
        super().__init__(idEmpleado,nombre,direccion,telefono,correo,salario,fechaInicio,rol)
        self.__privilegios = privilegios

    def getPrivilegios(self):
        return self.__privilegios

    def setPrivilegios(self,privilegios):
        self.__privilegios = privilegios

    def __str__(self):
        return f"Administrador: {self._nombre} - Privilegios: {self.__privilegios}"    