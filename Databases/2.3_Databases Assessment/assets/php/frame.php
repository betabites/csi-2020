<?php
// This file is used to share functions between PHP pages.
class frame {
    public $mysqli;

    function __construct() {
        // This function runs whenever the class is first used in a PHP file

        // Setup SQL connection
        $this->mysqli = mysqli_connect("fdb21.awardspace.net", "3400555_koolkiwiana", "Di3zsx@?5@O,(S*2", "3400555_koolkiwiana");
    }

    function print_top() {
        ?><!DOCTYPE html>

        <html>
        <head>
            <title>Kool Kiwiana</title>
            <link rel="stylesheet" href="/assets/css/styles.css" />
            <meta name="viewport" content="width=device-width, inital-scale=10">
            <style>
                /* This styling applies to all pages, except the main page */
                #header {
                    height: 0;
                }

                #header_content {
                    background-color: transparent;
                }

                body {
                    margin-top: 80px;
                }
            </style>
        </head>
        <body>
        <div id="header">
            <div id="header_content">
                <div id="menu_wrapper">
                    <div id="menu">
                        <h1>Kool Kiwiana</h1>
                        <ul id="nav">
                            <li id="search">
                                <form action="search" method="get">
                                    <!-- The 'action' attributes tells the browser to go to /search on the website, and do the query there. -->
                                    <input type="text" name="criteria" placeholder="Search" style="margin:-5px;padding:5px;">
                                </form>
                            </li>
                            <li><a href="/">Home</a></li>
                            <li><a href="/designers">Designers</a></li>
                            <li><a href="/categories">Categories</a></li>
                            <li><a href="/genders">Genders</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div id='content'>
        <?php
    }

    function print_bottom() {
        echo "</div></body></html>";
    }

    function get_all_products($get_variations = false) {
        $data_in = $this->mysqli->query("SELECT DISTINCT `products`.*, `designers`.`name` AS `des_name` FROM `products` 
JOIN `designers` ON `products`.`designer_id` = `designers`.`designer_id`
JOIN `product_variations` ON `product_variations`.`product_id` = `products`.`product_id`
WHERE 1 ORDER BY `product_variations`.`price` ASC");

        // Process data into an array
        $data = [];
        foreach ($data_in as $row) {
            array_push($data, $row);
        }

        if ($get_variations == true) {
            // Get product variations for each product
            foreach ($data as $i => $row){
                $data[$i]["variations"] = [];
                $variations_query = $this->mysqli->query("SELECT * FROM `product_variations` WHERE `product_id` = ".$row["product_id"]);
                foreach ($variations_query as $variation) {
                    array_push($data[$i]["variations"], $variation);
                }
            }
        }
        return $data;
    }

    function get_designers() {
        // Returns a list of all product variations sorted by designer name, then price
        return $this->mysqli->query("SELECT `product_variations`.*, `products`.*, `designers`.`name` AS 'des_name'  FROM `product_variations` JOIN `products` ON `products`.`product_id` = `product_variations`.`product_id` JOIN `designers` ON `designers`.`designer_id` = `products`.`designer_id` ORDER BY `designers`.`name` ASC, `product_variations`.`price` ASC");
    }

    function get_categories($get_sub_items = false) {
        if ($get_sub_items) {
            $sql = "SELECT * FROM `categories`
JOIN `product_categories_link` ON `product_categories_link`.`category_id` = `categories`.`category_id`
JOIN `product_variations` ON `product_variations`.`product_id` = `product_categories_link`.`product_id`
JOIN `products` ON `product_variations`.`product_id` = `products`.`product_id`
WHERE 1
ORDER BY `categories`.`category_name`, `product_variations`.`price` ASC";
        } else {
            $sql = "SELECT * FROM `categories` WHERE 1";
        }
        return $this->mysqli->query($sql);
    }

    function get_product($product_id) {
        $query = $this->mysqli->prepare("SELECT `products`.*, `designers`.`name` FROM `products` JOIN `designers` ON `designers`.`designer_id` = `products`.`designer_id` WHERE `products`.`product_id` = ?");
        $query->bind_param("i", $product_id);
        $query->execute();
        $output_array = [];
        $query->bind_result($output_array["product_id"], $output_array["name"], $output_array["about"], $output_array["designer_id"], $output_array["designer_name"]);

        // Get the results
        $query->fetch();

        $query->close();
        return $output_array;
    }

    function get_product_variations($product_id) {
        return $this->mysqli->query("SELECT * FROM `product_variations` WHERE `product_id` = ".$product_id);
    }

    function get_by_gender() {
        // Gets all product variations sorted by gender, then price
        return $this->mysqli->query("SELECT * FROM `product_variations` JOIN `products` on `product_variations`.`product_id` = `products`.`product_id` WHERE 1 ORDER BY `gender`, `price` ASC");
    }
}