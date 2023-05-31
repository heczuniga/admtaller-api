
from pydantic import BaseModel
from typing import Optional


class Autenticacion(BaseModel):
    login: str
    password: Optional[str]
    autenticado: bool = False


class CambioPassword(BaseModel):
    id_usuario: int
    nueva_password: Optional[str]
    confirmacion_nueva_password: Optional[str]
    modificada: bool = False
