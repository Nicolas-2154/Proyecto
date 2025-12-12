class RegistroTiempo:
    __idRegistro = None
    __fecha = None
    __horas = None
    __descripcion = None
    __idEmpleado = None
    __idProyecto = None

    def __init__(self,idRegistro,fecha,horas,descripcion,idEmpleado,idProyecto):
        self.__idRegistro = idRegistro
        self.__fecha = fecha
        self.__horas = horas
        self.__descripcion = descripcion
        self.__idEmpleado = idEmpleado
        self.__idProyecto = idProyecto

    def getID(self):
            return self.__idRegistro
    def getFecha(self):
            return self.__fecha
    def getHoras(self):
            return self.__horas
    def getDescripcion(self):
            return self.__descripcion
    def getIdEmpleado(self):
            return self.__idEmpleado
    def getIdProyecto(self):
            return self.__idProyecto

    def setFecha(self,fecha):
            self.__fecha = fecha
    def setHoras(self,horas):
            self.__horas = horas
    def setDescripcion(self,descripcion):
            self.__descripcion = descripcion
    def setIdEmpleado(self,idEmpleado):
            self.__idEmpleado = idEmpleado
    def setIdProyecto(self,idProyecto):
            self.__idProyecto = idProyecto

    def __str__(self):
            return f"{self.__fecha} - {self.__horas} - Empleado: {self.__idEmpleado} - Proyecto: {self.__idProyecto}"    