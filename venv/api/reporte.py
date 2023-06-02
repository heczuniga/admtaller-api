
import fastapi

router = fastapi.APIRouter()


@router.get("/api/reportes/", tags=["Reportes"])
def login():
    value: str = "reportes"
    result = {
        "reportes": value
    }
    return result
