import strawberry

from strawberry.types import Info
from src.bff_web import utils
from src.bff_web.despachadores import Despachador

from .esquemas import *

SCHEMA = "public/default/"
COMANDO_CREAR_PROPIEDAD = "ComandoCrearPropiedad"
TOPICO_COMANDO_CREAR_PROPIEDAD = 'comandos-crear-propiedad'
SCHEMA_COMANDO_CREAR_PROPIEDAD = f'{SCHEMA}{TOPICO_COMANDO_CREAR_PROPIEDAD}'


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_propiedad(self, id_propiedad: str, info: Info) -> PropiedadRespuesta:
        print(f"Mutacion crear propiedad ID: {id_propiedad}")

        payload = dict(
            id_propiedad=id_propiedad,
        )

        comando = dict(
            id=str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion="v1",
            type=COMANDO_CREAR_PROPIEDAD,
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name="BFF Web",
            data=payload
        )

        despachador = Despachador()
        info.context["background_tasks"].add_task(
            despachador.publicar_mensaje, comando, TOPICO_COMANDO_CREAR_PROPIEDAD, SCHEMA_COMANDO_CREAR_PROPIEDAD)

        return PropiedadRespuesta(mensaje="Creando propiedad", codigo=203)
