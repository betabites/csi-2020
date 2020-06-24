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
            $data = $frame->get_all_products(true);
            foreach ($data as $product) {
                ?>
                <div class="product" style="background-image: url('assets/images/<?php echo $product["variations"][0]["img_location"]; ?>');">
                    <div class="product_content">
                        <h1 class="product_name"><?php echo $product["name"]; ?></h1>
                        <form>
                            <?php
                            if (count($product["variations"]) > 1) {
                                ?>
                                <select>
                                    <?php
                                    foreach ($product["variations"] as $i => $variation) {
                                        if ($i == 0) {
                                            echo "<option selected>".$variation["size"].$variation["colour"]."</option>";
                                        } else {
                                            echo "<option>".$variation["size"].$variation["colour"]."</option>";
                                        }
                                    }
                                    ?>
                                </select>
                                <?php
                            }
                            ?>
                        </form>
                        <button class="get_product">View</button>
                    </div>
                </div>
                <?php
            }
            ?>
        </div>
    </body>
</html>
