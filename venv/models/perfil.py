
from pydantic import BaseModel
from typing import Optional


class Perfil(BaseModel):
    cod_perfil: int
    nom_perfil: str
    cod_carrera: Optional[int] = None
    nom_carrera: Optional[str] = None


class ItemMenu(BaseModel):
    cod_item_menu: str
    cod_item_menu_padre: Optional[str]
    nom_item_menu: str
    url: Optional[str]
    nivel: int
