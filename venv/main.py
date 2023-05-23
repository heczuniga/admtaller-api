
# Bibliotecas generales
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

# Instanciamos la aplicación
api = fastapi.FastAPI()


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


# Método de configuración general, que llama a los otros sub-métodos
# de configuración
def configura():
    configura_routers()


configura()
