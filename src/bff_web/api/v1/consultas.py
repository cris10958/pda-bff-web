
import strawberry
from .esquemas import *


@strawberry.type
class Query:
    catastros: typing.List[Catastro] = strawberry.field(
        resolver=obtener_catastros)

    contratos: typing.List[Contrato] = strawberry.field(
        resolver=obtener_contratos)
