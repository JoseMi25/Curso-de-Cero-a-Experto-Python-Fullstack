import axios from "axios";

const EMPLEADO_BASE_REST_API_URL = "http://localhost:8080/api/empleados";

class EmpleadoService {
    
    getAllEmpleados() {
        return axios.get(EMPLEADO_BASE_REST_API_URL);
    }

    createEmpleado(empleado) {
        return axios.post(EMPLEADO_BASE_REST_API_URL, empleado);
    }

    getEmpleadoById(empleadoId) {
        return axios.get(EMPLEADO_BASE_REST_API_URL + '/' + empleadoId);
    }

    updateEmpleado(empleadoId, empleado) {
        return axios.put(EMPLEADO_BASE_REST_API_URL + '/' + empleadoId, empleado);
    }

    deleteEmpleado(empleadoId) {
        return axios.delete(EMPLEADO_BASE_REST_API_URL + '/' + empleadoId);
    }
}

export default new EmpleadoService();