import { useState } from "react";

import {
  obterQuestoes
} from "../services/simuladoStore";

export default function Simulado() {

  const questoes =
    obterQuestoes();

  if (
    questoes.length === 0
  ) {

    return (
      <div className="page">

        <div className="container">

          <div className="card">

            <h1>
              Nenhum simulado carregado
            </h1>

          </div>

        </div>

      </div>
    );

  }

  const questao =
    questoes[0];

    const [respostaSelecionada,
       setRespostaSelecionada] =
       useState("");

  return (
    <div className="page">

      <div className="container">

        <div className="card">

          <h2>
            Questão 1 de {questoes.length}
          </h2>

          <p>
            {questao.enunciado}
          </p>

          <hr />

          {
            questao.alternativas.map(
              (
                alternativa
              ) => (

                <div
  key={
    alternativa.codigo
  }
>

  <label>

    <input
      type="radio"
      name="resposta"
      value={
        alternativa.codigo
      }

      checked={
        respostaSelecionada ===
        alternativa.codigo
      }

      onChange={() =>
        setRespostaSelecionada(
          alternativa.codigo
        )
      }
    />

    {" "}

    <strong>
      {
        alternativa.codigo
      }
    </strong>

    {" - "}

    {
      alternativa.texto
    }

  </label>

</div>

              )
            )
          }

        </div>

      </div>

    </div>
  );

}