
import fastapi
from models.perfil import Perfil
from datetime import date

router = fastapi.APIRouter()


@router.get("/api/perfil/usuario/{id_usuario}", response_model=Perfil, summary="Obtener el perfil de un usuario con un id específico")
async def perfil_usuario(id_usuario: int):
    perfil: Perfil = None

    if id_usuario == 1:
        perfil = Perfil(cod_perfil=0, nom_perfil="Administrador TI", descripcion="Administrador desde el punto de vista TI del sistema. En resumen, tiene acceso a todo. Es el alfa y el omega del sistema.")
    if id_usuario == 2:
        perfil = Perfil(cod_perfil=1, nom_perfil="Administrador de carrera", descripcion="Administrador de entidades del sistema, usuarios y perfiles. También accede a reportes de gestión.")
    if id_usuario == 3:
        perfil = Perfil(cod_perfil=2, nom_perfil="Docente", descripcion="Docentes de la carrera responsables de la ejecución del taller.")

    return perfil


@router.get("/api/param/ano_academ/valor", response_model=dict, summary="Obtener el valor del parámetro año académico vigente")
async def param_ano_academ_valor():
    return {
        "ano_academ": date.today().year,
    }


@router.get("/api/perfil/nom_carrera/{id_usuario}", response_model=dict, summary="Obtener el nombre de la carrera asignada al usuario respectivo")
async def perfil_nom_usuario(id_usuario: int):
    if id_usuario == 1:
        return {
            "nom_carrera": None,
        }
    if id_usuario == 2:
        return {
            "nom_carrera": "Gastronomía",
        }
    if id_usuario == 3:
        return {
            "nom_carrera": "Administración hotelera",
        }
