-- Crear base de datos "vinkos_raw" si no existe
CREATE DATABASE IF NOT EXISTS vinkos
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE vinkos;

-- Crear tabla visitas_raw
CREATE TABLE IF NOT EXISTS visitas_raw (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(320) NULL,
    `jyv` VARCHAR(320) NULL,
    `Badmail` VARCHAR(320) NULL,
    `Baja` VARCHAR(320) NULL,
    `Fecha envio` VARCHAR(320) NULL,
    `Fecha open` VARCHAR(320) NULL,
    `Opens` VARCHAR(320) NULL,
    `Opens virales` VARCHAR(320) NULL,
    `Fecha click` VARCHAR(320) NULL,
    `Clicks` VARCHAR(320) NULL,
    `Clicks virales` VARCHAR(320) NULL,
    `Links` VARCHAR(320) NULL,
    `IPs` VARCHAR(320) NULL,
    `Navegadores` VARCHAR(320) NULL,
    `Plataformas` VARCHAR(320) NULL,
    `archivo origen` VARCHAR(320) NULL,
    `data rescatada` TEXT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;