
import fastapi

router = fastapi.APIRouter()


@router.get("/api/asignatura/", tags=["Asignaturas"])
def login():
    value: str = "asignaturas"
    result = {
        "asignaturas": value
    }
    return result
