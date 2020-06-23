<?php
// Call the frame
require("assets/php/frame.php");
$frame = new frame();
?>
<!DOCTYPE html>

<html>
    <head>
        <title>Kool Kiwiana</title>
        <link rel="stylesheet" href="assets/css/styles.css" />
    </head>
    <body>
        <div id="mainpage_header">
            <div id="mainpage_header_content">
                <div id="menu">
                    <ul id="nav">
                        <li>Home</li>
                    </ul>
                </div>
                <h1>Kool Kiwiana</h1>
            </div>
        </div>
        <div id="content_list">
            <?php
            // Print all products
            $data = $frame->get_all_products("variations");
            foreach ($data as $product) {
                ?>
                <div class="product" style="background-image: url('assets/images/<?php echo $product["img_location"]; ?>');">
                    <div class="product_content">

                    </div>
                </div>
                <?php
            }
            ?>
        </div>
    </body>
</html>
