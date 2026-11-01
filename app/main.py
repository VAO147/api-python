
import requests

from fastapi import FastAPI, HTTPException
from app.weather import consultar_clima


app = FastAPI(
    title="Weather API Service",
    description="API de consulta meteorologica",
    version="1.0.0"
)


@app.get("/")
def pagina_inicial():
    return {
        "mensagem": "Weather API funcionando"
    }


@app.get("/health")
def verificar_saude():
    return {
        "status": "healthy"
    }


@app.get("/clima")
def obter_clima():
    try:
        resultado = consultar_clima()
        return resultado

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Erro ao consultar API meteorologica"
        )

    except (KeyError, ValueError, TypeError):
        raise HTTPException(
            status_code=502,
            detail="Resposta invalida da API meteorologica"
        )
