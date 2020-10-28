<?php
// This page displays data for all categories
require("../assets/php/frame.php");

$frame = new frame();
$frame->print_top();

// Perform the search
$data = $frame->mysqli->query("SELECT * FROM `products` JOIN `product_variations` ON `product_variations`.`product_id` = `products`.`product_id` WHERE LOWER(`products`.`name`) LIKE LOWER('%".addslashes($_GET['criteria'])."%') OR LOWER(`products`.`about`) LIKE LOWER('%".addslashes($_GET['criteria'])."%')");
?>
<style>
    #search_results {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-gap: 10px;
    }

    #search_results > div {
        box-shadow: 0 5px 10px rgba(0,0,0,0.5);
        display: grid;
        padding-top: 100px;
        background-size: cover;
        background-position: center;
    }

    #search_results > div:hover > div {
        opacity: 1;
    }

    #search_results > div > div {
        opacity: 0;
        background-color: rgba(0,0,0,0.9);
        color: white;
        transition: opacity 1s;
        padding: 0 20px 40px;
    }
</style>
<div id="search_results">
    <?php
    if ($data->num_rows == 0) {
        // Print an error when there are no results
        echo "<h1>Hmmm...</h1>We couldn't find any products matching your search.";
    } else {
        $last_product_id = -1;
        foreach ($data as $result) {
            ?>
            <div style="background-image: url('/assets/images/<?php echo addslashes($result["img_location"]);?>');">
                <div>
                    <h1><?php echo $result["name"];?></h1>
                    <p><?php echo $result["about"];?></p>
                    <h2><div class='circle circle_<?php echo strtolower($result["colour"]); ?>'></div><?php echo $result["colour"]; ?> - <?php echo $result["size"]; ?></h2>
                    <a href="/products/<?php echo $result["product_id"]."/".$result["variation_id"];?>" class="get_product">Get this product</a>
                </div>
            </div>
            <?php
        }
    }
    ?>
</div><?php
$frame->print_bottom();