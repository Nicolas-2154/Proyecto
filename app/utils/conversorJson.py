from app.utils.serializacion import exportar_json,importar_json

class ConversorJSON:
    @staticmethod
    def cargar(nombre_archivo):
        return importar_json(nombre_archivo)
    @staticmethod
    def guardar(nombre_archivo,datos):
        return exportar_json(nombre_archivo, datos)