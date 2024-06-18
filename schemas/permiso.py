from pydantic import BaseModel
from typing import Optional, Union

class Permiso(BaseModel):
    id: Optional[str]
    motivo: str
    id_dia: Optional[str]
    id_funcionarios: Optional[str]
