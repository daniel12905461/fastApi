from pydantic import BaseModel
from typing import Optional, Union

class Ubicacion(BaseModel):
    id: Optional[str]
    nombre: str
    latitud: Optional[float]
    longitud: Optional[float]
