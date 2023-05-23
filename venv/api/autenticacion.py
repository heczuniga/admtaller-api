
import fastapi

from typing import List

from models.autenticacion import Autenticacion
from models.perfil import Perfil
from models.perfil import ItemMenu

router = fastapi.APIRouter()


@router.post("/api/autenticacion/", response_model=Autenticacion, name="Autenticar un usuario y contraseña")
async def autenticacion(autenticacion: Autenticacion) -> Autenticacion:

    # Limpiamos la data ingresada
    autenticacion.login = autenticacion.login.strip()

    if autenticacion.login == "admin@duoc.cl" and autenticacion.password == "admin":
        autenticacion.autenticado = True

    if autenticacion.login == "jmoya@duoc.cl" and autenticacion.password == "jmoya":
        autenticacion.autenticado = True

    if autenticacion.login == "maalvarez@duoc.cl" and autenticacion.password == "maalvarez":
        autenticacion.autenticado = True

    # Limpiamos la password
    autenticacion.password = None

    return autenticacion
