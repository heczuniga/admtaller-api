
import fastapi

router = fastapi.APIRouter()


@router.get("/api/programacion/", tags=["Programación"])
def login():
    value: str = "programacion"
    result = {
        "programacion": value
    }
    return result
