import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import JogadorList from "./components/JogadorList";

function App() {
  const [jogadorList, setJogadorList] = useState([{}]);
  const [jogadorNome, setJogadorNome] = useState("");
  const [jogadorIdade, setJogadorIdade] = useState("");
  const [jogadorTime, setJogadorTime] = useState("");
  const [jogadorId, setJogadorId] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/jogadores")
      .then((resposta) => {
        console.log(resposta.data);
        setJogadorList(resposta.data);
      })
      .catch((error) => console.log(error));
  }, []);

  const atualizaJogador = (jogador) => {
    axios
      .put(`http://127.0.0.1:8000/jogadores/${jogadorId}`, jogador)
      .then((reposta) => {
        alert("Jogador atualizado com sucesso");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const adicionaJogador = (jogador) => {
    axios
      .post("http://127.0.0.1:8000/jogadores", jogador)
      .then((resposta) => {
        alert(JSON.stringify(resposta.data));
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const adicionaAtualizaJogador = () => {
    const jogador = {
      jogador_nome: jogadorNome,
      jogador_idade: Number(jogadorIdade),
      jogador_time: jogadorTime,
    };
    if (jogadorId !== "") {
      atualizaJogador(jogador);
    } else {
      adicionaJogador(jogador);
    }
  };
  return (
    <div className="container">
      <div
        className="mt-3 justify-content-center align-items-center mx-auto"
        style={{ width: "60vw", backgroundColor: "#ffffff" }}
      >
        <h2 className="text-center text-white bg-success card mb-1">
          Gerenciamento de Jogadores
        </h2>
        <h6 className="card text-center text-white bg-success mb-2 pb-1">
          Informações de Jogador
        </h6>
        <div className="card-body text-center">
          <h5 className="card text-center text-white bg-dark mb-2 pb-1">
            Cadastro do Jogador
          </h5>
          <span className="card-text">
            <input
              onChange={(evento) => setJogadorNome(evento.target.value)}
              value={jogadorNome}
              className="mb-2 form-control"
              placeholder="Informe o Nome"
            ></input>
            <input
              onChange={(evento) => setJogadorIdade(evento.target.value)}
              value={jogadorIdade}
              className="mb-2 form-control"
              placeholder="Informe a Idade"
            ></input>
            <input
              onChange={(evento) => setJogadorTime(evento.target.value)}
              value={jogadorTime}
              className="mb-2 form-control"
              placeholder="Informe o Time"
            ></input>
            <button
              onClick={adicionaAtualizaJogador}
              className="btn btn-outline-success mb-4"
            >
              Cadastrar
            </button>
          </span>
          <h5 className="card text-center text-white bg-dark pb-1 mb-5">
            Lista de Jogadores
          </h5>
          <div>
            <JogadorList
              jogadorList={jogadorList}
              setJogadorId={setJogadorId}
              setJogadorNome={setJogadorNome}
              setJogadorIdade={setJogadorIdade}
              setJogadorTime={setJogadorTime}
            ></JogadorList>
          </div>
        </div>
        <h6 className="card text-center text-light bg-success py-1">
          &copy; CodeTI - 2026
        </h6>
      </div>
    </div>
  );
}

export default App;
