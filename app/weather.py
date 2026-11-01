
import requests

API_URL = "https://api.open-meteo.com/v1/forecast"


def consultar_clima():
    parametros = {
        "latitude": -18.91,
        "longitude": -48.28,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m"
        ),
        "timezone": "America/Sao_Paulo"
    }

    resposta = requests.get(
        API_URL,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    dados = resposta.json()

    clima_atual = dados["current"]

    resultado = {
        "cidade": "Uberlandia",
        "temperatura": clima_atual["temperature_2m"],
        "umidade": clima_atual["relative_humidity_2m"],
        "vento": clima_atual["wind_speed_10m"],
        "horario": clima_atual["time"]
    }

    return resultado
