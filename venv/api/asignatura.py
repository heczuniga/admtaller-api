
import fastapi

router = fastapi.APIRouter()


@router.get("/api/asignatura/", summary="ASD", tags=["Asignaturas"])
def asignatura():
    value: str = "asignaturas"
    result = {
        "asignaturas": value
    }
    return result
