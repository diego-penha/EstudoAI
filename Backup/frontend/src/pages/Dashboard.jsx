import { useNavigate }
from "react-router-dom";

export default function Dashboard() {

  const navigate =
    useNavigate();

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
                navigate("/simulado")
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