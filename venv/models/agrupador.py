
from pydantic import BaseModel
from typing import Optional


# Modelo que representa un agrupador
class Agrupador(BaseModel):

    cod_agrupador: int
    nom_agrupador: str
