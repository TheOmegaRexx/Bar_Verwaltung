-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server-Version:               10.4.27-MariaDB - mariadb.org binary distribution
-- Server-Betriebssystem:        Win64
-- HeidiSQL Version:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Exportiere Datenbank-Struktur für barverwaltung
CREATE DATABASE IF NOT EXISTS `barverwaltung` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `barverwaltung`;

-- Exportiere Struktur von Tabelle barverwaltung.getraenke
CREATE TABLE IF NOT EXISTS `getraenke` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `preis` decimal(5,2) NOT NULL,
  `menge` int(11) NOT NULL,
  `liter` int(11) NOT NULL,
  `alkohol` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Exportiere Daten aus Tabelle barverwaltung.getraenke: ~10 rows (ungefähr)
DELETE FROM `getraenke`;
INSERT INTO `getraenke` (`id`, `name`, `preis`, `menge`, `liter`, `alkohol`) VALUES
	(1, 'Bier', 2.50, 50, 1, 1),
	(2, 'Cola', 1.20, 100, 1, 0),
	(3, 'Wein', 5.75, 20, 1, 1),
	(4, 'Wasser', 0.80, 200, 2, 0),
	(5, 'Whisky', 12.50, 10, 1, 1),
	(6, 'Limonade', 1.00, 80, 1, 0),
	(7, 'Rum', 8.75, 15, 1, 1),
	(8, 'Orangensaft', 1.50, 30, 1, 0),
	(9, 'Gin', 10.00, 12, 1, 1),
	(10, 'Eistee', 1.25, 60, 1, 0);

-- Exportiere Struktur von Tabelle barverwaltung.nachrichten
CREATE TABLE IF NOT EXISTS `nachrichten` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nachricht` text NOT NULL,
  `datum` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Exportiere Daten aus Tabelle barverwaltung.nachrichten: ~0 rows (ungefähr)
DELETE FROM `nachrichten`;

-- Exportiere Struktur von Tabelle barverwaltung.rauchwaren
CREATE TABLE IF NOT EXISTS `rauchwaren` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `preis` decimal(6,2) NOT NULL,
  `menge` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Exportiere Daten aus Tabelle barverwaltung.rauchwaren: ~10 rows (ungefähr)
DELETE FROM `rauchwaren`;
INSERT INTO `rauchwaren` (`id`, `name`, `preis`, `menge`) VALUES
	(1, 'Zigaretten', 6.50, 10),
	(2, 'Zigarren', 15.00, 5),
	(3, 'Pfeifentabak', 8.25, 8),
	(4, 'Zigarillos', 9.75, 12),
	(5, 'Wasserpfeifentabak', 12.50, 7),
	(6, 'Zigarrenillos', 7.80, 15),
	(7, 'Zigarettenfilter', 1.20, 50),
	(8, 'Feuerzeug', 2.50, 3),
	(9, 'Pfeife', 5.00, 2),
	(10, 'Tabakbeutel', 3.75, 5);

-- Exportiere Struktur von Tabelle barverwaltung.snacks
CREATE TABLE IF NOT EXISTS `snacks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `preis` decimal(4,2) NOT NULL,
  `menge` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Exportiere Daten aus Tabelle barverwaltung.snacks: ~10 rows (ungefähr)
DELETE FROM `snacks`;
INSERT INTO `snacks` (`id`, `name`, `preis`, `menge`) VALUES
	(1, 'Chips', 1.50, 30),
	(2, 'Schokolade', 0.80, 20),
	(3, 'Nüsse', 2.00, 25),
	(4, 'Cracker', 1.20, 40),
	(5, 'Popcorn', 1.00, 35),
	(6, 'Pretzels', 1.30, 28),
	(7, 'Gummibärchen', 0.75, 50),
	(8, 'Kekse', 1.10, 22),
	(9, 'Gemüsesticks', 2.50, 15),
	(10, 'Dip', 1.75, 18);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
