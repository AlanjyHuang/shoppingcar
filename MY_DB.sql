-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022 年 11 月 19 日 07:43
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `shopping_car`
--

-- --------------------------------------------------------

--
-- 資料表結構 `shopping`
--

CREATE TABLE `shopping` (
  `ID` int(11) NOT NULL,
  `Name` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `Price` int(11) NOT NULL,
  `Number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `storage`
--

CREATE TABLE `storage` (
  `ID` int(11) NOT NULL,
  `Name` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `Price` int(11) NOT NULL,
  `Number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `storage`
--

INSERT INTO `storage` (`ID`, `Name`, `Price`, `Number`) VALUES
(1, 'dog', 200, 0),
(4, 'frog', 2, 1900),
(5, 'cow', 1999, 30),
(6, 'happy', 20000000, 1),
(2, 'cat', 200, 200),
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
