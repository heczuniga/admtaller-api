

import fastapi
from fastapi import HTTPException
from fastapi import status
import aiomysql

from typing import List
from models.taller import Taller
from models.usuario import Usuario
from database import get_db_connection
from api.perfil import perfil_usuario
from infrastructure.constants import Const


router = fastapi.APIRouter()


@router.get("/api/asignatura/{sigla}/taller/lista", summary="Recupera la lista de los talleres de una asignatura", tags=["Talleres"])
async def taller_lista(sigla: str):

    query = " \
        select t.id_taller as id_taller, \
            t.titulo_preparacion as titulo_preparacion, \
            t.detalle_preparacion as detalle_preparacion, \
            t.semana, \
            t.sigla \
        from taller t \
        where t.sigla = %s \
        order by t.semana asc"
    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        values = (sigla)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            result = await cursor.fetchall()

    except aiomysql.Error as e:
        error_message = str(e)
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error en la base de datos")

    finally:
        db.close()

    # Armamos el diccionario de salida
    taller: Taller = None
    talleres: List[Taller] = []
    for row in result:
        taller = Taller(id_taller=row[0],
                            titulo_preparacion=row[1],
                            detalle_preparacion=row[2],
                            semana=row[3],
                            sigla=row[4])
        talleres.append(taller)

    return talleres


@router.delete("/api/taller/eliminar/{id_taller}", response_model=dict, summary="Elimina un taller de una asignatura", tags=["Talleres"])
async def asignatura_eliminar(id_taller: int):

    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = "delete from taller where id_taller = %s"

        values = (id_taller)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            await db.commit()

            return {
                "id_taller": id_taller,
                "eliminado": True,
                "msg_error": None
            }

    except aiomysql.Error as e:
        error_message = str(e)
        # Controlamos de manera especial el error de integridad de datos
        if "1451" in error_message:
            return {
                "id_taller": id_taller,
                "eliminado": False,
                "msg_error": "Taller no se puede eliminar por integridad de datos con otras tablas"
                }
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DBerror {error_message}")

    finally:
        db.close()

    return {
        "id_taller": id_taller,
        "eliminado": True
    }


@router.get("/api/taller/{id_taller}/{id_usuario}", response_model=Taller, summary="Recupera un taller en base a su ID", tags=["Talleres"])
async def taller_get(id_taller: int, id_usuario: int):
    taller: Taller = {
            "id_taller": 0,
            "titulo_preparacion": "",
            "detalle_preparacion": "",
            "semana": 0,
            "sigla": "",
        }

    # Si id_taller = 0 se asume que es un usuario nuevo
    if id_taller == 0:
        return taller

    # Determinamos el perfil del usuario conectado para determinar qué información puede ver
    perfil = await perfil_usuario(id_usuario)
    # Si todo está correcto, Retornamos la respuesta de la API
    if not perfil:
        return taller
    # Perfil docente no debe ver nada
    if perfil.cod_perfil == Const.K_DOCENTE.value:
        return taller

    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = "select t.id_taller as id_taller, \
                    t.titulo_preparacion as titulo_preparacion, \
                    t.detalle_preparacion as detalle_preparacion, \
                    t.semana as semana, \
                    t.sigla as sigla, \
                    a.nom_asign as nom_asign \
                from taller t \
                join asign a on t.sigla = a.sigla \
                where t.id_taller = %s"

        values = (id_taller)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            result = await cursor.fetchone()
            if not result:
                return taller

            asignatura = Taller(id_taller=result[0],
                            titulo_preparacion=result[1],
                            detalle_preparacion=result[2],
                            semana=result[3],
                            sigla=result[4],
                            nom_asignatura=result[5])
            return asignatura

    except aiomysql.Error as e:
        error_message = str(e)
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DBerror {error_message}")

    finally:
        db.close()


@router.put("/api/taller", response_model=Taller, summary="Modificar un taller", tags=["Talleres"])
async def taller_update(taller: Taller) -> Taller:

    print(taller)
    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = "update taller \
                    set titulo_preparacion = %s, \
                        detalle_preparacion = %s, \
                        semana = %s, \
                        sigla = %s \
                where id_taller = %s"
        values = (taller.titulo_preparacion,
                  taller.detalle_preparacion,
                  taller.semana,
                  taller.sigla,
                  taller.id_taller)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)

    except aiomysql.Error as e:
        error_message = str(e)
        print(error_message)
        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al conectar a la base de datos. DBerror {error_message}")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DBError {error_message}")

    finally:
        db.close()

    return taller


@router.post("/api/taller", response_model=Taller, summary="Agregar un taller", tags=["Talleres"])
async def taller_insertar(taller: Taller) -> Taller:

    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        query = \
            "insert into taller ( \
                titulo_preparacion, \
                detalle_preparacion, \
                semana, \
                sigla) \
            values ( \
                %s, \
                %s, \
                %s, \
                %s)"
        values = (taller.titulo_preparacion,
                    taller.detalle_preparacion,
                    taller.semana,
                    taller.sigla)
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            taller.id_taller = cursor.lastrowid

    except aiomysql.Error as e:
        error_message = str(e)
        # Controlamos de manera especial el error de integridad de datos
        if "1062" in error_message:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al insertar registro existente. DBerror {error_message}")

        if "Connection" in error_message:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al conectar a la base de datos. DBerror {error_message}")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DBError {error_message}")

    finally:
        db.close()

    return taller
