import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
// Importamos la función de la API
import { crearLibro } from '../api/libros';

export default function AgregarLibro() {

    // Hook para redireccionar
    let navegacion = useNavigate();

    // Estado inicial del libro
    const [libro, setLibro] = useState({
        titulo: "",
        autor: "",
        rating: ""
    });

    const { titulo, autor, rating } = libro;

    // Función para actualizar el estado cuando escribimos en los inputs
    const onInputChange = (e) => {
        setLibro({ ...libro, [e.target.name]: e.target.value });
    }

    // Función para enviar el formulario
    const onSubmit = async (e) => {
        e.preventDefault();
        // Llamada a la API
        await crearLibro(libro);
        // Redireccionar al inicio
        navegacion('/');
    }

    return (
        <div className='container'>
            <div className='row'>
                <div className='col-md-6 offset-md-3'>
                    <h3 className='text-center text-warning mb-4'>
                        <i className="bi bi-plus-circle-fill me-2"></i>
                        Agregar Libro
                    </h3>

                    
                    <form onSubmit={(e) => onSubmit(e)}>
                        <div className="mb-3">
                            <label htmlFor="titulo" className="form-label">Título</label>
                            
                            <input type="text" className="form-control" id="titulo" name="titulo" 
                                required={true} value={titulo} onChange={(e) => onInputChange(e)}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="autor" className="form-label">Autor</label>
                            <input type="text" className="form-control" id="autor" name="autor" 
                                required={true} value={autor} onChange={(e) => onInputChange(e)}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="rating" className="form-label">Rating (1-5)</label>
                            <input type="number" className="form-control" id="rating" name="rating" min="1" max="5" 
                                required={true} value={rating} onChange={(e) => onInputChange(e)}
                            />
                        </div>

                        <div className='text-center'>
                            <button type="submit" className="btn btn-warning me-3">Guardar</button>
                            <Link to="/" className="btn btn-danger">Cancelar</Link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}