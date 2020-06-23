<?php
// This file is used to share functions between PHP pages.
class frame {
    private $mysqli;

    function __construct() {
        // This function runs whenever the class is first used in a PHP file

        // Setup SQL connection
        $this->mysqli = mysqli_connect("localhost", "root", "", "designers");
    }

    function print_top() {

    }

    function print_bottom() {

    }

    function get_all_products($mode = "products") {
        // Mode specified whether to get all products, or all product variations

        // $mode can = "products" or "variations"
        if ($mode == "products") {
            return $this->mysqli->query("SELECT * FROM `designers`.`products` JOIN `designers`.`product_variations` ON `designers`.`product_variations`.`product_id` = `designers`.`products`.`product_id` WHERE 1");
        } elseif ($mode == "variations") {
            return $this->mysqli->query("SELECT * FROM `designers`.`product_variations` JOIN `designers`.`products` ON `designers`.`products`.`product_id` = `designers`.`product_variations`.`product_id` WHERE 1");
        } else {
            return "Invalid parameter(s)";
        }
    }
}