import { useNavigate } from "react-router-dom";

import api from "../services/api";
import { useState } from "react";

import {
  salvarQuestoes
} from "../services/simuladoStore";


export default function Dashboard() {

  const navigate =
    useNavigate();

    const [quantidade,
      setQuantidade] =
      useState(10);

    async function iniciarSimulado() {

  try {

    const resposta =
      await api.get(
      `/simulado/${quantidade}`
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

          <p>
  Quantidade de questões
</p>

<div
  style={{
    marginTop: "15px",
    marginBottom: "20px"
  }}
>

  <label>
    <input
      type="radio"
      checked={
        quantidade === 10
      }
      onChange={() =>
        setQuantidade(10)
      }
    />
    {" "}
    10
  </label>

  {"   "}

  <label>
    <input
      type="radio"
      checked={
        quantidade === 20
      }
      onChange={() =>
        setQuantidade(20)
      }
    />
    {" "}
    20
  </label>

  {"   "}

  <label>
    <input
      type="radio"
      checked={
        quantidade === 50
      }
      onChange={() =>
        setQuantidade(50)
      }
    />
    {" "}
    50
  </label>

  {"   "}

  <label>
    <input
      type="radio"
      checked={
        quantidade === 100
      }
      onChange={() =>
        setQuantidade(100)
      }
    />
    {" "}
    100
  </label>

</div>

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