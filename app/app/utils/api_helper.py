import requests
from datetime import datetime


def obtenerUF():
    url = "https://mindicador.cl/api/uf"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        serie = data.get("serie")
        if isinstance(serie, list) and serie:
            return serie[0].get("valor")
        print("Respuesta UF sin datos de serie válidos")
    except Exception as e:
        print("Error API UF: ", e)
    return None


def obtenerClimaSantiago():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-33.45&longitude=-70.66"
        "&current_weather=true"
    )
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        clima = data.get("current_weather")
        if clima:
            return {
                "temperature": clima.get("temperature"),
                "windspeed": clima.get("windspeed"),
                "winddirection": clima.get("winddirection"),
                "time": clima.get("time"),
                "current_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        print("Respuesta clima sin current_weather")
    except Exception as e:
        print("Error API clima: ", e)
    return None