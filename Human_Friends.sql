-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: some-mysql
-- Время создания: Сен 01 2024 г., 19:48
-- Версия сервера: 8.0.31
-- Версия PHP: 8.2.8

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
CREATE DEFINER=`hacoc`@`localhost` PROCEDURE `proc_delete` (OUT `tran_result` VARCHAR(100), IN `u_id` INT(45))   BEGIN
    
    DECLARE `_rollback` BIT DEFAULT 0;
    DECLARE code varchar(100);
    DECLARE error_string varchar(100); 

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SET `_rollback` = 1;
        GET stacked DIAGNOSTICS CONDITION 1
            code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
    END;

    START TRANSACTION;
    
    DELETE FROM animals WHERE id = u_id;
    
    IF `_rollback` THEN
        SET tran_result = concat('Error: ', code, ' Text error: ', error_string);
        ROLLBACK;
        INSERT INTO log_err SET error = tran_result;
    ELSE
        SET tran_result = 'O K';
        COMMIT;
    END IF;
END$$

CREATE DEFINER=`hacoc`@`localhost` PROCEDURE `proc_get_all` (OUT `tran_result` VARCHAR(100))   BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0;
	DECLARE code varchar(100);
	DECLARE error_string varchar(100); 

	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
	BEGIN
 		SET `_rollback` = 1;
 		GET stacked DIAGNOSTICS CONDITION 1
			code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
	END;

	START TRANSACTION;
	
    SELECT animals.id, animals.name, animals.date_birthday, class.class, species.species, animals.commands FROM animals JOIN class ON id_class = class.id JOIN species ON id_species = species.id;

    
	IF `_rollback` THEN
		SET tran_result = concat('Error: ', code, ' Text error: ', error_string);
		ROLLBACK;
        INSERT INTO log_err SET error = tran_result;
	ELSE
		SET tran_result = 'O K';
		COMMIT;
	END IF;
END$$

CREATE DEFINER=`hacoc`@`localhost` PROCEDURE `proc_insert` (OUT `tran_result` VARCHAR(100), IN `u_name` VARCHAR(45), IN `u_date_birthday` DATE, IN `u_id_class` VARCHAR(45), IN `u_id_species` VARCHAR(45), IN `u_commands` TEXT)   BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0;
	DECLARE code varchar(100);
	DECLARE error_string varchar(100); 

	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
	BEGIN
 		SET `_rollback` = 1;
 		GET stacked DIAGNOSTICS CONDITION 1
			code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
	END;

	START TRANSACTION;
	
    INSERT INTO animals set name = u_name, date_birthday = u_date_birthday,  id_class = (SELECT class.id FROM class WHERE class = u_id_class), id_species=(SELECT species.id FROM species WHERE species = u_id_species), commands=u_commands;
    
	IF `_rollback` THEN
		SET tran_result = concat('Error: ', code, ' Text error: ', error_string);
		ROLLBACK;
        INSERT INTO log_err SET error = tran_result;
	ELSE
		SET tran_result = 'O K';
		COMMIT;
	END IF;
END$$

CREATE DEFINER=`hacoc`@`localhost` PROCEDURE `proc_update` (OUT `tran_result` VARCHAR(100), IN `u_id` INT, IN `u_name` VARCHAR(45), IN `u_date_birthday` DATE, IN `u_id_class` VARCHAR(45), IN `u_id_species` VARCHAR(45), IN `u_commands` TEXT)   BEGIN
	
	DECLARE `_rollback` BIT DEFAULT 0;
	DECLARE code varchar(100);
	DECLARE error_string varchar(100); 

	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
	BEGIN
 		SET `_rollback` = 1;
 		GET stacked DIAGNOSTICS CONDITION 1
			code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
	END;

	START TRANSACTION;
	
    UPDATE animals set name = u_name, date_birthday = u_date_birthday,  id_class = (SELECT class.id FROM class WHERE class = u_id_class), id_species=(SELECT species.id FROM species WHERE species = u_id_species), commands=u_commands WHERE id = u_id;
    
	IF `_rollback` THEN
		SET tran_result = concat('Error: ', code, ' Text error: ', error_string);
		ROLLBACK;
        INSERT INTO log_err SET error = tran_result;
	ELSE
		SET tran_result = 'O K';
		COMMIT;
	END IF;
END$$

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
(11, 'Sandy', '2016-11-03', 2, 5, 'Walk, Carry Load'),
(23, 'ghgvc', '1111-11-11', 2, 6, 'gchgc, hgc'),
(24, 'Hgc', '1111-11-11', 1, 1, '');

--
-- Триггеры `animals`
--
DELIMITER $$
CREATE TRIGGER `animal_DELETE` AFTER DELETE ON `animals` FOR EACH ROW INSERT INTO log set record_ID = old.id, operation = 'DELETE'
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `animal_INSERT` AFTER INSERT ON `animals` FOR EACH ROW INSERT INTO log
set record_ID = new.id, operation = 'INSERT'
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `animals_UPDATE` AFTER UPDATE ON `animals` FOR EACH ROW INSERT INTO log set record_ID = new.id, operation = 'UPDATE'
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
(19, '2024-08-14 14:33:26', 10, 'UPDATE'),
(20, '2024-08-27 17:42:51', 23, 'INSERT'),
(21, '2024-08-28 06:36:48', 24, 'INSERT'),
(22, '2024-08-28 06:44:51', 25, 'INSERT'),
(23, '2024-08-28 07:12:02', 25, 'DELETE'),
(24, '2024-08-28 07:35:51', 26, 'INSERT'),
(25, '2024-08-28 07:43:31', 27, 'INSERT'),
(26, '2024-08-28 08:13:27', 28, 'INSERT'),
(27, '2024-08-28 08:30:51', 26, 'DELETE'),
(28, '2024-08-28 08:34:01', 27, 'DELETE'),
(29, '2024-08-28 15:45:41', 28, 'UPDATE'),
(30, '2024-08-28 15:52:05', 28, 'UPDATE'),
(31, '2024-08-28 15:53:25', 24, 'UPDATE'),
(32, '2024-08-28 15:58:58', 28, 'UPDATE'),
(33, '2024-08-28 16:01:04', 28, 'UPDATE'),
(34, '2024-08-28 16:20:41', 28, 'UPDATE'),
(35, '2024-08-28 16:22:10', 24, 'UPDATE'),
(36, '2024-08-28 16:35:34', 28, 'UPDATE'),
(37, '2024-08-29 19:02:42', 28, 'DELETE');

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
(4, '2024-08-15 22:22:40', 'Error: 42S22 Text error: Неизвестный столбец \'u_id_class\' в \'where clause\''),
(5, '2024-08-28 07:13:23', 'Error: 23000 Text error: Столбец \'id_class\' не может принимать величину NULL'),
(6, '2024-08-28 07:47:59', 'Error: 23000 Text error: Column \'name\' cannot be null');

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT для таблицы `class`
--
ALTER TABLE `class`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `log`
--
ALTER TABLE `log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT для таблицы `log_err`
--
ALTER TABLE `log_err`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
