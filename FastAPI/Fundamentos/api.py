from typing import Optional, TypedDict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Jogador(BaseModel):
    nome: str
    idade: int
    time: str


class AtuaizaJogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None


class JogadorDB(TypedDict):
    nome: str
    idade: int
    time: str


jogadores: dict[int, JogadorDB] = {
    1: {"nome": "Fulano", "idade": 22, "time": "Palmeiras"},
    2: {"nome": "Gustavo", "idade": 12, "time": "Flamengo"},
}


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
    jogadores[jogador_id] = {
        "nome": jogador.nome,
        "idade": jogador.idade,
        "time": jogador.time,
    }
    return jogadores[jogador_id]


@app.delete("/exclusao-jogador/{jogador_id}")
def exclui_jogador(jogador_id: int):
    if jogador_id not in jogadores:
        return {"Erro": "Jogador não existe"}
    del jogadores[jogador_id]
    return {"Mensagem": "Jogador excluido com sucesso"}


@app.put("/atualiza-jogador/{jogador_id}")
def atualiza_jogador(jogador_id: int, jogador: AtuaizaJogador):
    if jogador_id not in jogadores:
        return {"Erro": "Jogador não existe"}
    if jogador.nome is not None:
        jogadores[jogador_id]["nome"] = jogador.nome
    if jogador.idade is not None:
        jogadores[jogador_id]["idade"] = jogador.idade
    if jogador.time is not None:
        jogadores[jogador_id]["time"] = jogador.time
    return jogadores[jogador_id]
