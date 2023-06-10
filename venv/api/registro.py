
import fastapi

router = fastapi.APIRouter()


@router.get("/api/registro/", summary="ASD", tags=["Registro"])
def registro():
    value: str = "registro"
    result = {
        "registro": value
    }
    return result
