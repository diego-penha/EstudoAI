import { useNavigate } from "react-router-dom";

import api from "../services/api";

import {
  salvarQuestoes
} from "../services/simuladoStore";


export default function Dashboard() {

  const navigate =
    useNavigate();

    async function iniciarSimulado() {

  try {

    const resposta =
      await api.get(
        "/simulado/10"
      );

    salvarQuestoes(
      resposta.data
    );

    navigate(
      "/simulado"
    );

  } catch (erro) {

    console.error(
      erro
    );

    alert(
      "Erro ao carregar questões"
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
  onClick={
    iniciarSimulado
  }
>
  Iniciar Simulado
</button>

          </div>

        </div>

      </div>

    </div>
  );
}