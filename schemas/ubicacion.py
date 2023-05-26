from pydantic import BaseModel
from typing import Optional

class Ubicacion(BaseModel):
    id: Optional[str]
    nombre: str
    latitud: Optional[str]
    longitud: Optional[str]
