
import fastapi

router = fastapi.APIRouter()


@router.get("/api/taller/", summary="ASD", tags=["Talleres"])
def login():
    value: str = "taller"
    result = {
        "taller": value
    }
    return result
