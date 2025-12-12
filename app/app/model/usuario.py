class Usuario:
    _idUsuario = None
    _nombre = None
    _direccion = None
    _telefono = None
    _correo = None
    _rol = None
    _contrasena = None

    def __init__(self, idUsuario, nombre, direccion, telefono, correo, rol, contrasena=None):
        self._idUsuario = idUsuario
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._rol = rol
        self._contrasena = contrasena

    def getID(self):
        return self._idUsuario

    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono

    def getCorreo(self):
        return self._correo

    def getRol(self):
        return self._rol

    def getContrasena(self):
        return self._contrasena

    # alias con tilde para compatibilidad
    def getContraseña(self):  # noqa: N802
        return self.getContrasena()

    def setID(self, idUsuario):
        self._idUsuario = idUsuario

    def setNombre(self, nombre):
        self._nombre = nombre

    def setDireccion(self, direccion):
        self._direccion = direccion

    def setTelefono(self, telefono):
        self._telefono = telefono

    def setCorreo(self, correo):
        self._correo = correo

    def setRol(self, rol):
        self._rol = rol

    def setContrasena(self, contrasena):
        self._contrasena = contrasena

    def setContraseña(self, contrasena):  # noqa: N802
        self.setContrasena(contrasena)

    def __str__(self):
        return f"{self._idUsuario} - {self._nombre} - ({self._correo}) - ({self._rol})"
            



