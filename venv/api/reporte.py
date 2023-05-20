
import fastapi

router = fastapi.APIRouter()


@router.get("/api/reportes/")
def login():
    value: str = "reportes"
    result = {
        "reportes": value
    }
    return result
