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

    function get_all_products($get_variations = false) {
        $data_in = $this->mysqli->query("SELECT * FROM `designers`.`products` WHERE 1");

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
}