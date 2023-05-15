from pydantic import BaseModel
from typing import Optional

class Horario(BaseModel):
    id: Optional[str]
    hora_inicio: str
    hora_inicio_reseso: str
    hora_fin_reseso: str
    hora_fin: str
    domingo: bool
    lunes: bool
    martes: bool
    miercoles: bool
    jueves: bool
    viernes: bool
    sabado: bool
