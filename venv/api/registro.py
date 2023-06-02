
import fastapi

router = fastapi.APIRouter()


@router.get("/api/registro/", tags=["Registro"])
def login():
    value: str = "registro"
    result = {
        "registro": value
    }
    return result
