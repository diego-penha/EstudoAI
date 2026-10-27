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

<h3>
  ✅ Acertos: {resultado.acertos ?? 0}
</h3>

<h3>
  ❌ Erros: {resultado.erros ?? 0}
</h3>

<h3>
  🎯 Nota: {resultado.nota ?? 0}%
</h3>

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
