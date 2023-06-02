
import fastapi

router = fastapi.APIRouter()


@router.get("/api/productos/", tags=["Productos"])
def login():
    value: str = "productos"
    result = {
        "productos": value
    }
    return result
