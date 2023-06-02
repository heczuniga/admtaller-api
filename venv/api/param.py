
import fastapi
from models.perfil import Perfil
from datetime import date
from typing import List

router = fastapi.APIRouter()


@router.get("/api/param/ano_academ/valor", response_model=dict, summary="Obtener el valor del parámetro año académico vigente", tags=["Parámetros"])
async def param_ano_academ_valor():
    return {
        "ano_academ": date.today().year,
    }
