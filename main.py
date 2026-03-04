from db import obtener_cursor
from lector_archivos import (
    listar_archivos,
    obtener_ruta_directorio,
    leer_contenido_archivo,
)
from backup import crear_backup_zip, obtener_ruta_directorio_backup


def probar_conexion() -> None:
    """
    Consulta sencilla para verificar que la conexión a MySQL funciona.
    """
    with obtener_cursor() as cursor_bd:
        cursor_bd.execute("SELECT VERSION() AS version")
        fila = cursor_bd.fetchone()
        print(f"¡Conectado! Versión de MySQL: {fila['version']}")


def listar_tablas() -> None:
    """
    Ejemplo de consulta que lista las tablas de la base de datos actual.
    """
    with obtener_cursor() as cursor_bd:
        cursor_bd.execute("SHOW TABLES")
        filas = cursor_bd.fetchall()
        if not filas:
            print("No se encontraron tablas en la base de datos.")
        else:
            print("Tablas en la base de datos:")
            for fila in filas:
                # Cada fila es un diccionario con una sola clave (nombre de la tabla)
                print(" -", list(fila.values())[0])


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

    print(f"Archivos encontrados: {len(archivos)}")
    for archivo in archivos:
        tamaño = archivo.stat().st_size
        print(f"  - {archivo.name} ({tamaño} bytes)")

    # Backup: generar ZIP con los archivos en el directorio de backup
    ruta_zip = crear_backup_zip(archivos)
    if ruta_zip:
        print(f"\nBackup creado: {ruta_zip}")

        # Eliminar archivos fuente solo si el backup se creó correctamente
        print("Eliminando archivos fuente del directorio de origen...")
        for archivo in archivos:
            try:
                archivo.unlink()
                print(f"  Archivo eliminado: {archivo.name}")
            except OSError as e:
                print(f"  No se pudo eliminar '{archivo}': {e}")
    else:
        print("\nNo se generó backup (sin archivos).")

    # Ejemplo: leer las primeras líneas del primer archivo (si es texto)
    primer_archivo = archivos[0]
    try:
        contenido = leer_contenido_archivo(primer_archivo)
        lineas = contenido.strip().splitlines()[:5]
        print(f"\nPrimeras líneas de '{primer_archivo.name}':")
        for linea in lineas:
            print(f"  {linea[:80]}{'...' if len(linea) > 80 else ''}")
    except (UnicodeDecodeError, OSError) as e:
        print(f"\n(No se muestra contenido de '{primer_archivo.name}': {e})")


if __name__ == "__main__":
    print("=== Archivos de visitas (directorio local) ===")
    listar_y_leer_archivos_visitas()
    print()
    print("=== Conexión MySQL ===")
    probar_conexion()
    print()
    listar_tablas()

