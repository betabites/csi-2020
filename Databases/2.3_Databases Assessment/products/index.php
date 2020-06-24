<?php
// The product directory is programmed to allow the user to access urls like '/products/mr-tee/happiness t-shirt' without the directory actually existing.

// Get the frame
require("../assets/php/frame.php");
$frame = new frame();
$frame->print_top();

// Get the name of the product
$temp = explode("/", str_replace("/products/", "", $_SERVER["REQUEST_URI"]));
$designer_name = $temp[0];
$product_name = $temp[1];
echo $designer_name.": ".$product_name;
$frame->print_bottom();
