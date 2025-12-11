import requests

def obtenerUF():
        url="https://mindicador.cl/api/uf"
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return data.get("serie")[0].get("valor")
        except Exception as e:
            print("Error API UF: ",e)
            return None
    

def obtenerClimaSantiago():
    url=("https://api.open-meteo.com/v1/forecast"
        "?latitude=-33.45&longitude=-70.66"
        "&current_weather=true"
    )
    try:
        resp = requests.get(url,timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data.get("current").get("temperature_2m")
    except Exception as e:
        print("Error API clima: ",e)
        return None