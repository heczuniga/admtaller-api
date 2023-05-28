import fastapi
from fastapi import HTTPException, status
import aiomysql

from database import get_db_connection
from models.autenticacion import Autenticacion

router = fastapi.APIRouter()

@router.post("/api/autenticacion/", response_model=Autenticacion, name="Autenticar un usuario y contraseña")
async def autenticacion(autenticacion: Autenticacion) -> Autenticacion:
    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        autenticacion.login = autenticacion.login.strip()
        query = "select * \
                from usuario \
                where login = %s and \
                    hash_password = %s"
        values = (autenticacion.login, autenticacion.password)

        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            result = await cursor.fetchone()

        if result:
            autenticacion.autenticado = True
        else:
            autenticacion.autenticado = False

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

    autenticacion.password = None

    return autenticacion
