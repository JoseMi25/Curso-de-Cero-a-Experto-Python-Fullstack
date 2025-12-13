import { BrowserRouter, Route, Routes } from "react-router-dom";
import ListadoLibros from "./libros/ListadoLibros";
import Navegacion from "./componentes/Navegacion";
import AgregarLibro from "./libros/AgregarLibro";
import EditarLibro from "./libros/EditarLibro";

function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Navegacion />
        
        <div className="container mt-5">
          <Routes>
            <Route exact path="/" element={<ListadoLibros/>} />
            <Route exact path="/agregar" element={<AgregarLibro/>} />
            <Route exact path="/editar/:id" element={<EditarLibro/>} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  )
}

export default App