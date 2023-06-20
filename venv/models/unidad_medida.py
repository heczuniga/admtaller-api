
from pydantic import BaseModel
from typing import Optional


# Modelo que representa un agrupador
class UnidadMedida(BaseModel):

    cod_unidad_medida: int
    nom_unidad_medida: str
    nom_unidad_medida_abrev: str
