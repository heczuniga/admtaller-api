
from pydantic import BaseModel
from typing import Optional


# Se genera el modelo base que permite recuperar información del error con un simple to_dict()
class APIBaseModel(BaseModel):

    # Para retornar errores y mensajes de éxito
    msg_error: Optional[str] = None
    msg_exito: Optional[str] = None
