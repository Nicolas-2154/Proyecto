class Departamento:
    __idDepartamento = None
    __nombre = None
    __idGerente = None

    def __init__(self,idDepartamento,nombre,idGerente):
        self.__idDepartamento = idDepartamento
        self.__nombre = nombre
        self.__idGerente = idGerente

    def getID(self):
        return self.__idDepartamento
    def getNombre(self):
        return self.__nombre
    def getIdGerente(self):
        return self.__idGerente

    def setID(self,idDepartamento):
        self.__idDepartamento = idDepartamento
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setIdGerente(self,idGerente):
        self.__idGerente = idGerente

    def __str__(self):
        return f"Departamento: {self.__nombre} - ID Gerente: {self.__idGerente}"   
