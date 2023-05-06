
import fastapi

router = fastapi.APIRouter()


@router.get("/api/usuarios/")
def login():
    value: str = "usuarios"
    result = {
        "usuarios": value
    }
    return result
