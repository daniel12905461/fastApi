from pydantic import BaseModel
from typing import Optional

class Funcionario(BaseModel):
    id: Optional[str]
    nombres: str
    apellidos: str
    ci: str
    foto: str
    celular: str
    fecha_nac: str
    user: str
    password: str
