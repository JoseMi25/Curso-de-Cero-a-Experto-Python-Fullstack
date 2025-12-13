import axios from "axios";

const urlBase = "http://localhost:8080/api/libros";

export const listarLibros = async () => {
    const respuesta = await axios.get(urlBase);
    return respuesta.data;
}

export const crearLibro = async (libro) => {
    await axios.post(urlBase, libro);
}

export const obtenerLibroPorId = async (id) => {
    const respuesta = await axios.get(`${urlBase}/${id}`);
    return respuesta.data;
}

export const actualizarLibro = async (id, libro) => {
    await axios.put(`${urlBase}/${id}`, libro);
}

export const eliminarLibro = async (id) => {
    await axios.delete(`${urlBase}/${id}`);
}