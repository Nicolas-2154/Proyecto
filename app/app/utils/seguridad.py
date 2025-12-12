import hashlib, os

def generarSalt():
    return os.urandom(16).hex()

def generarHash(contraseña, salt):
    contrasena_valor = contraseña or ""
    salt_valor = salt or ""
    return hashlib.sha256((contrasena_valor + salt_valor).encode("utf-8")).hexdigest()

def verificarContrasena(contrasena, salt, hash_guardado):
    if not salt or not hash_guardado:
        return False

    hash_prueba = generarHash(contrasena or "", salt)
    return hash_prueba == hash_guardado