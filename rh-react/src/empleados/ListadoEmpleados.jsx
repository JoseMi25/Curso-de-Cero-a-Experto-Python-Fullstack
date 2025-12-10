import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import EmpleadoService from '../services/EmpleadoService';
import Swal from 'sweetalert2';

export default function ListadoEmpleados() {

    const [empleados, setEmpleados] = useState([]);
    const [busqueda, setBusqueda] = useState("");

    useEffect(() => {
        cargarEmpleados();
    }, []);

    const cargarEmpleados = async () => {
        try {
            const resultado = await EmpleadoService.getAllEmpleados();
            setEmpleados(resultado.data);
        } catch (error) {
            console.error("Error al cargar empleados:", error);
        }
    }

    const eliminarEmpleado = async (id) => {
        const result = await Swal.fire({
            title: '¿Estás seguro?',
            text: "No podrás revertir esta acción",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        });

        if (result.isConfirmed) {
            try {
                await EmpleadoService.deleteEmpleado(id);
                cargarEmpleados(); 
                Swal.fire(
                    '¡Eliminado!',
                    'El empleado ha sido eliminado.',
                    'success'
                )
            } catch (error) {
                console.error("Error al eliminar:", error);
                Swal.fire('Error', 'No se pudo eliminar el registro', 'error');
            }
        }
    }

    return (
        <div className="container">
            <div className="container text-center" style={{ margin: "30px" }}>
                <h3>Sistema de Recursos Humanos</h3>
            </div>
            <div className="row mb-4">
                <div className="col-md-6 offset-md-3">
                    <div className="input-group">
                        <span className="input-group-text bg-dark text-white border-secondary">
                            <i className="bi bi-search"></i>
                        </span>
                        <input 
                            type="text" 
                            className="form-control bg-dark text-white border-secondary" 
                            placeholder="Buscar empleado por nombre..." 
                            value={busqueda}
                            onChange={(e) => setBusqueda(e.target.value)}
                        />
                    </div>
                </div>
            </div>

            <div className="card shadow border-0">
                <div className="card-body p-0">
                    <table className="table table-striped table-hover align-middle mb-0">
                        <thead className='table-dark'>
                            <tr>
                                <th scope="col" className="ps-4">Id</th>
                                <th scope="col">Empleado</th>
                                <th scope="col">Departamento</th>
                                <th scope="col">Sueldo</th>
                                <th scope="col" className="text-center">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {empleados
                                .filter((empleado) => 
                                    empleado.nombre.toLowerCase().includes(busqueda.toLowerCase())
                                )
                                .map((empleado, indice) => (
                                <tr key={indice}>
                                    <th scope="row" className="ps-4">{empleado.idEmpleado}</th>
                                    <td>{empleado.nombre}</td>
                                    <td>{empleado.departamento}</td>
                                    <td>
                                        {new Intl.NumberFormat('es-MX', {
                                            style: 'currency',
                                            currency: 'MXN'
                                        }).format(empleado.sueldo)}
                                    </td>
                                    <td className='text-center'>
                                        <div>
                                            <Link to={`/editar/${empleado.idEmpleado}`}
                                                className='btn btn-warning btn-sm me-2' title="Editar">
                                                <i className="bi bi-pencil-square"></i>
                                            </Link>
                                            
                                            <button 
                                                onClick={() => eliminarEmpleado(empleado.idEmpleado)}
                                                className='btn btn-danger btn-sm' title="Eliminar">
                                                <i className="bi bi-trash3-fill"></i>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                            {empleados.length === 0 && (
                                <tr>
                                    <td colSpan="5" className="text-center p-4">No hay empleados registrados.</td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}