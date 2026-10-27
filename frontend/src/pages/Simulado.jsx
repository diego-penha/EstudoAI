import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  obterQuestoes
} from "../services/simuladoStore";

import {
  salvarResultado
} from "../services/resultadoStore";


export default function Simulado() {

  const questoes =
    obterQuestoes();

  const [indice, setIndice] =
    useState(0);

  const [respostas,
   setRespostas] =
    useState({});

    const navigate =
  useNavigate();

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

  } else {

  console.log(
    "RESPOSTAS:",
    respostas
  );

  console.log(
    "QUANTIDADE:",
    Object.keys(
      respostas
    ).length
  );

  salvarResultado({

    respondidas:
      Object.keys(
        respostas
      ).length

  });

  navigate(
    "/resultado"
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
  respostas[
    questao.id
  ] ===
  alternativa.codigo
}


                      onChange={() =>
  setRespostas({

    ...respostas,

    [questao.id]:
      alternativa.codigo

  })
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
  {
    indice <
    questoes.length - 1

      ? "Próxima"

      : "Finalizar Simulado"
  }
</button>


        </div>

      </div>

    </div>
  );
}