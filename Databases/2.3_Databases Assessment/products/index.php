<?php
// The product directory is programmed to allow the user to access urls like '/products/mr-tee/happiness t-shirt' without the directory actually existing.

// Get the name of the product
$temp = explode("/", str_replace("/products/", "", $_SERVER["REQUEST_URI"]));
$designer_name = $temp[0];
$product_name = $temp[1];

// Get the frame
require("../assets/php/frame.php");
$frame = new frame();

// Get product by designer & name
$product_query = $frame->get_product($product_name, $designer_name);

if ($product_query->num_rows == 0) {
    // Could not find product, so return the 404 error
    http_response_code(404);
    require ("../assets/error_pages/404.php");
    die();
}

$frame->print_top();

$frame->print_bottom();
