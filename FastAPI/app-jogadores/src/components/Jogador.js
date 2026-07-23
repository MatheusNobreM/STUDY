import React from "react";
import axios from "axios";

function Jogador(props) {
  const excluijogador = (jogadorId) => {
    axios
      .delete(`http://127.0.0.1:8000/jogadores/${jogadorId}`)
      .then((resposta) => {
        alert("Jogador removido com sucesso" + resposta.data);
      });
  };

  const editarJogador = (jogador) => {
    props.setJogadorId(jogador.id);
    props.setJogadorNome(jogador.nome);
    props.setJogadorIdade(jogador.idade);
    props.setJogadorTime(jogador.time);
  };
  return (
    <div>
      <p>
        <span className="fw-bold">
          {props.jogador.nome} - {props.jogador.idade} - {props.jogador.time}
        </span>
        <button
          onClick={() => editarJogador(props.jogador)}
          className="btn btn-sn"
        >
          <span className="badge rounded-pill bg-info"> Editar</span>
        </button>
        <button
          onClick={() => excluijogador(props.jogador.id)}
          className="btn btn-sn"
        >
          <span className="badge rounded-pill bg-danger"> X</span>
        </button>
      </p>
    </div>
  );
}

export default Jogador;
