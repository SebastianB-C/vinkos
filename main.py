from db import obtener_cursor
from lector_archivos import (
    listar_archivos,
    obtener_ruta_directorio,
    leer_contenido_archivo,
)
from backup import crear_backup_zip, obtener_ruta_directorio_backup
from carga_visitas_raw import cargar_archivos_en_visitas_raw


def listar_y_leer_archivos_visitas() -> None:
    """
    Lista los archivos en el directorio de archivos de visitas y muestra
    un resumen (nombre y tamaño). Si hay archivos, muestra las primeras
    líneas del primero como ejemplo de lectura.
    """
    directorio = obtener_ruta_directorio()
    print(f"Directorio: {directorio}")

    if not directorio.is_dir():
        print("El directorio no existe o no es accesible.")
        return

    archivos = listar_archivos()
    if not archivos:
        print("No hay archivos en el directorio.")
        return

    print(f"Archivos encontrados (patrón válido): {len(archivos)}")
    for archivo in archivos:
        tamaño = archivo.stat().st_size
        print(f"  - {archivo.name} ({tamaño} bytes)")

    # Cargar datos en la tabla visitas_raw usando pandas
    total_insertados = cargar_archivos_en_visitas_raw(archivos)
    print(f"\nFilas insertadas en visitas_raw: {total_insertados}")

    # Backup: generar ZIP con los archivos en el directorio de backup
    ruta_zip = crear_backup_zip(archivos)
    if ruta_zip:
        print(f"Backup creado: {ruta_zip}")

        # Eliminar archivos fuente solo si el backup se creó correctamente
        print("Eliminando archivos fuente del directorio de origen...")
        for archivo in archivos:
            try:
                archivo.unlink()
                print(f"  Archivo eliminado: {archivo.name}")
            except OSError as e:
                print(f"  No se pudo eliminar '{archivo}': {e}")
    else:
        print("No se generó backup (sin archivos).")

if __name__ == "__main__":
    print("=== Archivos de visitas (directorio local) ===")
    listar_y_leer_archivos_visitas()

