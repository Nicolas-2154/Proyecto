import hashlib, os

def generarSalt():
    return os.urandom(16).hex()

def generarHash(contraseña, salt):
    return hashlib.sha256((contraseña + salt).encode("utf-8")).hexdigest()

def verificarContrasena(contrasena,salt,hash_guardado):
    hash_prueba = generarHash(contrasena,salt)
    return hash_prueba == hash_guardado
