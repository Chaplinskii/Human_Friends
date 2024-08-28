-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Авг 16 2024 г., 08:54
-- Версия сервера: 8.0.39-0ubuntu0.24.04.1
-- Версия PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Human_Friends`
--

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`%`@`localhost` PROCEDURE `proc_delete` (OUT `tran_result` VARCHAR(100), IN `u_id` INT(45))  SQL SECURITY INVOKER BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0$$

CREATE DEFINER=`%`@`localhost` PROCEDURE `proc_get_all` (OUT `tran_result` VARCHAR(100))  SQL SECURITY INVOKER BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0$$

CREATE DEFINER=`%`@`localhost` PROCEDURE `proc_insert` (OUT `tran_result` VARCHAR(100), IN `u_name` VARCHAR(45), IN `u_date_birthday` DATE, IN `u_id_class` VARCHAR(45), IN `u_id_species` VARCHAR(45), IN `u_commands` TEXT)   BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0$$

CREATE DEFINER=`%`@`localhost` PROCEDURE `proc_update` (IN `u_id` INT, IN `u_name` VARCHAR(45), IN `u_date_birthday` DATE, IN `u_id_class` VARCHAR(45), IN `u_id_species` VARCHAR(45), IN `u_commands` TEXT, OUT `tran_result` VARCHAR(100))   BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `animals`
--

CREATE TABLE `animals` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `date_birthday` date NOT NULL,
  `id_class` int NOT NULL,
  `id_species` int NOT NULL,
  `commands` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `animals`
--

INSERT INTO `animals` (`id`, `name`, `date_birthday`, `id_class`, `id_species`, `commands`) VALUES
(8, 'Eeyore', '2017-09-19', 2, 6, 'Walk, Carry Load, Bray'),
(9, 'Fido', '2020-01-01', 1, 1, 'Sit, Stay, Fetch'),
(10, 'Thunder', '2015-07-21', 2, 4, 'Sit, Stay, Fetch'),
(11, 'Sandy', '2016-11-03', 2, 5, 'Walk, Carry Load');

--
-- Триггеры `animals`
--
DELIMITER $$
CREATE TRIGGER `animal_DELETE` AFTER DELETE ON `animals` FOR EACH ROW INSERT INTO log set record_ID = old.id, operation = 'DELETE'
$$
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `animal_INSERT` AFTER INSERT ON `animals` FOR EACH ROW INSERT INTO log
set record_ID = new.id, operation = 'INSERT'
$$
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `animals_UPDATE` AFTER UPDATE ON `animals` FOR EACH ROW INSERT INTO log set record_ID = new.id, operation = 'UPDATE'
$$
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `class`
--

CREATE TABLE `class` (
  `id` int NOT NULL,
  `class` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `class`
--

INSERT INTO `class` (`id`, `class`) VALUES
(2, 'Pack animals'),
(1, 'Pets');

-- --------------------------------------------------------

--
-- Структура таблицы `log`
--

CREATE TABLE `log` (
  `id` int NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `record_ID` int NOT NULL,
  `operation` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `log`
--

INSERT INTO `log` (`id`, `date`, `record_ID`, `operation`) VALUES
(12, '2024-08-12 12:06:33', 9, 'INSERT'),
(13, '2024-08-12 12:07:17', 6, 'DELETE'),
(14, '2024-08-12 12:13:08', 8, 'UPDATE'),
(15, '2024-08-14 12:58:09', 10, 'INSERT'),
(16, '2024-08-14 13:02:38', 11, 'INSERT'),
(17, '2024-08-14 13:16:01', 14, 'INSERT'),
(18, '2024-08-14 13:19:41', 14, 'DELETE'),
(19, '2024-08-14 14:33:26', 10, 'UPDATE');

-- --------------------------------------------------------

--
-- Структура таблицы `log_err`
--

CREATE TABLE `log_err` (
  `id` int NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `error` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `log_err`
--

INSERT INTO `log_err` (`id`, `date`, `error`) VALUES
(1, '2024-08-14 12:49:23', 'УПС. Ошибка: 42S22 Текст ошибки: Неизвестный столбец \'u_name\' в \'field list\''),
(2, '2024-08-14 13:07:09', 'УПС. Ошибка: 21000 Текст ошибки: Операнд должен содержать 1 колонок'),
(3, '2024-08-14 13:09:44', 'УПС. Ошибка: 21000 Текст ошибки: Операнд должен содержать 1 колонок'),
(4, '2024-08-15 22:22:40', 'Error: 42S22 Text error: Неизвестный столбец \'u_id_class\' в \'where clause\'');

-- --------------------------------------------------------

--
-- Структура таблицы `species`
--

CREATE TABLE `species` (
  `id` int NOT NULL,
  `species` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `species`
--

INSERT INTO `species` (`id`, `species`) VALUES
(5, 'Camel'),
(2, 'Cat'),
(1, 'Dog'),
(6, 'Donkey'),
(3, 'Hamster'),
(4, 'Horse');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `animals`
--
ALTER TABLE `animals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_class` (`id_class`),
  ADD KEY `id_species` (`id_species`);

--
-- Индексы таблицы `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `class` (`class`);

--
-- Индексы таблицы `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `log_err`
--
ALTER TABLE `log_err`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `species`
--
ALTER TABLE `species`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `species` (`species`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `animals`
--
ALTER TABLE `animals`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT для таблицы `class`
--
ALTER TABLE `class`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `log`
--
ALTER TABLE `log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT для таблицы `log_err`
--
ALTER TABLE `log_err`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `species`
--
ALTER TABLE `species`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `animals`
--
ALTER TABLE `animals`
  ADD CONSTRAINT `animals_ibfk_1` FOREIGN KEY (`id_class`) REFERENCES `class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `animals_ibfk_2` FOREIGN KEY (`id_species`) REFERENCES `species` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
