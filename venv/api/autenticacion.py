
import fastapi

from typing import List

from models.autenticacion import Autenticacion
from models.perfil import Perfil
from models.perfil import ItemMenu

router = fastapi.APIRouter()


@router.post("/api/autenticacion/", response_model=Autenticacion, name="Autenticar un usuario y contraseña")
async def autenticacion(autenticacion: Autenticacion) -> Autenticacion:

    # Limpiamos la data ingresada
    autenticacion.login = autenticacion.login.strip()

    if autenticacion.login == "admin@duoc.cl" and autenticacion.password == "admin":
        autenticacion.autenticado = True

    if autenticacion.login == "jmoya@duoc.cl" and autenticacion.password == "jmoya":
        autenticacion.autenticado = True

    if autenticacion.login == "maalvarez@duoc.cl" and autenticacion.password == "maalvarez":
        autenticacion.autenticado = True

    # Limpiamos la password
    autenticacion.password = None

    return autenticacion


@router.post("/api/perfil/")
def perfil(login: str) -> Perfil:

    p: Perfil = None

    # Limpiamos la data ingresada
    login = login.strip()

    if login == "admin":
        p = Perfil(cod_perfil=0, nom_perfil="Administrador")

    if login == "jmoya@duoc.cl":
        p = Perfil(cod_perfil=1, nom_perfil="Administrador de carrera", cod_carrera=1, nom_carrera="Gastronomía")

    if login == "maalvarez@duoc.cl":
        p = Perfil(cod_perfil=2, nom_perfil="Docente", cod_carrera=1, nom_carrera="Gastronomía")

    return p


@router.post("/api/perfil/lista/")
def listaperfil(login: str) -> List[ItemMenu]:

    result: List[ItemMenu] = []
    item_menu: ItemMenu = None

    # Limpiamos la data ingresada
    login = login.strip()


    if login == "admin":
        item_menu = ItemMenu(cod_item_menu="01",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Usuarios", 
                             url="usuarios/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="02",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Talleres", 
                             url="asignaturas/lista/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="03",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Programación", 
                             url="programacion/lista/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="04",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Reportes", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0401",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 1", 
                             url="reportes/1/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0402",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 2", 
                             url="reportes/2/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0403",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 3", 
                             url="reportes/3/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0404",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 4", 
                             url="reportes/4/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0405",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Reporte 5", 
                             url="reportes/5/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="05",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Consultas", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0501",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 1", 
                             url="consultas/1/",
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0502",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 2", 
                             url="consultas/2/", 
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0503",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 3", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0504",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 4", 
                             url="consulta/4/", 
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0505",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 5", 
                             url="consultas/5/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="06",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Productos", 
                             url="productos/lista/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="07",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Registro", 
                             url="registro/lista/", 
                             nivel=1)
        result.append(item_menu)

    if login == "jmoya@duoc.cl":
        item_menu = ItemMenu(cod_item_menu="01",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Usuarios", 
                             url="usuarios/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="02",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Talleres", 
                             url="asignaturas/lista/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="03",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Programación", 
                             url="programacion/lista/", 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="04",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Reportes", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0401",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 1", 
                             url="reportes/1/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0402",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 2", 
                             url="reportes/2/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0403",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 3", 
                             url="reportes/3/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0404",
                             cod_item_menu_padre="04", 
                             nom_item_menu="Reporte 4", 
                             url="reportes/4/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0405",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Reporte 5", 
                             url="reportes/5/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="05",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Consultas", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0501",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 1", 
                             url="consultas/1/",
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0502",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 2", 
                             url="consultas/2/", 
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0503",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 3", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0504",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 4", 
                             url="consulta/4/", 
                             nivel=2)
        result.append(item_menu)
        
        item_menu = ItemMenu(cod_item_menu="0505",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 5", 
                             url="consultas/5/", 
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="06",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Productos", 
                             url="productos/lista/", 
                             nivel=1)
        result.append(item_menu)

    if login == "maalvarez@duoc.cl":
        item_menu = ItemMenu(cod_item_menu="05",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Consultas", 
                             url=None, 
                             nivel=1)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="0501",
                             cod_item_menu_padre="05", 
                             nom_item_menu="Consulta 1", 
                             url="consultas/1/",
                             nivel=2)
        result.append(item_menu)

        item_menu = ItemMenu(cod_item_menu="07",
                             cod_item_menu_padre=None, 
                             nom_item_menu="Registro", 
                             url="registro/lista/", 
                             nivel=1)
        result.append(item_menu)

    return result
