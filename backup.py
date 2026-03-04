"""
Módulo para generar backups en ZIP de los archivos de visitas.
"""
import os
from datetime import datetime
from pathlib import Path

import zipfile
from dotenv import load_dotenv

load_dotenv(".env.local")

# Directorio donde se guardan los ZIP de backup
RUTA_BACKUP_VISITAS = os.getenv(
    "DIR_BACKUP_VISITAS"
)


def obtener_ruta_directorio_backup() -> Path:
    """
    Devuelve la ruta del directorio de backups como Path.
    """
    return Path(RUTA_BACKUP_VISITAS)


def crear_backup_zip(archivos: list[Path], nombre_base: str = "backup_visitas") -> Path | None:
    """
    Crea un archivo ZIP con los archivos indicados y lo guarda en el directorio de backup.

    Crea el directorio de backup si no existe. El nombre del ZIP incluye fecha y hora
    para no sobrescribir backups anteriores.

    Args:
        archivos: Lista de rutas (Path) de archivos a incluir en el ZIP.
        nombre_base: Prefijo del nombre del archivo ZIP (por defecto "backup_visitas").

    Returns:
        Path del archivo ZIP creado, o None si no había archivos que incluir.
    """
    if not archivos:
        return None

    directorio_backup = obtener_ruta_directorio_backup()
    directorio_backup.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_zip = f"{nombre_base}_{timestamp}.zip"
    ruta_zip = directorio_backup / nombre_zip

    with zipfile.ZipFile(ruta_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for archivo in archivos:
            if archivo.is_file():
                # Se guarda en el ZIP solo con el nombre del archivo (sin rutas absolutas)
                zf.write(archivo, arcname=archivo.name)

    return ruta_zip
