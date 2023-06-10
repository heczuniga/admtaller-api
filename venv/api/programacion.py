
import fastapi

router = fastapi.APIRouter()


@router.get("/api/programacion/", summary="ASD", tags=["Programación"])
def programacion():
    value: str = "programacion"
    result = {
        "programacion": value
    }
    return result
