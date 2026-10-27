import { useState } from "react";

import {
  obterQuestoes
} from "../services/simuladoStore";

export default function Simulado() {

  const questoes =
    obterQuestoes();

  const [indice, setIndice] =
    useState(0);

  const [respostas,
   setRespostas] =
    useState({});

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

    alert(
      "Simulado finalizado!"
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