-- Crear base de datos "vinkos_raw" si no existe
CREATE DATABASE IF NOT EXISTS vinkos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE vinkos;

-- Crear tabla visitas_raw
CREATE TABLE IF NOT EXISTS visitantes (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(320) UNIQUE NOT NULL,
    fechaPrimeraVisita DATETIME NULL,
    fechaUltimaVisita DATETIME NULL,
    visitasTotales INT UNSIGNED NULL,
    visitasAnioActual INT UNSIGNED NULL,
    visitasMesActual INT UNSIGNED NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;