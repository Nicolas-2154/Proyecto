from app.model.usuario import Usuario

class Empleado(Usuario):
    _salario = None
    _fechaInicio = None

    def __init__(self,idUsuario,nombre,direccion,telefono,correo,rol,salario,fechaInicio):
        super().__init__(idUsuario,nombre,direccion,telefono,correo,rol)
        self._salario = salario
        self._fechaInicio = fechaInicio

    def getSalario(self):
            return self._salario
    def getFechaInicio(self):
            return self._salario

    def setSalario(self,salario):
            self._salario = salario
    def setFechaInicio(self,fechaInicio):
            self._fechaInicio = fechaInicio

    def __str__(self):
            return f"Empleado: {self.getNombre()} - Salario: {self._salario}"  

