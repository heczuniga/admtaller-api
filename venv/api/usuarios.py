
import fastapi

router = fastapi.APIRouter()


@router.get("/api/usuario/login/{login}")
def login_usuario(login: str):
    if login == "admin@duoc.cl":
        return {
            "id_usuario": 1,
        }

    if login == "jmoya@duoc.cl":
        return {
            "id_usuario": 2,
        }

    if login == "maalvarez@duoc.cl":
        return {
            "id_usuario": 3,
        }

    return None
