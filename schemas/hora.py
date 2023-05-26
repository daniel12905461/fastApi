from pydantic import BaseModel
from typing import Optional

class Hora(BaseModel):
    id: Optional[str]
    hora: str
    latitud: Optional[str]
    longitud: Optional[str]
    id_dia: Optional[str]
