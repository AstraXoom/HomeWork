-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 16 2022 г., 11:44
-- Версия сервера: 10.3.22-MariaDB
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `users_passwords`
--

-- --------------------------------------------------------

--
-- Структура таблицы `users_pass`
--

CREATE TABLE `users_pass` (
  `UserID` int(11) NOT NULL,
  `UserName` varchar(15) NOT NULL,
  `UserPass` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `users_pass`
--

INSERT INTO `users_pass` (`UserID`, `UserName`, `UserPass`) VALUES
(1, 'Slava', '1234%HGHGHhhh1'),
(2, 'Kola', '89FJu%%2wwwq1'),
(4, 'Alena', '889GHGHhy%12u');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `users_pass`
--
ALTER TABLE `users_pass`
  ADD PRIMARY KEY (`UserID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `users_pass`
--
ALTER TABLE `users_pass`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
