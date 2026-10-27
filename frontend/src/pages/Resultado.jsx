import { useNavigate } from "react-router-dom";

import {
  obterResultado
} from "../services/resultadoStore";

export default function Resultado() {

  const resultado =
    obterResultado();

  const navigate =
    useNavigate();

  return (
    <div className="page">

      <div className="container">

        <div className="card">

          <h1>
            Resultado
          </h1>

          <p>
            Questões respondidas:
            {" "}
            {
              resultado.respondidas || 0
            }
          </p>

          <br />

          <button
            className="btn"
            onClick={() =>
              navigate("/")
            }
          >
            🔄 Novo Simulado
          </button>

        </div>

      </div>

    </div>
  );

}