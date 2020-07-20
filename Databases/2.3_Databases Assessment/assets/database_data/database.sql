-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: fdb21.awardspace.net
-- Generation Time: Jul 18, 2020 at 03:14 AM
-- Server version: 5.7.20-log
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `3400555_koolkiwiana`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` tinyint(2) NOT NULL,
  `category_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`category_id`, `category_name`) VALUES
(1, 'Jewlry'),
(2, 'Clothing'),
(3, 'Sports Gear'),
(4, 'Décor'),
(5, 'Miscellanious');

-- --------------------------------------------------------

--
-- Table structure for table `designers`
--

CREATE TABLE `designers` (
  `designer_id` tinyint(2) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `land` int(10) DEFAULT NULL,
  `mobi` int(10) DEFAULT NULL,
  `addr_lin1` varchar(20) NOT NULL,
  `addr_line2` varchar(20) DEFAULT NULL,
  `region` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `designers`
--

INSERT INTO `designers` (`designer_id`, `name`, `email`, `land`, `mobi`, `addr_lin1`, `addr_line2`, `region`, `city`) VALUES
(1, 'JHD', 'juliahuyserdesign@gmail.com', 42316758, NULL, '1 Morrin Road', NULL, 'Saint Johns', 'Auckland'),
(2, 'Mr Vintage', '', 93006225, NULL, '34 Thorndon Quay', NULL, 'Pipitea', 'Wellington'),
(3, 'Moana Road', 'paul@moanaroad.co.nz', NULL, 21822505, '22 Halton Street', NULL, 'Strowan', 'Christchurch');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` tinyint(2) NOT NULL,
  `name` varchar(50) NOT NULL,
  `about` varchar(1000) NOT NULL,
  `designer_id` tinyint(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `about`, `designer_id`) VALUES
(1, 'Awesome Kid Banner', 'Wood banner, painted with Resene Galliano, and cut into a banner shape and engraved. Inspirational and gorgeous home decor item. Approx 13 x 18cm diameter. Twine for hanging.', 1),
(2, 'Be Bold Banner', 'Wood banner, painted, cut and engraved into a flag shape and engraved.Inspirational and quirky home decor item. Approx 17 x 14 cm. Twine for hanging.', 1),
(3, 'It gets better with Coffee Banner', 'Wood banner, painted with Resene Jaguar, and cut into a banner shape and engraved.Inspirational and gorgeous home decor item. Approx 13 x 19 cm diameter. Twine for hanging', 1),
(4, 'Day Mountain Pendant', 'Pendants are perfect for dress or casual. Add a splash of colour to a black outfit. Comes in 2 sizes. Hand-painted. Adjustable length chain to suit any neckline. 30 x 30 mm wooden oval face. Hand-painted. Hand-made. Reminiscent of New Zealand\'s Mountain Ranges during the day (also see the night mountain pendant) Aqua colour as per pic.Bronze backing. Nickel and Lead Free Chain. 80cm fully adjustable chain. Comes packaged in a Kraft gift box.', 1),
(5, 'NZ Natural Pendant', '30 x 40 mm oval face. Hand-painted. Hand-made. NZ design. Natural Rimu Wood. Bronze backing. Nickel and Lead free. 80cm fully adjustable chain.', 1),
(6, 'Rimu Stag Ring', '25mm diameter. Hand-painted wood face. RIMU. Stag Design. Fully adjustable ring (will go Ser or Lr). Nickel-free Stainless Steel Bronze Coated.', 1),
(7, 'Tiny Red Mountain Studs', 'Tiny, neat and charming.5mm diameter each earring approx. Rimu wood engraved with mountain design. Hand-painted in red. Surgical stainless steel backs. Gorgeous subtle little earrings for everyday wear.', 1),
(8, 'Hanging diamonds', 'Beautiful hanging hand-painted wood diamond shaped earrings. Perfect for casual or dress up for a night out. Approx 25mm long, 10mm wide. Wood engraved and hand-painted in yellow. Rimu wood. Nickel-free for sensitive ears.', 1),
(9, 'Bird Ring', '20 x 27 mm. Hand-painted wood face. Aqua colour. Bird Design. Fully adjustable ring (will go Ser or Lr). Nickel-free Stainless Steel Bronze Coated.', 1),
(10, 'Paralympics NZ Athletic Unisex Zip Hood', 'Paralympics New Zealand have launched their official Mr Vintage supporters range for the Rio 2016 Paralympic Games.', 2),
(11, 'NZ Olympic Team Goldie Men\'s Singlet', 'This is the official supporters range for the New Zealand Olympic Team to the 2016 Rio Olympic Games. Brought to you by Mr Vintage, the New Zealand Olympic Committee’s supporters range is the best way to take your support for New Zealand’s 2016 Olympic Team to the next level.', 2),
(12, 'Paralympics NZ Athletic Men\'s Singlet', 'Paralympics New Zealand have launched their official Mr Vintage supporters range for the Rio 2016 Paralympic Games.', 2),
(13, 'Bugger Mens T-Shirt', 'Our men\'s tees are 180 GSM, 100% super soft combed cotton, pre-shrunk to minimise shrinkage, lightweight and side-seamed for that tailored cut. Designed specifically for the NZ body shape, we know you\'ll love the fit and feel of the tees as much as what\'s printed on them.', 2),
(14, 'Burger Queen Womens T-Shirt', 'Our women’s tees are 100% cotton and pre-shrunk to minimise shrinkage, tailored to fit your NZ body. You also now have no reason to say you’ve got “nothing to wear”. This is what you’ll wear', 2),
(15, 'Tui Love Unisex Graphite Hood', 'Our UNISEX heavyweight hoods are composed of 350 GSM (Nice and warm); 80% Cotton and 20% Polyester. They’ve got a shoe-string cord, a kangaroo pouch for your hands (and lint), a cotton lined hood to look gangsta (if you’re that way inclined), and are made of anti-pill fabric (that’s the good stuff).', 2),
(16, 'EP: Sugar Skull Women\'s Scoop', 'Originally painted on a skateboard, this design symbolises the colour and finality of life. My love of Mexican artwork has taught me that skulls are not deathly images to be afraid off. Brightly coloured sugar skulls are used to celebrate the lives of loved ones during Día de Muertos (the Day of the Dead festival), they teach us to live and love life. Erika Pearce is an up and coming Auckland artist and designer with a flair for colour and life. Upon leaving her comfy salary-paying graphic design job in August 2012, she has ventured out on her own and has never looked back. Her artwork ranges from tattoo inspired designs to surf and skate art and highly detailed portraits. She is known for her versatility and is in high demand for custom artwork from collectors locally and all over the world. She loves creating things by hand, acrylic paint is her favourite M. Every piece she creates tells a story.', 2),
(17, 'Wooden Sunnies', 'These unisex, trendy and fun to wear sunglasses are made with wooden arms. Light but sturdy, they come with a microfibre sock case that doubles as a cleaning cloth. Produced by a New Zealand designer these affordable sunglasses are one of our best sellers for all ages!!', 3),
(18, 'Paddle', 'For the guys and gals who just want to paddle along and enjoy life. Beautifully finished and sporting our attractive Beech Palm Grip, this rugged paddle satisfies the needs of strong paddlers from fishermen to white water rafters. Made in New Zealand.', 3);

-- --------------------------------------------------------

--
-- Table structure for table `product_categories_link`
--

CREATE TABLE `product_categories_link` (
  `product_id` tinyint(2) NOT NULL,
  `category_id` tinyint(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_categories_link`
--

INSERT INTO `product_categories_link` (`product_id`, `category_id`) VALUES
(1, 4),
(2, 4),
(3, 4),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 2),
(10, 3),
(11, 2),
(11, 3),
(12, 2),
(12, 3),
(13, 2),
(14, 2),
(15, 2),
(16, 2),
(17, 5),
(18, 3);

-- --------------------------------------------------------

--
-- Table structure for table `product_variations`
--

CREATE TABLE `product_variations` (
  `variation_id` int(2) NOT NULL,
  `product_id` int(2) DEFAULT NULL,
  `price` int(2) DEFAULT NULL,
  `colour` varchar(6) DEFAULT NULL,
  `size` varchar(58) DEFAULT NULL,
  `img_location` varchar(38) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `inventory` int(2) DEFAULT NULL,
  `launch_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_variations`
--

INSERT INTO `product_variations` (`variation_id`, `product_id`, `price`, `colour`, `size`, `img_location`, `gender`, `inventory`, `launch_date`) VALUES
(0, NULL, NULL, NULL, 'Replaced sizes with global size abreviations (S, M, L, XL)', NULL, NULL, NULL, NULL),
(1, 1, 39, 'Yellow', NULL, 'yellowkidsbanner.jpg', NULL, 12, '0000-00-00'),
(2, 2, 39, 'Blue', NULL, 'boldbanner.jpg', NULL, 12, '0000-00-00'),
(3, 3, 39, 'Brown', NULL, 'coffeebanner.jpg', NULL, 12, '0000-00-00'),
(4, 4, 42, 'Blue', NULL, 'mountainpendant.jpg', NULL, 12, '0000-00-00'),
(5, 5, 42, 'Orange', NULL, 'nzpendant.jpg', NULL, 12, '0000-00-00'),
(6, 6, 28, 'Brown', NULL, 'stagring.jpg', NULL, 12, '0000-00-00'),
(7, 7, 29, 'Red', NULL, 'redstuds.png', NULL, 12, '0000-00-00'),
(8, 8, 34, 'Yellow', NULL, 'yellowdiamonds.jpg', NULL, 12, '0000-00-00'),
(9, 9, 28, 'Blue', NULL, 'birdring.jpg', NULL, 12, '0000-00-00'),
(10, 10, 69, 'Black', 'S', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '0000-00-00'),
(11, 10, 69, 'Black', 'M', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '0000-00-00'),
(12, 10, 69, 'Black', 'L', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '0000-00-00'),
(13, 10, 69, 'Black', 'XL', 'para-athletic_blk_hood_unisex-back.jpg', 'U', 12, '0000-00-00'),
(14, 11, 35, 'Black', 'S', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '0000-00-00'),
(15, 11, 35, 'Black', 'M', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '0000-00-00'),
(16, 11, 35, 'Black', 'L', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '0000-00-00'),
(17, 11, 35, 'Black', 'XL', 'nzot-goldie_blk_singlet_mens-back.jpg', 'M', 12, '0000-00-00'),
(18, 12, 35, 'Black', 'S', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '0000-00-00'),
(19, 12, 35, 'Black', 'M', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '0000-00-00'),
(20, 12, 35, 'Black', 'L', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '0000-00-00'),
(21, 12, 35, 'Black', 'XL', 'para-athletic_blk_singlet_mens.jpg', 'M', 12, '0000-00-00'),
(22, 13, 40, 'Black', 'S', 'bugger_blk_tee_mens.jpg', NULL, 12, '0000-00-00'),
(23, 13, 40, 'Black', 'M', 'bugger_blk_tee_mens.jpg', NULL, 12, '0000-00-00'),
(24, 13, 40, 'Black', 'L', 'bugger_blk_tee_mens.jpg', NULL, 12, '0000-00-00'),
(25, 13, 40, 'Black', 'XL', 'bugger_blk_tee_mens.jpg', NULL, 12, '0000-00-00'),
(26, 14, 40, NULL, 'S', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '0000-00-00'),
(27, 14, 40, NULL, 'M', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '0000-00-00'),
(28, 14, 40, NULL, 'L', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '0000-00-00'),
(29, 14, 40, NULL, 'XL', 'burgerqueen_water_tee_womens-main.jpg', 'W', 12, '0000-00-00'),
(30, 15, 89, NULL, 'S', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '0000-00-00'),
(31, 15, 89, NULL, 'M', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '0000-00-00'),
(32, 15, 89, NULL, 'L', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '0000-00-00'),
(33, 15, 89, NULL, 'XL', 'lh-tuilove_ash_hood_womens.jpg', 'U', 12, '0000-00-00'),
(34, 16, 40, NULL, 'S', 'epss-34.jpg', 'W', 12, '0000-00-00'),
(35, 16, 40, NULL, 'M', 'epss-35.jpg', 'W', 12, '0000-00-00'),
(36, 16, 40, NULL, 'L', 'epss-36.jpg', 'W', 12, '0000-00-00'),
(37, 16, 40, NULL, 'XL', 'epss-37.jpg', 'W', 12, '0000-00-00'),
(38, 17, 39, 'Blue', NULL, 'bluesunnies.jpg', 'U', 12, '0000-00-00'),
(39, 17, 39, 'Green', NULL, 'greensunnies.jpg', 'U', 12, '0000-00-00'),
(40, 17, 39, 'Red', NULL, 'redsunnies.jpg', 'U', 12, '0000-00-00'),
(41, 18, 59, 'Yellow', NULL, 'yellowpaddle.jpg', 'U', 12, '0000-00-00'),
(42, 18, 59, 'Blue', NULL, 'bluepaddle.jpg', 'U', 12, '0000-00-00'),
(43, 18, 59, 'Green', NULL, 'greenpaddle.jpg', 'U', 12, '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `designers`
--
ALTER TABLE `designers`
  ADD PRIMARY KEY (`designer_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_categories_link`
--
ALTER TABLE `product_categories_link`
  ADD KEY `product_id` (`product_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `product_variations`
--
ALTER TABLE `product_variations`
  ADD PRIMARY KEY (`variation_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `designers`
--
ALTER TABLE `designers`
  MODIFY `designer_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;