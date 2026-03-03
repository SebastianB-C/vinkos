from db import obtener_cursor


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


if __name__ == "__main__":
    print("Probando conexión a MySQL...")
    probar_conexion()
    print()
    listar_tablas()

