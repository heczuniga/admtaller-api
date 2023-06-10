
import fastapi

router = fastapi.APIRouter()


@router.get("/api/reporte/", summary="ASD", tags=["Reportes"])
def reporte():
    value: str = "reporte"
    result = {
        "reporte": value
    }
    return result
