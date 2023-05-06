
# Bibliotecas generales
import fastapi

# Importación de routers
from api import autenticacion
from api import usuarios
from api import principal
from api import asignaturas
from api import programacion
from api import reportes
from api import productos
from api import registro
from api import talleres

# Instanciamos la aplicación
api = fastapi.FastAPI()


# Método de configuración de routers
def configura_routers():
    api.include_router(autenticacion.router)
    api.include_router(usuarios.router)
    api.include_router(principal.router)
    api.include_router(asignaturas.router)
    api.include_router(programacion.router)
    api.include_router(reportes.router)
    api.include_router(productos.router)
    api.include_router(registro.router)
    api.include_router(talleres.router)


# Método de configuración general, que llama a los otros sub-métodos
# de configuración
def configura():
    configura_routers()


configura()
