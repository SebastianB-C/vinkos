"""
Módulo para cargar archivos de visitas a la tabla vinkos.visitas_raw usando pandas.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from db import obtener_nombres_columnas

load_dotenv(".env.local")

def _crear_engine_mysql():
    """
    Crea un engine de SQLAlchemy usando mysql-connector y variables de entorno.

    Se usa connect_args para evitar problemas de caracteres especiales
    en usuario/contraseña (por ejemplo '@').
    """
    host = os.getenv("MYSQL_HOST")
    port = int(os.getenv("MYSQL_PORT"))
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DATABASE")

    if not user or not password:
        raise RuntimeError("MYSQL_USER y MYSQL_PASSWORD deben estar definidos en .env.local")

    return create_engine(
        "mysql+mysqlconnector://",
        connect_args={
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database,
        },
    )


def cargar_archivos_en_visitas_raw(archivos: Iterable[Path]) -> int:
    """
    Carga los archivos de visitas a la tabla visitas_raw.

    Returns:
        Número total de filas insertadas.
    """

    # Si no hay archivos, retornar 0 inmediatamente para evitar crear conexión innecesaria
    archivos = list(archivos)
    if not archivos:
        return 0

    sep = os.getenv("VISITAS_CSV_SEP")
    engine = _crear_engine_mysql()
    total_filas = 0

    for archivo in archivos:
        if not archivo.is_file():
            continue

        print(f"Cargando archivo en visitas_raw desde: {archivo}")
        df = pd.read_csv(
            archivo,
            sep=sep,
            dtype=str,
            encoding="utf-8",
            keep_default_na=False,
        )

        # Agregar columna 'archivo_origen' con el nombre del archivo
        df["archivo_origen"] = archivo.name

        # Agregar columna 'data_rescatada'
        df["data_rescatada"] = ""

        # Renombrar columnas del DataFrame: reemplazar espacios por guiones bajos y convertir a minúsculas
        df.columns = [col.replace(' ', '_').lower() for col in df.columns]

        # Normalizar columnas destino a minúsculas para comparación
        columnas_destino = obtener_nombres_columnas("visitas_raw")
        columnas_destino_minusculas = [col.lower() for col in columnas_destino]

        # Identificar columnas desconocidas (no en la tabla destino)
        columnas_desconocidas = [c for c in df.columns if c not in columnas_destino_minusculas]

        # Construir 'data_rescatada' con nombre y valor de cada columna desconocida
        if columnas_desconocidas:
            print(f"Columnas no definidas en visitas_raw, se registrarán en 'data_rescatada': \
                  {columnas_desconocidas}"
            )

            # Concatenar nombre y valor de cada columna desconocida en 'data_rescatada'
            df["data_rescatada"] = df[columnas_desconocidas].apply(
                lambda fila: ", ".join(
                    f"{col}={fila[col]}" for col in columnas_desconocidas
                ),
                axis=1,
            )

            # Eliminar columnas desconocidas del DataFrame antes de insertar
            df = df.drop(columns=columnas_desconocidas)

        # Insertar en la tabla visitas_raw
        df.to_sql(
            "visitas_raw",
            con=engine,
            if_exists="append",
            index=False,
        )

        total_filas += len(df)

    return total_filas

