
import fastapi

router = fastapi.APIRouter()


@router.get("/api/programacion/")
def login():
    value: str = "programacion"
    result = {
        "programacion": value
    }
    return result
