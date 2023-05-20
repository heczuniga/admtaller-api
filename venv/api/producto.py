
import fastapi

router = fastapi.APIRouter()


@router.get("/api/productos/")
def login():
    value: str = "productos"
    result = {
        "productos": value
    }
    return result
