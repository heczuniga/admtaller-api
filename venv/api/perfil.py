
import fastapi
from models.perfil import Perfil
from datetime import date
from typing import List
from fastapi import HTTPException
from fastapi import status
import aiomysql

from database import get_db_connection

router = fastapi.APIRouter()


@router.get("/api/perfil/usuario/{id_usuario}", response_model=Perfil, summary="Obtener el perfil de un usuario coa través de su id")
async def perfil_usuario(id_usuario: int):
    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = "select p.cod_perfil as cod_perfil, \
                    p.nom_perfil as nom_perfil, \
                    p.descripcion as descripcion \
                from perfil p, \
                    usuario u \
                where u.cod_perfil = p.cod_perfil and \
                    u.id_usuario = %s"
        values = (id_usuario)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            result = await cursor.fetchone()

        perfil: Perfil = None
        perfil = Perfil(cod_perfil=result[0], nom_perfil=result[1], descripcion=result[2])
        return perfil

    except aiomysql.Error as e:
        error_message = str(e)
        print(error_message)
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error en la base de datos")

    finally:
        db.close()


@router.get("/api/perfil/nom_carrera/{id_usuario}", response_model=dict, summary="Obtener el nombre de la carrera asignada al usuario respectivo")
async def perfil_nom_carrera(id_usuario: int):
    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = "select c.nom_carrera as nom_carrera \
                from carrera c, \
                    usuario u \
                where u.cod_carrera = c.cod_carrera and \
                    u.id_usuario = %s"
        values = (id_usuario)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            result = await cursor.fetchone()

        nom_carrera: str = None
        if result:
            nom_carrera = result[0]

        return {
            "nom_carrera": nom_carrera,
        }

    except aiomysql.Error as e:
        error_message = str(e)
        print(error_message)
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al conectar a la base de datos. DBerror {error_message}.")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}.")

    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. {e}")

    finally:
        db.close()


@router.get("/api/perfil/lista/{id_usuario}", response_model=List[dict], summary="Obtener la lista de perfiles desde el sistema")
async def perfil_lista(id_usuario: int):
    perfil: Perfil = None
    lista_perfil: List[Perfil] = []

    if id_usuario == 1:
        perfil = Perfil(cod_perfil=0, nom_perfil="Administrador TI", descripcion="Administrador desde el punto de vista TI del sistema. En resumen, tiene acceso a todo. Es el alfa y el omega del sistema.")
        lista_perfil.append(perfil)
        perfil = Perfil(cod_perfil=1, nom_perfil="Administrador de carrera", descripcion="Administrador de entidades del sistema, usuarios y perfiles. También accede a reportes de gestión.")
        lista_perfil.append(perfil)
        perfil = Perfil(cod_perfil=2, nom_perfil="Docente", descripcion="Docentes de la carrera responsables de la ejecución del taller.")
        lista_perfil.append(perfil)

    if id_usuario == 2:
        perfil = Perfil(cod_perfil=1, nom_perfil="Administrador de carrera", descripcion="Administrador de entidades del sistema, usuarios y perfiles. También accede a reportes de gestión.")
        lista_perfil.append(perfil)
        perfil = Perfil(cod_perfil=2, nom_perfil="Docente", descripcion="Docentes de la carrera responsables de la ejecución del taller.")
        lista_perfil.append(perfil)

    return lista_perfil
