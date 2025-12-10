import React, { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom';
import EmpleadoService from '../services/EmpleadoService';
import Swal from 'sweetalert2';

export default function AgregarEmpleado() {

    let navigate = useNavigate();

    const [empleado, setEmpleado] = useState({
        nombre: "",
        departamento: "",
        sueldo: ""
    });

    const { nombre, departamento, sueldo } = empleado;

    const onInputChange = (e) => {
        setEmpleado({ ...empleado, [e.target.name]: e.target.value });
    }

    const onSubmit = async (e) => {
        e.preventDefault();
        try {
            await EmpleadoService.createEmpleado(empleado);
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'Empleado registrado con éxito',
                showConfirmButton: false,
                timer: 1500
            })
            navigate('/');
        } catch (error) {
            console.error(error);
            Swal.fire('Error', 'No se pudo guardar el empleado', 'error');
        }
    }

    return (
        <div className='container'>
            <div className='container text-center' style={{ margin: "30px" }}>
                <h3>Agregar Empleado</h3>
            </div>

            <div className="row justify-content-center">
                <div className="col-md-6 border rounded p-4 shadow bg-dark text-white">
                    <form onSubmit={(e) => onSubmit(e)}>
                        <div className="mb-3">
                            <label htmlFor="nombre" className="form-label">Nombre</label>
                            <input type="text" className="form-control" id="nombre" name="nombre" required={true}
                                value={nombre} onChange={(e) => onInputChange(e)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="departamento" className="form-label">Departamento</label>
                            <input type="text" className="form-control" id="departamento" name="departamento"
                                value={departamento} onChange={(e) => onInputChange(e)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="sueldo" className="form-label">Sueldo</label>
                            <input type="number" step="any" className="form-control" id="sueldo" name="sueldo"
                                value={sueldo} onChange={(e) => onInputChange(e)} />
                        </div>
                        
                        <div className='text-center mt-4'>
                            <button type="submit" className="btn btn-warning btn-sm me-3">
                                <i className="bi bi-floppy me-2"></i> Agregar
                            </button>
                            <Link to='/' className='btn btn-danger btn-sm'>
                                <i className="bi bi-arrow-left-circle me-2"></i> Regresar
                            </Link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}