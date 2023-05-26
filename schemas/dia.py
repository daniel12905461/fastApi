from pydantic import BaseModel
from typing import Optional

class Dia(BaseModel):
    id: Optional[str]
    nombre: str
    numero: Optional[str]
    estado: Optional[str]
    detalle: str
    fecha: str
    id_funcionarios: Optional[str]
    id_mes: Optional[str]
