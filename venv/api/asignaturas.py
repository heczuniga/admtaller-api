
import fastapi

router = fastapi.APIRouter()


@router.get("/api/asignaturas/")
def login():
    value: str = "asignaturas"
    result = {
        "asignaturas": value
    }
    return result
