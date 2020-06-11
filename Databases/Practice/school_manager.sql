-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2020 at 01:29 AM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `school_manager`
--

-- --------------------------------------------------------

--
-- Table structure for table `incomes`
--

CREATE TABLE IF NOT EXISTS `incomes` (
  `income_id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `income` int(6) NOT NULL,
  `tax` int(5) NOT NULL,
  `super` int(5) NOT NULL,
  PRIMARY KEY (`income_id`),
  UNIQUE KEY `income_id` (`income_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `incomes`
--

INSERT INTO `incomes` (`income_id`, `income`, `tax`, `super`) VALUES
(1, 75000, 22500, 7500),
(2, 90000, 27000, 9000),
(3, 110000, 33000, 11000),
(4, 55000, 16500, 5500),
(5, 80000, 24000, 8000),
(6, 95000, 28500, 9500),
(7, 65000, 19500, 6500);

-- --------------------------------------------------------

--
-- Table structure for table `positions`
--

CREATE TABLE IF NOT EXISTS `positions` (
  `positon_id` tinyint(1) NOT NULL AUTO_INCREMENT,
  `position_name` varchar(27) NOT NULL,
  PRIMARY KEY (`positon_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `positions`
--

INSERT INTO `positions` (`positon_id`, `position_name`) VALUES
(1, 'Assistant Principal Year 9'),
(2, 'Dean Year 9'),
(3, 'HOD_English'),
(4, 'Assistant Principal Year 10'),
(5, 'Dean Year 10'),
(6, 'Assistant Principal Year 13'),
(7, 'Dean Year 13'),
(8, 'Assistant Principal Year 11'),
(9, 'HOD_Digital Technologies');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE IF NOT EXISTS `rooms` (
  `room_id` tinyint(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(11) NOT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`room_id`, `name`) VALUES
(1, 'A1'),
(2, 'A2'),
(3, 'A6'),
(4, 'A9'),
(5, 'Admin Block'),
(6, 'B13'),
(7, 'B14'),
(8, 'C10'),
(9, 'C11'),
(10, 'C12'),
(11, 'C14'),
(12, 'C3'),
(13, 'C8'),
(14, 'C9'),
(15, 'D3'),
(16, 'D5'),
(17, 'D6'),
(18, 'D8'),
(19, 'D9'),
(20, 'F3'),
(21, 'G1'),
(22, 'G2'),
(23, 'G3'),
(24, 'G6'),
(25, 'Library'),
(26, 'T5'),
(27, 'T6');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE IF NOT EXISTS `subjects` (
  `subject_id` tinyint(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `name`) VALUES
(1, 'English'),
(2, 'Mathematics'),
(3, 'Digital Technology'),
(4, 'Info Tech'),
(5, 'Drama'),
(6, 'Arts'),
(7, 'Guidance'),
(8, 'Transition'),
(9, 'Languages'),
(10, 'Science'),
(11, 'Learner Support');

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE IF NOT EXISTS `teachers` (
  `teacher_cypher` char(3) NOT NULL,
  `teacher_surname` varchar(15) DEFAULT NULL,
  `theacher_christan` varchar(15) DEFAULT NULL,
  `teacher_form` char(5) NOT NULL,
  `teacher_form_mentors` char(5) DEFAULT NULL,
  `room` tinyint(2) DEFAULT NULL,
  `subject` tinyint(2) DEFAULT NULL,
  `position` tinyint(2) NOT NULL,
  `income` tinyint(2) DEFAULT NULL,
  `yob` year(4) DEFAULT NULL,
  `started` year(4) DEFAULT NULL,
  `image` varchar(15) NOT NULL,
  PRIMARY KEY (`teacher_cypher`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`teacher_cypher`, `teacher_surname`, `theacher_christan`, `teacher_form`, `teacher_form_mentors`, `room`, `subject`, `position`, `income`, `yob`, `started`, `image`) VALUES
('BRL', 'Brown', 'Lesley', '10BRL', '13BRL', 8, 1, 0, NULL, 1990, 2016, 'Art/Image01.jpg'),
('COR', 'Cook', 'Rose', '', NULL, 20, 1, 0, 1, 1984, 1990, 'Art/Image02.jpg'),
('CSR', 'Chester', 'Robyn', '13CSR', NULL, 5, 2, 1, 2, 1988, 2008, 'Art/Image03.jpg'),
('CTF', 'Christie', 'Fraser', '', NULL, 1, 3, 0, 1, 1976, 2003, 'Art/Image01.jpg'),
('CTS', 'Coats', 'Stephanie', '12CTS', NULL, 21, 1, 0, 1, 1971, 2015, 'Art/Image02.jpg'),
('DCA', 'Davies-Colley', 'Anne', '13DCA', NULL, 14, 1, 0, 1, 1982, 2015, 'Art/Image03.jpg'),
('DEJ', 'Doyle', 'Jason', '', NULL, 19, 2, 2, 5, 1974, 1994, 'Art/Image01.jpg'),
('DRJ', 'Dagger', 'Jo', '12DRJ', NULL, 6, 2, 0, 1, 1985, 2016, 'Art/Image02.jpg'),
('EDM', 'Edgecombe', 'Mark', '12EDM', NULL, 13, 1, 3, 2, 1981, 2009, 'Art/Image03.jpg'),
('ENJ', 'Engelbrecht', 'Jenny', '11ENJ', NULL, 18, 2, 0, 1, 1961, 1994, 'Art/Image01.jpg'),
('ESB', 'Espinosa', 'Ben', '', NULL, 2, 3, 0, 1, 1979, 1999, 'Art/Image02.jpg'),
('FDD', 'Foulds', 'David', '10FDD', '13FDD', 9, 4, 9, 2, 1971, 1987, 'Art/Image03.jpg'),
('GAR', 'Gale', 'Richard', '', NULL, 5, 1, 4, 6, 1977, 2013, 'Art/Image01.jpg'),
('GLN', 'Gartell', 'Nick', '11GLN', NULL, 10, 1, 0, 1, 1959, 2007, 'Art/Image02.jpg'),
('GYA', 'Grey', 'Aleisha', '13GYA', NULL, 14, 1, 0, 1, 1965, 2006, 'Art/Image03.jpg'),
('HAG', 'Hall', 'Gordon', '12HAG', NULL, 10, 4, 0, 1, 1965, 2003, 'Art/Image01.jpg'),
('HCO', 'Hutchison', 'Olwen', '', NULL, 16, 2, 5, 5, 1989, 1998, 'Art/Image02.jpg'),
('JNN', 'Johnston', 'Natalie', '12JNN', NULL, 15, 2, 0, 1, 1988, 1995, 'Art/Image03.jpg'),
('LIB', 'Smith', 'Elaine', '', NULL, 25, 1, 0, 1, 1987, 1986, 'Art/Image01.jpg'),
('LSM', 'Lucas', 'Murray', '', NULL, 5, NULL, 0, 3, 1976, 1995, 'Art/Image02.jpg'),
('MFT', 'McAuliffe', 'Terry', '11MFT', NULL, 7, 2, 0, 1, 1956, 1982, 'Art/Image03.jpg'),
('MZE', 'Maritz', 'Elize', '10MZE', '13MZE', 6, 1, 0, 1, 1983, 1980, 'Art/Image01.jpg'),
('NSJ', 'Nicholas', 'Jules', '', NULL, 5, 4, 6, 6, 1956, 1998, 'Art/Image02.jpg'),
('ONS', 'Overton', 'Sonia', '10ONS', '13ONS', 12, 1, 0, 1, 1976, 2012, 'Art/Image03.jpg'),
('PZK', 'Paradza', 'Kuda', '', NULL, 24, 2, 7, 7, 0000, 2010, 'Art/Image01.jpg'),
('RDJ', 'Randell', 'Judith', '9RDF', '13RDF', 17, 2, 0, NULL, 1966, 2009, 'Art/Image02.jpg'),
('RED', 'Rynne', 'Declan', '10RED', '13RED', 15, 2, 0, 1, 1963, 2006, 'Art/Image03.jpg'),
('ROM', 'Ross', 'Marie', '', NULL, 4, 6, 0, 1, 1970, 1986, 'Art/Image01.jpg'),
('RRA', 'Roberts', 'Angela', '12RRA', NULL, 23, 1, 0, 1, 1955, 1993, 'Art/Image02.jpg'),
('RYR', 'Ryder', 'Rebecca', '10RYR', '13RYR', 19, 2, 0, 1, 1959, 2001, 'Art/Image03.jpg'),
('SAE', 'Salem', 'Edmund', '', NULL, 26, 7, 0, 1, 1981, 1982, 'Art/Image01.jpg'),
('SHB', 'Sheridan', 'Belinda', '', NULL, 22, 1, 0, 1, 1976, 1993, 'Art/Image02.jpg'),
('SHC', 'Shill', 'Clare', '9SHC', '13SHC', 1, 3, 0, 4, 1969, 2014, 'Art/Image03.jpg'),
('SKA', 'Swank', 'Angela', '', NULL, 27, 7, 0, 1, 1970, 2011, 'Art/Image01.jpg'),
('SVC', 'Stevens', 'Charlotte', '9SVC', '13SVC', 11, 4, 0, 1, 1964, 2002, 'At/Image02.jpg'),
('SZC', 'Szabados', 'Christine', '', NULL, 3, 6, 0, NULL, 1968, 2012, 'Art/Image03.jpg'),
('TSM', 'Thomas', 'Mitch', '9TSM', '13TSM', 22, 1, 0, 1, 1971, 1986, 'Art/Image01.jpg'),
('WEA', 'West', 'Anne', '', NULL, 5, NULL, 8, 1, 1961, 1993, 'Art/Image02.jpg'),
('ZMG', 'McGuire', 'Sam', '', NULL, 9, 4, 0, 1, 1955, 1981, 'Art/Image03.jpg');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
