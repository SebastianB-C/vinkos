## Ejemplo Python + MySQL

Este es un proyecto mínimo en Python que se conecta a una base de datos MySQL usando variables de entorno.

### 1. Crear y activar un entorno virtual (recomendado)

```bash
cd C:\vinkos
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la conexión a la base de datos

El programa lee las variables desde el archivo `.env.local` ubicado en la raíz del proyecto.

Edita (o crea) el archivo `.env.local` con tus credenciales de MySQL:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=tu_usuario_mysql
MYSQL_PASSWORD=tu_contraseña_mysql
MYSQL_DATABASE=nombre_de_tu_base
```

Asegúrate de tener un servidor MySQL en ejecución.  
Si la base de datos indicada en `MYSQL_DATABASE` no existe, el programa la creará automáticamente.

### 4. Probar la conexión

Ejecuta:

```bash
python main.py
```

Deberías ver la versión de MySQL y la lista de tablas de la base de datos (o un mensaje indicando que no hay tablas).
