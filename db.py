import os
from typing import Generator
from contextlib import contextmanager

import mysql.connector
from dotenv import load_dotenv


load_dotenv(".env.local")


def _obtener_conexion_base() -> mysql.connector.MySQLConnection:
    """
    Conexión sin base de datos seleccionada, usada para crearla si no existe.
    """
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
    )


def asegurar_base_datos_existe() -> None:
    """
    Crea la base de datos definida en MYSQL_DATABASE si no existe.
    """
    nombre_bd = os.getenv("MYSQL_DATABASE")
    if not nombre_bd:
        raise RuntimeError("MYSQL_DATABASE no está definida en las variables de entorno.")

    conexion = _obtener_conexion_base()
    cursor_bd = conexion.cursor()
    try:
        cursor_bd.execute(
            f"CREATE DATABASE IF NOT EXISTS `{nombre_bd}` DEFAULT CHARACTER SET utf8mb4"
        )
        conexion.commit()
    finally:
        cursor_bd.close()
        conexion.close()


def obtener_conexion_bd() -> mysql.connector.MySQLConnection:
    """
    Crea y devuelve una nueva conexión MySQL usando variables de entorno.

    Variables de entorno requeridas:
      - MYSQL_HOST
      - MYSQL_PORT
      - MYSQL_USER
      - MYSQL_PASSWORD
      - MYSQL_DATABASE
    """
    asegurar_base_datos_existe()
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )


@contextmanager
def obtener_cursor() -> Generator[mysql.connector.cursor.MySQLCursor, None, None]:
    """
    Generador de contexto que devuelve un cursor y asegura el cierre de recursos.
    Uso:

        with obtener_cursor() as cursor_bd:
            cursor_bd.execute("SELECT 1")
            print(cursor_bd.fetchone())
    """
    conexion = obtener_conexion_bd()
    cursor_bd = conexion.cursor(dictionary=True)
    try:
        yield cursor_bd
        conexion.commit()
    finally:
        cursor_bd.close()
        conexion.close()


def probar_conexion_simple() -> None:
    """
    Prueba rápida que abre una conexión y muestra la versión de MySQL.
    """
    with obtener_cursor() as cursor_bd:
        cursor_bd.execute("SELECT VERSION() AS version")
        fila = cursor_bd.fetchone()
        print(f"Versión de MySQL: {fila['version']}")


def probar_consulta_basica() -> None:
    """
    Prueba básica que ejecuta SELECT 1 y muestra el resultado.
    """
    with obtener_cursor() as cursor_bd:
        cursor_bd.execute("SELECT 1 AS resultado")
        fila = cursor_bd.fetchone()
        print(f"Resultado de SELECT 1: {fila['resultado']}")


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


def obtener_nombres_columnas(table_name: str) -> list:
    """
    Retorna los nombres de las columnas de una tabla específica.
    
    Args:
        table_name (str): El nombre de la tabla.
    
    Returns:
        list: Lista de strings con los nombres de las columnas.
    """
    with obtener_cursor() as cursor_bd:
        cursor_bd.execute(f"DESCRIBE {table_name}")
        columnas = cursor_bd.fetchall()
        return [columna['Field'] for columna in columnas]


if __name__ == "__main__":
    print("Ejecutando pruebas de conexión desde db.py...")
    probar_conexion_simple()
    probar_consulta_basica()
    print(obtener_nombres_columnas('visitas_raw'))