<?php
// This file is used to share functions between PHP pages.
class frame {
    private $mysqli;

    function __construct() {
        // This function runs whenever the class is first used in a PHP file

        // Setup SQL connection
        $this->mysqli = mysqli_connect("fdb21.awardspace.net", "3400555_designers", "Jf3hGnlA50JTe%qo", "3400555_designers");
    }

    function print_top() {
        echo "<!DOCTYPE html>

        <html>
        <head>
            <title>Kool Kiwiana</title>
            <link rel=\"stylesheet\" href=\"/assets/css/styles.css\" />
            <meta name=\"viewport\" content=\"width=device-width, inital-scale=10\">
        </head>
        <body>
        <div id=\"header\">
            <div id=\"header_content\">
                <div id=\"menu\">
                    <ul id=\"nav\">
                        <li><a href='/'>Home</a></li>
                        <li><a href='/designers'>Designers</a></li>
                    </ul>
                </div>
                <h1>Kool Kiwiana</h1>
            </div>
        </div>
        <div id='content'>";
    }

    function print_bottom() {
        echo "</div></body></html>";
    }

    function get_all_products($get_variations = false) {
        $data_in = $this->mysqli->query("SELECT `products`.*, `designers`.`name` AS `des_name` FROM `products` JOIN `designers` ON `products`.`designer_id` = `designers`.`designer_id` WHERE 1");

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

    function get_product($name, $des_name) {
        $query = $this->mysqli->prepare("SELECT `products`.*, `designers`.`name` FROM `products` JOIN `designers` ON `designers`.`designer_id` = `products`.`designer_id` WHERE `products`.`name` = ? AND `designers`.`name` = ?");
        $query->bind_param("ss", $name, $des_name);
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
}