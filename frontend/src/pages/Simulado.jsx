import { useState } from "react";

import {
  obterQuestoes
} from "../services/simuladoStore";

export default function Simulado() {

  const questoes =
    obterQuestoes();

  const [indice, setIndice] =
    useState(0);

  const [respostaSelecionada,
    setRespostaSelecionada] =
    useState("");

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
    questoes[indice];

  function proximaQuestao() {

    if (
      indice <
      questoes.length - 1
    ) {

      setIndice(
       (atual) => atual + 1
      );

      setRespostaSelecionada(
        ""
      );

    }

  }

  return (
    <div className="page">

      <div className="container">

        <div className="card">

          <h2>
             Questão {indice + 1}
             de
             {questoes.length}
          </h2>

          <p>
            {questao.enunciado}
          </p>

          
          <hr />

          {
            questao.alternativas.map(
              (alternativa) => (

                <div
                  key={
  `${questao.id}-${alternativa.codigo}`
}

                  style={{
                    marginBottom:
                      "12px"
                  }}
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
                      {alternativa.codigo}
                    </strong>

                    {" - "}

                   {
  alternativa.texto
    .replace(/^[A-D]\./, "")
    .replace(/\t/g, " ")
}

                  </label>

                </div>

              )
            )
          }

          <br />

          <button
            className="btn"
            onClick={
              proximaQuestao
            }
          >
            Próxima
          </button>

        </div>

      </div>

    </div>
  );
}