import { BrowserRouter, Route, Routes } from "react-router-dom";
import ListadoEmpleados from "./empleados/ListadoEmpleados";
import Navegacion from "./plantilla/Navegacion";
import AgregarEmpleado from "./empleados/AgregarEmpleado";
import EditarEmpleado from "./empleados/EditarEmpleado";
import Footer from "./plantilla/Footer";

function App() {
  return (
    <div className="d-flex flex-column min-vh-100">
      <BrowserRouter>
        <Navegacion />
      
        <div className="container flex-grow-1">
            <Routes>
            <Route exact path="/" element={<ListadoEmpleados/>} />
            <Route exact path="/agregar" element={<AgregarEmpleado/>} />
            <Route exact path="/editar/:id" element={<EditarEmpleado/>} />
            </Routes>
        </div>

        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;