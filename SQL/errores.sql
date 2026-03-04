-- Crear base de datos "vinkos_raw" si no existe
CREATE DATABASE IF NOT EXISTS vinkos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE vinkos;

-- Crear tabla visitas_raw
CREATE TABLE IF NOT EXISTS errores (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    registro TEXT NOT NULL,
    archivoOrigen VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;