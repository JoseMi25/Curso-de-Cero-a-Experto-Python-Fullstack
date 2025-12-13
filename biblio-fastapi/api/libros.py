from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import schemas
from services import libro_service

router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)

@router.get("/", response_model=List[schemas.LibroRead])
def get_libros(db: Session = Depends(get_db)):
    """
    Endpoint para obtener el listado completo de libros.
    """
    return libro_service.listar_libros(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.LibroRead)
def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo libro.
    """
    return libro_service.crear_libro(db, libro)

@router.get("/{id}", response_model=schemas.LibroRead)
def get_libro(id: int, db: Session = Depends(get_db)):
    """
    Busca un libro por ID.
    """
    libro = libro_service.obtener_libro_por_id(db, id)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro

@router.put("/{id}", response_model=schemas.LibroRead)
def update_libro(id: int, libro_actualizado: schemas.LibroUpdate, db: Session = Depends(get_db)):
    """
    Actualiza un libro existente.
    """
    libro = libro_service.actualizar_libro(db, id, libro_actualizado)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro

# Endpoint para eliminar un libro
@router.delete("/{id}")
def delete_libro(id: int, db: Session = Depends(get_db)):
    """
    Elimina un libro por ID.
    Si no existe, devuelve error 404.
    Si tiene éxito, devuelve un mensaje de confirmación y status 200.
    """
    libro = libro_service.eliminar_libro(db, id)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    
    return {"mensaje": "Libro eliminado correctamente"}