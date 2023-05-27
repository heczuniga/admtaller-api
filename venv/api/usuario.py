
import fastapi

from typing import List
from models.usuario import Usuario

router = fastapi.APIRouter()


@router.get("/api/usuario/login/{login}", response_model=dict, name="Recupera el id de un usuario en base a su login")
def usuario_login(login: str):
    if login == "admin@duoc.cl":
        return {
            "id_usuario": 1,
        }

    if login == "jmoya@duoc.cl":
        return {
            "id_usuario": 2,
        }

    if login == "maalvarez@duoc.cl":
        return {
            "id_usuario": 3,
        }

    return None


@router.get("/api/usuario/lista/{id_usuario}", response_model=List[dict], name="Recupera un usuario en base a su Id")
def usuario_lista(id_usuario: int):
    d: List[Usuario]

    if id_usuario == 1:
        d = [
            {
                "id_usuario": 3,
                "login": "maalvarez@duoc.cl",
                "password": "None",
                "primer_apellido": "Álvarez",
                "segundo_apellido": "Román",
                "nom": "Marco",
                "nom_preferido": "Marco",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 10,
                "login": "fabi.arancibia@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Arancibia",
                "segundo_apellido": "Severino",
                "nom": "Fabián",
                "nom_preferido": "Fabián",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 12,
                "login": "al.camposa@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Campos",
                "segundo_apellido": "Acuña",
                "nom": "Alejandra",
                "nom_preferido": "Alejandra",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 7,
                "login": "xi.castro@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Castro",
                "segundo_apellido": "Arancibia",
                "nom": "Ximena",
                "nom_preferido": "Ximena",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 5,
                "login": "r.ceura@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Ceura",
                "segundo_apellido": "Vergara",
                "nom": "Raúl",
                "nom_preferido": "Raúl",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 21,
                "login": "j.enero@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Enero",
                "segundo_apellido": "Rivero",
                "nom": "Juan Francisco",
                "nom_preferido": "Juan",
                "cod_perfil": 2,
                "cod_carrera": 2,
                "nom_perfil": "Docente",
                "nom_carrera": "Administración Hotelera"
            },
            {
                "id_usuario": 6,
                "login": "hec.fonseca@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Fonseca",
                "segundo_apellido": "Castillo",
                "nom": "Héctor",
                "nom_preferido": "Héctor",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 15,
                "login": "v.fuentealbav@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Fuentealva",
                "segundo_apellido": "Vargas",
                "nom": "Víctor",
                "nom_preferido": "Víctor",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 4,
                "login": "c.gonzalez6@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "González",
                "segundo_apellido": "Figueroa",
                "nom": "Cristian",
                "nom_preferido": "Cristian",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 22,
                "login": "m.gutierrez2@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Gutierrez",
                "segundo_apellido": "Cortés",
                "nom": "Mauricio",
                "nom_preferido": "Mauricio",
                "cod_perfil": 2,
                "cod_carrera": 2,
                "nom_perfil": "Docente",
                "nom_carrera": "Administración Hotelera"
            },
            {
                "id_usuario": 11,
                "login": "roci.guzman@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Guzmán",
                "segundo_apellido": "Acuña",
                "nom": "Rocío",
                "nom_preferido": "Rocío",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 14,
                "login": "i.inostroza@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Inostroza",
                "segundo_apellido": "Rodríguez",
                "nom": "Isaac",
                "nom_preferido": "Isaac",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 13,
                "login": "cr.madariagam@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Madariaga",
                "segundo_apellido": "Martínez",
                "nom": "Cristian",
                "nom_preferido": "Cristian",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 2,
                "login": "jmoya@duoc.cl",
                "password": "None",
                "primer_apellido": "Moya",
                "segundo_apellido": "Plaza",
                "nom": "Jéssica",
                "nom_preferido": "Jéssica",
                "cod_perfil": 1,
                "cod_carrera": 1,
                "nom_perfil": "Administrador de carrera",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 19,
                "login": "dmunita@duoc.cl",
                "password": "None",
                "primer_apellido": "Munita",
                "segundo_apellido": "Toro",
                "nom": "Daniela",
                "nom_preferido": "Daniela",
                "cod_perfil": 1,
                "cod_carrera": 2,
                "nom_perfil": "Administrador de carrera",
                "nom_carrera": "Administración Hotelera"
            },
            {
                "id_usuario": 9,
                "login": "sa.navarret@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Navarrete",
                "segundo_apellido": "Bustamante",
                "nom": "Sandra",
                "nom_preferido": "Sandra",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 17,
                "login": "car.perezz@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Pérez",
                "segundo_apellido": "Zúñiga",
                "nom": "Carlos",
                "nom_preferido": "Carlos",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 16,
                "login": "j.premolo@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Premolo",
                "segundo_apellido": "Yergues",
                "nom": "Juan",
                "nom_preferido": "Juan",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 18,
                "login": "de.reglas@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Reglas",
                "segundo_apellido": "Villagra",
                "nom": "Deyanira",
                "nom_preferido": "Deyanira",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 8,
                "login": "c.valenzuelair@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Valenzuela",
                "segundo_apellido": "Irrazabal",
                "nom": "Carolina",
                "nom_preferido": "Carolina",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 20,
                "login": "pzamorano@duoc.cl",
                "password": "None",
                "primer_apellido": "Zamorano",
                "segundo_apellido": "Moreno",
                "nom": "Paola",
                "nom_preferido": "Paola",
                "cod_perfil": 2,
                "cod_carrera": 2,
                "nom_perfil": "Docente",
                "nom_carrera": "Administración Hotelera"
            }
        ]

    if id_usuario == 2:
                d = [
            {
                "id_usuario": 3,
                "login": "maalvarez@duoc.cl",
                "password": "None",
                "primer_apellido": "Álvarez",
                "segundo_apellido": "Román",
                "nom": "Marco",
                "nom_preferido": "Marco",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 10,
                "login": "fabi.arancibia@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Arancibia",
                "segundo_apellido": "Severino",
                "nom": "Fabián",
                "nom_preferido": "Fabián",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 12,
                "login": "al.camposa@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Campos",
                "segundo_apellido": "Acuña",
                "nom": "Alejandra",
                "nom_preferido": "Alejandra",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 7,
                "login": "xi.castro@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Castro",
                "segundo_apellido": "Arancibia",
                "nom": "Ximena",
                "nom_preferido": "Ximena",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 5,
                "login": "r.ceura@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Ceura",
                "segundo_apellido": "Vergara",
                "nom": "Raúl",
                "nom_preferido": "Raúl",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 6,
                "login": "hec.fonseca@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Fonseca",
                "segundo_apellido": "Castillo",
                "nom": "Héctor",
                "nom_preferido": "Héctor",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 15,
                "login": "v.fuentealbav@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Fuentealva",
                "segundo_apellido": "Vargas",
                "nom": "Víctor",
                "nom_preferido": "Víctor",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 4,
                "login": "c.gonzalez6@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "González",
                "segundo_apellido": "Figueroa",
                "nom": "Cristian",
                "nom_preferido": "Cristian",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 11,
                "login": "roci.guzman@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Guzmán",
                "segundo_apellido": "Acuña",
                "nom": "Rocío",
                "nom_preferido": "Rocío",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 14,
                "login": "i.inostroza@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Inostroza",
                "segundo_apellido": "Rodríguez",
                "nom": "Isaac",
                "nom_preferido": "Isaac",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 13,
                "login": "cr.madariagam@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Madariaga",
                "segundo_apellido": "Martínez",
                "nom": "Cristian",
                "nom_preferido": "Cristian",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 2,
                "login": "jmoya@duoc.cl",
                "password": "None",
                "primer_apellido": "Moya",
                "segundo_apellido": "Plaza",
                "nom": "Jéssica",
                "nom_preferido": "Jéssica",
                "cod_perfil": 1,
                "cod_carrera": 1,
                "nom_perfil": "Administrador de carrera",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 9,
                "login": "sa.navarret@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Navarrete",
                "segundo_apellido": "Bustamante",
                "nom": "Sandra",
                "nom_preferido": "Sandra",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 17,
                "login": "car.perezz@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Pérez",
                "segundo_apellido": "Zúñiga",
                "nom": "Carlos",
                "nom_preferido": "Carlos",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 16,
                "login": "j.premolo@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Premolo",
                "segundo_apellido": "Yergues",
                "nom": "Juan",
                "nom_preferido": "Juan",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 18,
                "login": "de.reglas@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Reglas",
                "segundo_apellido": "Villagra",
                "nom": "Deyanira",
                "nom_preferido": "Deyanira",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
            {
                "id_usuario": 8,
                "login": "c.valenzuelair@profesor.duoc.cl",
                "password": "None",
                "primer_apellido": "Valenzuela",
                "segundo_apellido": "Irrazabal",
                "nom": "Carolina",
                "nom_preferido": "Carolina",
                "cod_perfil": 2,
                "cod_carrera": 1,
                "nom_perfil": "Docente",
                "nom_carrera": "Gastronomía"
            },
        ]

    return d


@router.get("/api/usuario/{id_usuario_editar}/{id_usuario}", response_model=dict, name="Recupera un usuario en base a su Id")
def usuario_get(id_usuario_editar: int, id_usuario: int):
    u: Usuario

    if id_usuario_editar == -1:
        u = {
            "id_usuario": None,
            "login": None,
            "hash_password": None,
            "primer_apellido": None,
            "segundo_apellido": None,
            "nom": None,
            "nom_preferido": None,
            "cod_perfil": None,
            "cod_carrera": None,
            "nom_perfil": None,
            "nom_carrera": None,
        }
        return u

    if id_usuario_editar == 18:
        u = {
            "id_usuario": 18,
            "login": "de.reglas@profesor.duoc.cl",
            "hash_password": "AHDGSJHGJAHDGJHGDJYTULKDLKLD",
            "primer_apellido": "Reglas",
            "segundo_apellido": "Villagra",
            "nom": "Deyanira",
            "nom_preferido": "Deyanira",
            "cod_perfil": 2,
            "cod_carrera": 1,
            "nom_perfil": "Docente",
            "nom_carrera": "Gastronomía"
        }

        return u
        
    if id_usuario == 1:
        u = {
            "id_usuario": 3,
            "login": "maalvarez@duoc.cl",
            "hash_password": "AHDGSJHGJAHDGJHGDJYTULKDLKLD",
            "primer_apellido": "Álvarez",
            "segundo_apellido": "Román",
            "nom": "Marco",
            "nom_preferido": "Marco",
            "cod_perfil": 2,
            "cod_carrera": 1,
            "nom_perfil": "Docente",
            "nom_carrera": "Gastronomía"
        }
    if id_usuario == 2:
        u = {
            "id_usuario": 3,
            "login": "maalvarez@duoc.cl",
            "hash_password": "AHDGSJHGJAHDGJHGDJYTULKDLKLD",
            "primer_apellido": "Álvarez",
            "segundo_apellido": "Román",
            "nom": "Marco",
            "nom_preferido": "Marco",
            "cod_perfil": 2,
            "cod_carrera": 1,
            "nom_perfil": "Docente",
            "nom_carrera": "Gastronomía"
        }
    if id_usuario == 3:
        u = {
            "id_usuario": 0,
            "login": None,
            "hash_password": None,
            "primer_apellido": None,
            "segundo_apellido": None,
            "nom": None,
            "nom_preferido": None,
            "cod_perfil": None,
            "cod_carrera": None,
            "nom_perfil": None,
            "nom_carrera": None
        }

    return u


@router.delete("/api/usuario/eliminar/{id_usuario_eliminar}", response_model=dict, name="Elimina un usuario y retorna si hubo o no éxito")
def usuario_eliminar(id_usuario_eliminar: int):
    return {
        "id_usuario": id_usuario_eliminar,
        "eliminado": True
    }



@router.put("/api/usuario/{id_usuario_modificar}/", response_model=dict, name="Modificar un usuario")
async def usuario_modificar(usuario: Usuario, id_usuario_modificar) -> Usuario:

    return {
        "id_usuario": 3,
        "login": "maalvarez@profesor.duoc.cl",
        "hash_password": "AHDGSJHGJAHDGJHGDJYTULKDLKLD",
        "primer_apellido": "Álvarez",
        "segundo_apellido": "Román",
        "nom": "Marco Aurelio",
        "nom_preferido": "Marco",
        "cod_perfil": 2,
        "cod_carrera": 1,
        "nom_perfil": "Docente",
        "nom_carrera": "Gastronomía"
    }


@router.post("/api/usuario", response_model=dict, name="Agregar un usuario")
async def usuario_insertar(usuario: Usuario) -> Usuario:

    return {
        "id_usuario": 18,
        "login": "de.reglas@profesor.duoc.cl",
        "hash_password": "AHDGSJHGJAHDGJHGDJYTULKDLKLD",
        "primer_apellido": "Reglas",
        "segundo_apellido": "Villagra",
        "nom": "Deyanira",
        "nom_preferido": "Deyanira",
        "cod_perfil": 2,
        "cod_carrera": 1,
        "nom_perfil": "Docente",
        "nom_carrera": "Gastronomía"
    }
