-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2020 at 11:24 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `designers`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `contacts_id` smallint(5) NOT NULL,
  `fname` varchar(10) NOT NULL,
  `lname` varchar(15) NOT NULL,
  `email_addr` varchar(40) NOT NULL,
  `phys_address_1` varchar(20) NOT NULL,
  `phys_address_2` varchar(20) NOT NULL,
  `town` varchar(10) NOT NULL,
  `city` varchar(15) NOT NULL,
  `country_cypher` char(2) NOT NULL,
  `pwd_hash` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`contacts_id`, `fname`, `lname`, `email_addr`, `phys_address_1`, `phys_address_2`, `town`, `city`, `country_cypher`, `pwd_hash`) VALUES
(1, 'Jack', 'Hawinkels', '7jhawinkels@tawacollege.school.nz', '', '16 Duncan Street', 'Tawa', 'Wellington', 'NZ', '####');

-- --------------------------------------------------------

--
-- Table structure for table `designers`
--

CREATE TABLE `designers` (
  `designer_id` tinyint(2) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `land` varchar(12) NOT NULL,
  `mobi` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `designers`
--

INSERT INTO `designers` (`designer_id`, `name`, `email`, `land`, `mobi`) VALUES
(1, 'JHD', 'juliahuyserdesign@gmail.com', '042316758', ''),
(2, 'Mr Vintage', 'help@mrvintage.co.nz', '093006225', ''),
(3, 'Moana Road', 'paul@moanaroad.co.nz', '', '021822505');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `transaction_id` tinyint(2) NOT NULL,
  `product_variation_id` tinyint(2) NOT NULL,
  `transaction_type` char(2) NOT NULL,
  `cost` float NOT NULL,
  `amount` smallint(2) NOT NULL,
  `contact_id` smallint(3) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`transaction_id`, `product_variation_id`, `transaction_type`, `cost`, `amount`, `contact_id`, `timestamp`) VALUES
(1, 1, 'in', 120, 12, 1, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` tinyint(2) NOT NULL,
  `name` varchar(50) NOT NULL,
  `about` varchar(1000) NOT NULL,
  `designer_id` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `about`, `designer_id`) VALUES
(1, 'Awesome Kid Yellow Banner', 'Wood banner, painted with Resene Galliano, and cut into a banner shape and engraved. Inspirational and gorgeous home decor item. Approx 13 x 18cm diameter. Twine for hanging.', 1),
(2, 'Be Bold Banner', 'Wood banner, painted, cut and engraved into a flag shape and engraved.Inspirational and quirky home decor item. Approx 17 x 14 cm. Twine for hanging.', 1),
(3, 'It gets better with Coffee Banner', 'Wood banner, painted with Resene Jaguar, and cut into a banner shape and engraved.Inspirational and gorgeous home decor item. Approx 13 x 19 cm diameter. Twine for hanging', 1),
(4, 'Day Mountain Pendant', 'Pendants are perfect for dress or casual. Add a splash of colour to a black outfit. Comes in 2 sizes. Hand-painted. Adjustable length chain to suit any neckline. 30 x 30 mm wooden oval face. Hand-painted. Hand-made. Reminiscent of New Zealand\'s Mountain Ranges during the day (also see the night mountain pendant) Aqua colour as per pic.Bronze backing. Nickel and Lead Free Chain. 80cm fully adjustable chain. Comes packaged in a Kraft gift box.', 1),
(5, 'NZ Natural Pendant', '30 x 40 mm oval face. Hand-painted. Hand-made. NZ design. Natural Rimu Wood. Bronze backing. Nickel and Lead free. 80cm fully adjustable chain.', 1),
(6, 'Rimu Stag Ring', '25mm diameter. Hand-painted wood face. RIMU. Stag Design. Fully adjustable ring (will go Ser or Lr). Nickel-free Stainless Steel Bronze Coated.', 1),
(7, 'Tiny Red Mountain Studs', 'Tiny, neat and charming.5mm diameter each earring approx. Rimu wood engraved with mountain design. Hand-painted in red. Surgical stainless steel backs. Gorgeous subtle little earrings for everyday wear.', 1),
(8, 'Yellow Hanging diamonds', 'Beautiful hanging hand-painted wood diamond shaped earrings. Perfect for casual or dress up for a night out. Approx 25mm long, 10mm wide. Wood engraved and hand-painted in yellow. Rimu wood. Nickel-free for sensitive ears.', 1),
(9, 'Aqua Bird Ring', '20 x 27 mm. Hand-painted wood face. Aqua colour. Bird Design. Fully adjustable ring (will go Ser or Lr). Nickel-free Stainless Steel Bronze Coated.', 1),
(10, 'Paralympics NZ Athletic Black Unisex Zip Hood', 'Paralympics New Zealand have launched their official Mr Vintage supporters range for the Rio 2016 Paralympic Games.', 2),
(11, 'NZ Olympic Team Goldie Men\'s Black Singlet', 'This is the official supporters range for the New Zealand Olympic Team to the 2016 Rio Olympic Games. Brought to you by Mr Vintage, the New Zealand Olympic Committee’s supporters range is the best way to take your support for New Zealand’s 2016 Olympic Team to the next level.', 2),
(12, 'Paralympics NZ Athletic Black Men\'s Singlet', 'Paralympics New Zealand have launched their official Mr Vintage supporters range for the Rio 2016 Paralympic Games.', 2),
(13, 'Bugger Mens Black T-Shirt', 'Our men\'s tees are 180 GSM, 100% super soft combed cotton, pre-shrunk to minimise shrinkage, lightweight and side-seamed for that tailored cut. Designed specifically for the NZ body shape, we know you\'ll love the fit and feel of the tees as much as what\'s printed on them.', 2),
(14, 'Burger Queen Womens Peach T-Shirt', 'Our women’s tees are 100% cotton and pre-shrunk to minimise shrinkage, tailored to fit your NZ body. You also now have no reason to say you’ve got “nothing to wear”. This is what you’ll wear', 2),
(15, 'Tui Love Unisex Graphite Hood', 'Our UNISEX heavyweight hoods are composed of 350 GSM (Nice and warm); 80% Cotton and 20% Polyester. They’ve got a shoe-string cord, a kangaroo pouch for your hands (and lint), a cotton lined hood to look gangsta (if you’re that way inclined), and are made of anti-pill fabric (that’s the good stuff).', 2),
(16, 'EP: Sugar Skull Women\'s Scoop', 'Originally painted on a skateboard, this design symbolises the colour and finality of life. My love of Mexican artwork has taught me that skulls are not deathly images to be afraid off. Brightly coloured sugar skulls are used to celebrate the lives of loved ones during Día de Muertos (the Day of the Dead festival), they teach us to live and love life. Erika Pearce is an up and coming Auckland artist and designer with a flair for colour and life. Upon leaving her comfy salary-paying graphic design job in August 2012, she has ventured out on her own and has never looked back. Her artwork ranges from tattoo inspired designs to surf and skate art and highly detailed portraits. She is known for her versatility and is in high demand for custom artwork from collectors locally and all over the world. She loves creating things by hand, acrylic paint is her favourite M. Every piece she creates tells a story.', 2),
(17, 'Wooden Sunnies', 'These unisex, trendy and fun to wear sunglasses are made with wooden arms. Light but sturdy, they come with a microfibre sock case that doubles as a cleaning cloth. Produced by a New Zealand designer these affordable sunglasses are one of our best sellers for all ages!!', 3),
(18, 'Paddle', 'For the guys and gals who just want to paddle along and enjoy life. Beautifully finished and sporting our attractive Beech Palm Grip, this rugged paddle satisfies the needs of strong paddlers from fishermen to white water rafters. Made in New Zealand.', 3);

-- --------------------------------------------------------

--
-- Table structure for table `product_variations`
--

CREATE TABLE `product_variations` (
  `variation_id` tinyint(2) NOT NULL,
  `product_id` tinyint(2) NOT NULL,
  `price` float NOT NULL,
  `colour` varchar(9) DEFAULT NULL,
  `size` varchar(3) DEFAULT NULL,
  `img_location` varchar(40) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `inventory` smallint(2) NOT NULL,
  `launch_date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_variations`
--

INSERT INTO `product_variations` (`variation_id`, `product_id`, `price`, `colour`, `size`, `img_location`, `gender`, `inventory`, `launch_date`) VALUES
(1, 1, 39, '', '', 'yellowkidsbanner.jpg', '', 12, '2020-06-19'),
(2, 2, 39, '', '', 'boldbanner.jpg', '', 12, '2020-06-19'),
(3, 3, 39, '', '', 'coffeebanner.jpg', '', 12, '2020-06-19'),
(4, 4, 42, '', '', 'mountainpendant.jpg', '', 12, '2020-06-19'),
(5, 5, 42, '', '', 'nzpendant.jpg', '', 12, '2020-06-19'),
(6, 6, 28, '', '', 'stagring.jpg', '', 12, '2020-06-19'),
(7, 7, 29, '', '', 'redstuds.jpg', '', 12, '2020-06-19'),
(8, 8, 34, '', '', 'yellowdiamonds.jpg', '', 12, '2020-06-19'),
(9, 9, 28, '', '', 'birdring.jpg', '', 12, '2020-06-19'),
(10, 10, 69, '', 'S', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '2020-06-19'),
(11, 10, 69, '', 'M', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '2020-06-19'),
(12, 10, 69, NULL, 'L', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '2020-06-19'),
(13, 10, 69, '', 'XL', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '2020-06-19'),
(14, 11, 35, 'Black', 'S', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '2020-06-19'),
(15, 11, 35, 'Black', 'M', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '2020-06-19'),
(16, 11, 35, 'Black', 'L', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '2020-06-19'),
(17, 11, 35, 'Black', 'XL', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '2020-06-19'),
(18, 12, 35, 'Black', 'S', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '2020-06-19'),
(19, 12, 35, 'Black', 'M', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '2020-06-19'),
(20, 12, 35, 'Black', 'L', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '2020-06-19'),
(21, 12, 35, 'Black', 'XL', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '2020-06-19'),
(22, 13, 40, 'Black', 'S', 'bugger_blk_tee_mens.jpg', '', 12, '2020-06-19'),
(23, 13, 40, 'Black', 'M', 'bugger_blk_tee_mens.jpg', '', 12, '2020-06-19'),
(24, 13, 40, 'Black', 'L', 'bugger_blk_tee_mens.jpg', '', 12, '2020-06-19'),
(25, 13, 40, 'Black', 'XL', 'bugger_blk_tee_mens.jpg', '', 12, '2020-06-19'),
(26, 14, 40, '', 'S', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '2020-06-19'),
(27, 14, 40, '', 'M', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '2020-06-19'),
(28, 14, 40, '', 'L', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '2020-06-19'),
(29, 14, 40, '', 'XL', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '2020-06-19'),
(30, 15, 89, '', 'S', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '2020-06-19'),
(31, 15, 89, '', 'M', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '2020-06-19'),
(32, 15, 89, '', 'L', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '2020-06-19'),
(33, 15, 89, '', 'XL', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '2020-06-19'),
(34, 16, 40, '', 'S', 'epss-34.jpg', 'W', 12, '2020-06-19'),
(35, 16, 40, '', 'M', 'epss-35.jpg', 'W', 12, '2020-06-19'),
(36, 16, 40, '', 'L', 'epss-36.jpg', 'W', 12, '2020-06-19'),
(37, 16, 40, '', 'XL', 'epss-37.jpg', 'W', 12, '2020-06-19'),
(38, 17, 39, 'Blue', '', 'bluesunnies.jpg', 'U', 12, '2020-06-19'),
(39, 17, 39, 'Green', '', 'greensunnies.jpg', 'U', 12, '2020-06-19'),
(40, 17, 39, 'Red', '', 'redsunnies.jpg', 'U', 12, '2020-06-19'),
(41, 18, 59, 'Yellow', '', 'yellowpaddle.jpg', 'U', 12, '2020-06-19'),
(42, 18, 59, 'Blue', '', 'bluepaddle.jpg', 'U', 12, '2020-06-19'),
(43, 18, 59, 'Green', '', 'greenpaddle.jpg', 'U', 12, '2020-06-19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`contacts_id`);

--
-- Indexes for table `designers`
--
ALTER TABLE `designers`
  ADD PRIMARY KEY (`designer_id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `product_variation_id` (`product_variation_id`),
  ADD KEY `contact_id` (`contact_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `designer_id` (`designer_id`);

--
-- Indexes for table `product_variations`
--
ALTER TABLE `product_variations`
  ADD PRIMARY KEY (`variation_id`),
  ADD KEY `product_id` (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `contacts_id` smallint(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `designers`
--
ALTER TABLE `designers`
  MODIFY `designer_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `transaction_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `product_variations`
--
ALTER TABLE `product_variations`
  MODIFY `variation_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`product_variation_id`) REFERENCES `product_variations` (`variation_id`),
  ADD CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`contact_id`) REFERENCES `contacts` (`contacts_id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`designer_id`) REFERENCES `designers` (`designer_id`);

--
-- Constraints for table `product_variations`
--
ALTER TABLE `product_variations`
  ADD CONSTRAINT `product_variations_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
