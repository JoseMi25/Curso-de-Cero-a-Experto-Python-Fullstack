import React, { useEffect, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { obtenerLibroPorId, actualizarLibro } from '../api/libros';

export default function EditarLibro() {

    let navegacion = useNavigate();
    const { id } = useParams();

    const [libro, setLibro] = useState({
        titulo: "",
        autor: "",
        rating: ""
    });

    const { titulo, autor, rating } = libro;

    useEffect(() => {
        cargarLibro();
    }, [])

    const cargarLibro = async () => {
        const datos = await obtenerLibroPorId(id);
        setLibro(datos);
    }

    const onInputChange = (e) => {
        setLibro({ ...libro, [e.target.name]: e.target.value });
    }

    // Lógica completa de envío
    const onSubmit = async (e) => {
        e.preventDefault();
        // Llamamos a la API enviando el ID y el objeto modificado
        await actualizarLibro(id, libro);
        // Redirigimos al inicio
        navegacion('/');
    }

    return (
        <div className='container'>
            <div className='row'>
                <div className='col-md-6 offset-md-3'>
                    <h3 className='text-center text-warning mb-4'>
                        <i className="bi bi-pencil-square me-2"></i>
                        Editar Libro
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
                            <button type="submit" className="btn btn-warning me-3">Guardar Cambios</button>
                            <Link to="/" className="btn btn-danger">Cancelar</Link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}