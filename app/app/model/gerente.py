from app.model.empleado import Empleado

class Gerente(Empleado):
    _idDepartamento = None

    def __init__(self,idEmpleado,nombre,direccion,telefono,correo,rol,salario,fechaInicio,idDepartamento):
        super().__init__(idEmpleado,nombre,direccion,telefono,correo,rol,salario,fechaInicio)
        self._idDepartamento = idDepartamento

    def getDepartamento(self):
        return self._idDepartamento

    def setDepartamento(self,idDepartamento):
        self._idDepartamento = idDepartamento

    def __str__(self):
        return f"Gerente: {self._nombre} - Departamento: {self._idDepartamento}"