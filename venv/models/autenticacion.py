
from pydantic import BaseModel
from typing import Optional


class Autenticacion(BaseModel):
    login: str
    password: Optional[str]
    autenticado: bool
