
import fastapi
from models.carrera import Carrera
from typing import List

router = fastapi.APIRouter()


@router.get("/api/carrera/lista", summary="Obtener la lista de carreras desde el sistema")
async def carrera_lista():
    carrera: Carrera = None
    lista_carrera: List[Carrera] = []

    carrera = Carrera(cod_carrera=1, nom_carrera="Gastronomía", nom_carrera_abrev="GASTRO")
    lista_carrera.append(carrera)
    carrera = Carrera(cod_carrera=2, nom_carrera="Administración hotelera", nom_carrera_abrev="HOTEL")
    lista_carrera.append(carrera)

    return lista_carrera
