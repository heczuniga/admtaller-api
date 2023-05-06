
import fastapi

router = fastapi.APIRouter()


@router.get("/api/registro/")
def login():
    value: str = "registro"
    result = {
        "registro": value
    }
    return result
