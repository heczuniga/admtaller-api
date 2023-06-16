
import fastapi
from fastapi import HTTPException
from fastapi import status
import aiomysql

from typing import List
from models.programacion_asignatura import ProgramacionAsignatura
from database import get_db_connection
from api.perfil import perfil_usuario
from infrastructure.constants import Const
from api.perfil import perfil_cod_carrera

router = fastapi.APIRouter()


@router.get("/api/programacion/asignatura/{ano_academ}/{id_usuario}", summary="Recupera la lista de las asignaturas programadas para un año académico", tags=["Programación"])
async def programacion_asignatura_lista(ano_academ: int, id_usuario: int):
    # Determinamos el perfil del usuario para determinar qué información puede ver
    perfil = await perfil_usuario(id_usuario)
    programaciones: List[ProgramacionAsignatura] = []
    # Si todo está correcto, Retornamos la respuesta de la API
    if not perfil:
        return programaciones
    # Perfil docente no debe ver nada
    if perfil.cod_perfil == Const.K_DOCENTE.value:
        return programaciones

    if perfil.cod_perfil == Const.K_ADMINISTRADOR_CARRERA.value:
        # Determinamos la carrera del usuario
        dicc = await perfil_cod_carrera(id_usuario)
        cod_carrera = dicc["cod_carrera"]

        query = " \
            select pa.ano_academ as ano_academ, \
                pa.cod_periodo_academ as cod_periodo_academ, \
                pa.sigla as sigla, \
                pa.seccion as seccion, \
                a.cod_carrera as cod_carrera, \
                c.nom_carrera as nom_carrera, \
                a.nom_asign as nom_asign, \
                per.nom_periodo_academ as nom_periodo_academ \
            from prog_asign pa \
                join periodo_academ per on pa.cod_periodo_academ = per.cod_periodo_academ \
                join asign a on pa.sigla = a.sigla \
                join carrera c on a.cod_carrera = c.cod_carrera \
            where pa.ano_academ = %s and \
                a.cod_carrera = %s \
            order by pa.cod_periodo_academ asc, \
                a.cod_carrera asc, \
                pa.sigla asc, \
                pa.seccion asc"

        db = await get_db_connection()
        if db is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

        try:
            values = (ano_academ, cod_carrera)
            async with db.cursor() as cursor:
                await cursor.execute(query, values)
                result = await cursor.fetchall()

        except aiomysql.Error as e:
            error_message = str(e)
            if "Connection" in error_message:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

        except Exception as e:
            error_message = str(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DB error {error_message}")

        finally:
            db.close()

    if perfil.cod_perfil == Const.K_ADMINISTRADOR_TI.value:
        query = " \
            select pa.ano_academ as ano_academ, \
                pa.cod_periodo_academ as cod_periodo_academ, \
                pa.sigla as sigla, \
                pa.seccion as seccion, \
                a.cod_carrera as cod_carrera, \
                c.nom_carrera as nom_carrera, \
                a.nom_asign as nom_asign, \
                per.nom_periodo_academ as nom_periodo_academ \
            from prog_asign pa \
                join periodo_academ per on pa.cod_periodo_academ = per.cod_periodo_academ \
                join asign a on pa.sigla = a.sigla \
                join carrera c on a.cod_carrera = c.cod_carrera \
            where pa.ano_academ = %s \
            order by pa.cod_periodo_academ asc, \
                a.cod_carrera asc, \
                pa.sigla asc, \
                pa.seccion asc"

        db = await get_db_connection()
        if db is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

        try:
            values = (ano_academ)
            async with db.cursor() as cursor:
                await cursor.execute(query, values)
                result = await cursor.fetchall()

        except aiomysql.Error as e:
            error_message = str(e)
            if "Connection" in error_message:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error en la consulta a la base de datos. DBerror {error_message}")

        except Exception as e:
            error_message = str(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error en la base de datos. DB error {error_message}")

        finally:
            db.close()

    # Armamos el diccionario de salida
    programacion: ProgramacionAsignatura = None
    for row in result:
        print
        programacion = ProgramacionAsignatura(ano_academ=row[0],
                                                cod_periodo_academ=row[1],
                                                sigla=row[2],
                                                seccion=row[3],
                                                cod_carrera=row[4],
                                                nom_carrera=row[5],
                                                nom_asignatura=row[6],
                                                nom_periodo_academ=row[7])

        programaciones.append(programacion)

    return programaciones
