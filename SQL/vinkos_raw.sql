-- Crear base de datos "vinkos_raw" si no existe
CREATE DATABASE IF NOT EXISTS vinkos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE vinkos;

-- Crear tabla visitas_raw
CREATE TABLE IF NOT EXISTS visitas_raw (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(320) NULL,
    jyv VARCHAR(320) NULL,
    Badmail VARCHAR(320) NULL,
    Baja VARCHAR(320) NULL,
    Fecha_envio VARCHAR(320) NULL,
    Fecha_open VARCHAR(320) NULL,
    Opens VARCHAR(320) NULL,
    Opens_virales VARCHAR(320) NULL,
    Fecha_click VARCHAR(320) NULL,
    Clicks VARCHAR(320) NULL,
    Clicks_virales VARCHAR(320) NULL,
    Links VARCHAR(320) NULL,
    IPs VARCHAR(320) NULL,
    Navegadores VARCHAR(320) NULL,
    Plataformas VARCHAR(320) NULL,
    archivo_origen VARCHAR(320) NULL,
    data_rescatada TEXT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;