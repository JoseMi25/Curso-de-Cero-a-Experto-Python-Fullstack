from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

# 1. LibroBase
# Contiene los campos comunes que se usan tanto al crear como al leer.
class LibroBase(BaseModel):
    # Validamos que titulo y autor no sean cadenas vacías con min_length=1
    titulo: str = Field(..., min_length=1, description="El título del libro")
    autor: str = Field(..., min_length=1, description="El autor del libro")
    
    # Validamos que el rating esté entre 1 y 5
    rating: int = Field(..., ge=1, le=5, description="Calificación del 1 al 5")

# 2. LibroCreate
# Esquema usado para recibir datos en POST. 
# Hereda todo de LibroBase, no necesitamos agregar nada extra por ahora.
class LibroCreate(LibroBase):
    pass

# 3. LibroUpdate
# Esquema para actualizar (PUT). 
# Al heredar de LibroBase, exigimos que envíen todos los datos de nuevo (reemplazo completo).
class LibroUpdate(LibroBase):
    pass

# 4. LibroRead
# Esquema para devolver datos al cliente (GET).
# Incluye el 'id' que genera la base de datos, el cual NO enviamos al crear.
class LibroRead(LibroBase):
    id: int

    # Configuración para que Pydantic pueda leer datos directamente 
    # desde los objetos de SQLAlchemy (ORM).
    # En Pydantic v1 esto era 'orm_mode = True'
    model_config = ConfigDict(from_attributes=True)