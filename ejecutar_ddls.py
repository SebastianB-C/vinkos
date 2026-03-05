"""
Script para ejecutar los archivos DDL de la carpeta SQL
contra la base de datos configurada en .env.local.
"""
from pathlib import Path

from db import obtener_conexion_bd


def ejecutar_sql(path_sql: Path) -> None:
    """
    Lee un archivo .sql y ejecuta sus sentencias separadas por ';'.
    Ignora líneas vacías/comentarios simples.
    """
    print(f"-> Ejecutando DDL desde: {path_sql}")
    contenido = path_sql.read_text(encoding="utf-8")

    conexion = obtener_conexion_bd()
    cursor_bd = conexion.cursor()
    try:
        # Separar por ';' y ejecutar cada sentencia no vacía.
        for sentencia in contenido.split(";"):
            stmt = sentencia.strip()
            if not stmt:
                continue
            cursor_bd.execute(stmt)
        conexion.commit()
        print(f"   OK: {path_sql.name}")
    finally:
        cursor_bd.close()
        conexion.close()


def main() -> None:
    carpeta_sql = Path("SQL")
    archivos = [
        "vinkos_raw.sql",
        "visitante.sql",
        "errores.sql",
        "estadistica.sql",
    ]

    for nombre in archivos:
        ruta = carpeta_sql / nombre
        if not ruta.is_file():
            print(f"!! Archivo no encontrado, se omite: {ruta}")
            continue
        ejecutar_sql(ruta)

    print("Ejecución de DDLs finalizada.")


if __name__ == "__main__":
    main()

