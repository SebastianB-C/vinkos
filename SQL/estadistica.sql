-- Crear base de datos "vinkos" si no existe
CREATE DATABASE IF NOT EXISTS vinkos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE vinkos;

-- Crear tabla estadistica
CREATE TABLE IF NOT EXISTS estadistica (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(320) NOT NULL,
    jyv VARCHAR(50) NULL,
    Badmail TINYINT(1) NULL,
    Baja TINYINT(1) NULL,
    FechaEnvio DATETIME NULL,
    FechaOpen DATETIME NULL,
    Opens INT NULL,
    OpensVirales INT NULL,
    FechaClick DATETIME NULL,
    Clicks INT NULL,
    ClicksVirales INT NULL,
    Links INT NULL,
    IPs INT NULL,
    Navegadores VARCHAR(255) NULL,
    Plataformas VARCHAR(255) NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;