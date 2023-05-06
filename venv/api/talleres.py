
import fastapi

router = fastapi.APIRouter()


@router.get("/api/talleres/")
def login():
    value: str = "talleres"
    result = {
        "talleres": value
    }
    return result
