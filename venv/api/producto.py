
import fastapi
from fastapi import HTTPException
from fastapi import status
import aiomysql

from typing import List
from models.producto import Producto
from database import get_db_connection
from api.perfil import perfil_usuario
from infrastructure.constants import Const

router = fastapi.APIRouter()


@router.get("/api/producto/lista/{id_usuario}", summary="Recupera los productos del sistema para un determinado usuario", tags=["Productos"])
async def productos(id_usuario: int):
    productos: List[Producto] = []    

    # Determinamos el perfil del usuario para determinar qué información puede ver
    perfil = await perfil_usuario(id_usuario)
    # Si todo está correcto, Retornamos la respuesta de la API
    if not perfil:
        return productos
    
    if perfil.cod_perfil == Const.K_DOCENTE.value:
        return productos

    query = " \
        select p.id_producto as id_producto, \
            p.nom_producto as nom_producto, \
            p.precio as precio, \
            p.cod_unidad_medida as cod_unidad_medida, \
            p.cod_categ_producto as cod_categ_producto, \
            um.nom_unidad_medida as nom_unidad_medida, \
            cp.nom_categ_producto as nom_categ_producto \
        from producto p \
        join unidad_medida um on p.cod_unidad_medida = um.cod_unidad_medida \
        join categ_producto cp on p.cod_categ_producto = cp.cod_categ_producto \
        order by p.nom_producto asc"

    db = await get_db_connection()
    if db is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al conectar a la base de datos")

    try:
        values = ()
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
    producto: Producto = None
    productos: List[Producto] = []
    for row in result:
        producto = Producto(id_producto=row[0],
                            nom_producto=row[1],
                            precio=row[2],
                            cod_unidad_medida=row[3],
                            cod_categ_producto=row[4],
                            nom_unidad_medida=row[5],
                            nom_categ_producto=row[6])
        productos.append(producto)

    return productos
