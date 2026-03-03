"""
Módulo para leer archivos desde un directorio local (p. ej. archivos de visitas).
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(".env.local")

# Ruta por defecto; puede sobrescribirse con DIR_ARCHIVOS_VISITAS en .env.local
RUTA_ARCHIVOS_VISITAS = os.getenv(
    "DIR_ARCHIVOS_VISITAS",
    r"C:\home\vinkOS\archivosVisitas",
)


def obtener_ruta_directorio() -> Path:
    """
    Devuelve la ruta del directorio de archivos de visitas como Path.
    """
    return Path(RUTA_ARCHIVOS_VISITAS)


def listar_archivos(en_subdirectorios: bool = False) -> list[Path]:
    """
    Lista los archivos en el directorio de archivos de visitas.

    Args:
        en_subdirectorios: Si es True, incluye archivos en subdirectorios (recursivo).

    Returns:
        Lista de Path con la ruta completa de cada archivo (solo archivos, no carpetas).
    """
    directorio = obtener_ruta_directorio()
    if not directorio.is_dir():
        return []

    if en_subdirectorios:
        return [p for p in directorio.rglob("*") if p.is_file()]
    return [p for p in directorio.iterdir() if p.is_file()]


def leer_contenido_archivo(ruta: Path | str, codificacion: str = "utf-8") -> str:
    """
    Lee el contenido de un archivo como texto.

    Args:
        ruta: Ruta del archivo (Path o str).
        codificacion: Codificación del archivo (por defecto utf-8).

    Returns:
        Contenido del archivo como string.
    """
    path = Path(ruta)
    return path.read_text(encoding=codificacion)


def leer_bytes_archivo(ruta: Path | str) -> bytes:
    """
    Lee el contenido de un archivo en modo binario.

    Args:
        ruta: Ruta del archivo (Path o str).

    Returns:
        Contenido del archivo como bytes.
    """
    path = Path(ruta)
    return path.read_bytes()
