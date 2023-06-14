from pydantic import BaseModel
from typing import Optional

class UbicacionHora(BaseModel):
    id: Optional[str]
    hora: str
    latitud: Optional[str]
    longitud: Optional[str]
    id_dia: Optional[str]
