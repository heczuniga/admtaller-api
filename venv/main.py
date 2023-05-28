
import aiomysql
import fastapi

# Importación de routers
from api import autenticacion
from api import usuario
from api import perfil
from api import principal
from api import asignatura
from api import programacion
from api import reporte
from api import producto
from api import registro
from api import taller
from api import carrera
from api import param
from database import get_db_connection

# Instanciamos la aplicación
api = fastapi.FastAPI()
db = None


# Método de configuración de routers
def configura_routers():
    api.include_router(autenticacion.router)
    api.include_router(usuario.router)
    api.include_router(perfil.router)
    api.include_router(principal.router)
    api.include_router(asignatura.router)
    api.include_router(programacion.router)
    api.include_router(reporte.router)
    api.include_router(producto.router)
    api.include_router(registro.router)
    api.include_router(taller.router)
    api.include_router(carrera.router)
    api.include_router(param.router)


async def configura_db():
    global db
    try:
        # Obtiene la conexión a la base de datos desde el módulo database
        conn = await get_db_connection()
        # Asigna la conexión a la variable global db
        db = conn
    except aiomysql.Error as e:
        # Maneja la excepción y muestra un mensaje de error personalizado
        print(f"Error al conectar a la base de datos: {e}")
        return None


# Método de configuración general, que llama a los otros sub-métodos
# de configuración
async def configura():
    await configura_db()
    configura_routers()


async def close_db_connection():
    global db
    if db is not None:
        db.close()
        await db.wait_closed()


api.add_event_handler("startup", configura)
api.add_event_handler("shutdown", close_db_connection)
