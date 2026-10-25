import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Simulado from "./pages/Simulado";
import Resultado from "./pages/Resultado";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Dashboard />}
        />

        <Route
          path="/simulado"
          element={<Simulado />}
        />

        <Route
          path="/resultado"
          element={<Resultado />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;