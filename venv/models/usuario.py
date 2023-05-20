
from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id_usuario: int
    login: str
    hash_password: str
    primer_apellido: str
    segundo_apellido: str
    nom: str
    nom_preferido: Optional[str]
    cod_perfil: int
    cod_carrera: Optional[int]
    nom_perfil: Optional[str]
    nom_carrera: Optional[str]
