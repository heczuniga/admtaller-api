
import fastapi

router = fastapi.APIRouter()


@router.get("/api/producto/", summary="ASD", tags=["Productos"])
def productos():
    value: str = "producto"
    result = {
        "producto": value
    }
    return result
