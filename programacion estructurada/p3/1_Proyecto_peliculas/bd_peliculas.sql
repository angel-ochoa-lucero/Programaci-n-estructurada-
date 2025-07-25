-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2025 a las 08:22:22
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_utd_2a_class`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bd_peliculas`
--

CREATE TABLE `bd_peliculas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `categoria` varchar(100) NOT NULL,
  `clasificacion` varchar(100) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `idioma` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bd_peliculas`
--

INSERT INTO `bd_peliculas` (`id`, `nombre`, `categoria`, `clasificacion`, `genero`, `idioma`) VALUES
(1, 'La Bella y la Bestia', 'infantil', 'A', 'fantasia', 'Español'),
(2, 'La Noche del Demonio ', 'Juvenil', 'B', 'Terror', 'Ingles'),
(3, 'Piratas del Caribe', 'juvenil', 'B', 'Fantasia', 'Español'),
(4, 'Tusk ', 'Adultos', 'C', 'Terror', 'Ingles '),
(5, 'La Dama de Negro ', 'Juvenil', 'B', 'Terror', 'Español\r\n');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bd_peliculas`
--
ALTER TABLE `bd_peliculas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bd_peliculas`
--
ALTER TABLE `bd_peliculas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
