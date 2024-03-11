import typing
import strawberry
import requests
import os
import uuid

from datetime import datetime


PDA_CATASTRO_URL = os.getenv(
    "PDA_CATASTRO_URL", default="http://127.0.0.1:3000/catastros")
PDA_CONTRATO_URL = os.getenv(
    "PDA_CONTRATO_URL", default="http://127.0.0.1:3002/contratos")


def obtener_catastros(root) -> typing.List["Catastro"]:
    print('Consultando catastros')
    catastros_json = requests.get(PDA_CATASTRO_URL).json()
    catastros = []

    for catastro in catastros_json:
        catastros.append(
            Catastro(
                id_propiedad=catastro.get('id_propiedad'),
                numero_catastro=catastro.get('numero_catastro'),
                fecha_creacion=catastro.get('fecha_creacion'),
                fecha_actualizacion=catastro.get('fecha_actualizacion'))
        )

    return catastros


def obtener_contratos(root) -> typing.List["Contrato"]:
    print('Consultando contratos')
    contratos_json = requests.get(PDA_CONTRATO_URL).json()
    contratos = []
    for contrato in contratos_json:
        contratos.append(
            Contrato(
                id_propiedad=contrato.get('propiedad_id'),
                numero_contrato=contrato.get('numero_contrato'),
                fecha_creacion=contrato.get('fecha_creacion'),
                fecha_actualizacion=contrato.get('fecha_actualizacion'))
        )

    return contratos


@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int


@strawberry.type
class Catastro:
    id_propiedad: str
    numero_catastro: str
    fecha_creacion: str
    fecha_actualizacion: str


@strawberry.type
class Contrato:
    id_propiedad: str
    numero_contrato: str
    fecha_creacion: str
    fecha_actualizacion: str
