
import fastapi

router = fastapi.APIRouter()


@router.get("/api/asignatura/")
def login():
    value: str = "asignaturas"
    result = {
        "asignaturas": value
    }
    return result
