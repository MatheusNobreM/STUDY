from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

jogadores = {
    1: {"nome": "Fulano", "idade": 22, "time": "Palmeiras"},
    2: {"nome": "Gustavo", "idade": 12, "time": "Flamengo"},
}


class Jogador(BaseModel):
    nome: str
    idade: int
    time: str


@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador: int):
    return jogadores[id_jogador]


@app.get("/get-jogador-time")
def get_jogador_time(time: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado"}


# get-jogador/1 - Path Parameter

# get-jogador/?id=1 - Query Parameter


@app.get("/")
def inicio():
    return jogadores


@app.post("/cadastra-jogador/{jogador_id}")
def cadastr_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {"Erro": "Jogador já existe"}
    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]
