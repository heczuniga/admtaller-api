
import fastapi

router = fastapi.APIRouter()


@router.get("/api/principal/")
def login():
    value: str = "principal"
    result = {
        "datos": value
    }
    return result
