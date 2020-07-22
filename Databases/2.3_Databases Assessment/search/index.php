<?php
// This page displays data for all categories
require("../assets/php/frame.php");

$frame = new frame();
$frame->print_top();

// Perform the search
$data = $frame->mysqli->query("SELECT * FROM `products` WHERE LOWER(`products`.`name`) LIKE LOWER('%".addslashes($_GET['criteria'])."%') OR LOWER(`products`.`about`) LIKE LOWER('%".addslashes($_GET['criteria'])."%')");
if ($data->num_rows == 0) {
    // Print an error when there are no results
    echo "<h1>Hmmm...</h1>We couldn't find any products matching your search.";
} else {
    foreach ($data as $result) {
        echo "<a href='/products/".$result["product_id"]."'><strong>".$result["name"]."</strong></a><br><p>".$result["about"]."</p><hr>";
    }
}
$frame->print_bottom();