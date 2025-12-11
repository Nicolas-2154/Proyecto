from app.utils.api_helper import *

def mostrarUF():
    print("VALOR DE LA UF")
    uf = obtenerUF()
    if uf is not None:
        print(f"UF actual: {uf} CLP")
    else:
        print("No se pudo obtener el valor de la UF.")


def MostrarClima():
    print("CLIMA ACTUAL SANTIAGO")
    clima = obtenerClimaSantiago()
    if clima:
        temp = clima.get("temperature")
        viento = clima.get("windspeed")
        direccion = clima.get("winddirection")
        hora = clima.get("time")

        print(f"Hora dato   : {hora}")
        print(f"Temperatura : {temp} C°")
        print(f"Viento      : {viento} KM/H")
        print(f"Dirección viento: {direccion}°")
    else:
        print("No se pudo obtener el clima de Santiago")