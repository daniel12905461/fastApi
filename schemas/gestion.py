from pydantic import BaseModel
from typing import Optional

class Gestion(BaseModel):
    id: Optional[str]
    nombres: str
