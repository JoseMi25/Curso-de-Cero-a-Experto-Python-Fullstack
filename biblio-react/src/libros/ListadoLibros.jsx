import React, { useEffect, useState } from 'react'
import { listarLibros, eliminarLibro } from '../api/libros'
import { Link } from 'react-router-dom';

export default function ListadoLibros() {

    const [libros, setLibros] = useState([]);

    useEffect(() => {
        cargarLibros();
    }, [])

    const cargarLibros = async () => {
        const datos = await listarLibros();
        setLibros(datos);
    }

    // Función para eliminar un libro
    const eliminar = async (id) => {
        // Confirmación básica de JavaScript
        if (window.confirm("¿Estás seguro de que deseas eliminar este libro?")) {
            await eliminarLibro(id);
            // Recargamos la lista para ver los cambios
            cargarLibros();
        }
    }

    return (
        <div className="container">
            <div className="text-center mb-4">
                <h3 className="text-warning">
                    <i className="bi bi-journal-bookmark-fill me-3"></i>
                    Listado de Libros
                </h3>
            </div>

            <table className="table table-striped table-hover align-middle">
                <thead className="table-primary">
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Título</th>
                        <th scope="col">Autor</th>
                        <th scope="col">Rating</th>
                        <th scope="col">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        libros.map((libro, indice) => (
                            <tr key={indice}>
                                <th scope="row">{libro.id}</th>
                                <td>{libro.titulo}</td>
                                <td>{libro.autor}</td>
                                <td>{libro.rating}</td>
                                <td className='text-center'>
                                    {/* Botón Editar */}
                                    <Link to={`/editar/${libro.id}`} className='btn btn-warning btn-sm me-3'>
                                        <i className="bi bi-pencil-square me-2"></i>
                                        Editar
                                    </Link>
                                    
                                    {/* Botón Eliminar */}
                                    <button onClick={() => eliminar(libro.id)} className='btn btn-danger btn-sm'>
                                        <i className="bi bi-trash3-fill me-2"></i>
                                        Eliminar
                                    </button>
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    )
}