class Proyecto:
    __idProyecto = None
    __nombre = None
    __descripcion = None
    __fechaInicio = None

    def __init__(self,idProyecto,nombre,descripcion,fechaInicio):
        self.__idProyecto = idProyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechaInicio = fechaInicio
    
    def getID(self):
        return self.__idProyecto
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def getFechaInicio(self):
        return self.__fechaInicio

    def setNombre(self,nombre):
        self.__nombre = nombre
    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion
    def setFechaInicio(self,fechaInicio):
        self.__fechaInicio = fechaInicio

    def __str__(self):
        return f"Protecto: {self.__nombre} - Inicio: {self.__fechaInicio}"