-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 30, 2019 at 12:52 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `deplib`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `accession_number` varchar(30) NOT NULL,
  `shelf_no` varchar(10) DEFAULT NULL,
  `title` varchar(120) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `author` varchar(200) DEFAULT NULL,
  `sno` int(11) NOT NULL,
  `publisher` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`accession_number`, `shelf_no`, `title`, `price`, `author`, `sno`, `publisher`) VALUES
('0001', NULL, 'A', 980, 'YUS', 1, 'OPen'),
('0002', NULL, 'Aa', 980, 'YUS', 3, 'OPen'),
('0003', NULL, 'B', 380, 'YU', 4, 'Oasc'),
('0004', NULL, 'asdc', 380, 'YU', 5, 'Oasc'),
('0005', NULL, 'asdsdc', 380, 'YU', 6, 'Oasc'),
('0006', NULL, 'asdsdc', 380, 'YU', 7, 'Oasc'),
('1009', NULL, 'Discrete mayh', 789, '456', 8, '789');

-- --------------------------------------------------------

--
-- Table structure for table `borrows`
--

CREATE TABLE `borrows` (
  `transaction_id` int(11) NOT NULL,
  `issue_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `issue_time` time DEFAULT NULL,
  `return_time` time DEFAULT NULL,
  `remarks` varchar(90) DEFAULT NULL,
  `issuers_member_id` int(11) DEFAULT NULL,
  `book_accesion_number` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `member_type` varchar(7) DEFAULT NULL,
  `member_id` int(11) NOT NULL,
  `mobile_number` varchar(12) DEFAULT NULL,
  `email_id` varchar(45) DEFAULT NULL,
  `full_name` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member_type`, `member_id`, `mobile_number`, `email_id`, `full_name`) VALUES
('Student', 1, '8275791691', 'skulkarni@mitaoe.ac.in', 'Shardul Kulkanri'),
('Student', 2, '987654321', 'ska@m.com', 'ABC'),
('Student', 7, '123456', 's@qw', 'Abc verma'),
('Student', 9, '123456', 's@qw', 'Ab verma'),
('', 11, '456789123', 'vkhan@mitaoe.ac.in', 'Vinay K'),
('', 12, '789456123', 'asinha@mitaoe.ac.in', 'Ankit Sinha'),
('', 14, '456789132', 'asdakjds', 'Sha Kul'),
('Student', 15, '9872427615', 'vschaudhari@mitaoe.ac.in', 'Vaibhav Chaudhari'),
('Student', 16, '123456789', 'sjkdskdfh@skjhfdkjsadf.com', 'Akashdeep Dhar'),
('Faculty', 17, '751', 'sk@as', 'Ak KA'),
('Faculty', 18, 'asd', 'sadas', 'as cm'),
('Faculty', 19, '2121e', 'askdansl', 'Alam asdas'),
('Student', 20, '45612', 'sdfasf', 'abc asdc'),
('Student', 21, '54', '32', 'saslkdn alsncas'),
('Student', 22, '789456123', 'asdsad@lkas', 'Lakshmikant Berde'),
('Student', 23, 'sss', 'sa', 'asdasd asd'),
('Student', 24, '89', '', 'Shardul s');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`accession_number`),
  ADD UNIQUE KEY `sno` (`sno`);

--
-- Indexes for table `borrows`
--
ALTER TABLE `borrows`
  ADD PRIMARY KEY (`transaction_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`member_id`),
  ADD UNIQUE KEY `full_name` (`full_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `borrows`
--
ALTER TABLE `borrows`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `member_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
