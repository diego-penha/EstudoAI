import { useNavigate } from "react-router-dom";

import api from "../services/api";

import {
  salvarQuestoes
} from "../services/simuladoStore";

export default function Dashboard() {

  const navigate = useNavigate();

  async function iniciarSimulado(
    quantidade
  ) {

    try {

      const resposta = await api.get(
        `/simulado/${quantidade}`
      );

      console.log(
  "QUESTOES RECEBIDAS:",
  resposta.data.length
);

console.log(
  resposta.data
);

      salvarQuestoes(
        resposta.data
      );

      navigate(
        "/simulado"
      );

    } catch (erro) {

      console.error(erro);

      alert(
        "Erro ao carregar simulado"
      );

    }

  }

  return (
    <div className="page">

      <div className="container">

        <h1 className="title">
          EstudoAI
        </h1>

        <p className="subtitle">
          Plataforma de estudos para certificações
        </p>

        <div className="card">

          <h2>
            AWS SAA-C03
          </h2>

          <p>
            Banco com mais de 1000 questões
          </p>

          <div className="button-group">

            <button
              className="btn"
              onClick={() =>
                iniciarSimulado(10)
              }
            >
              10 Questões
            </button>

            <button
              className="btn"
              onClick={() =>
                iniciarSimulado(20)
              }
            >
              20 Questões
            </button>

            <button
              className="btn"
              onClick={() =>
                iniciarSimulado(50)
              }
            >
              50 Questões
            </button>

            <button
              className="btn"
              onClick={() =>
                iniciarSimulado(100)
              }
            >
              100 Questões
            </button>

          </div>

        </div>

      </div>

    </div>
  );
}