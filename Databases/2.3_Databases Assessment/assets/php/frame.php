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

    function get_all_products() {
        return $this->mysqli->query("SELECT * FROM `designers`.`products` WHERE 1");
    }
}