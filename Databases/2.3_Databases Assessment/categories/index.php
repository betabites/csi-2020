<?php
// This page displays data for all categories
require("../assets/php/frame.php");

$frame = new frame();
$frame->print_top();

$categories_query = $frame->get_categories(true);
$last_category_id = -1;
?>
<style>
    .content_list {
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    }
</style>
<script>
    let last_category = -1;
    function category_toggle(category_id) {
        if (last_category === -1) {
            document.getElementById("content_list_" + category_id).style.display = "grid"
            last_category = category_id
        } else {
            document.getElementById("content_list_" + last_category).style.display = "none"
            document.getElementById("content_list_" + category_id).style.display = "grid"
            last_category = category_id
        }
    }
</script>
Products are sorted by: Category name (a-z), Price (low - high)
<?php
foreach($categories_query as $i => $product_var) {
    if ($i === 0) {
        echo "<div class='designer_drop'>".$product_var["category_name"]."<span style='float: right; cursor: pointer;' onclick='category_toggle(".$product_var["category_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["category_id"]."'>";
        $last_category_id = $product_var["category_id"];
    } elseif ($product_var["category_id"] !== $last_category_id) {
        echo "</div><div class='designer_drop'>".$product_var["category_name"]."<span style='float: right; cursor: pointer;' onclick='category_toggle(".$product_var["category_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["category_id"]."'>";
        $last_category_id = $product_var["category_id"];
    }?>
    <div class="product" style="background-image: url('../assets/images/<?php echo $product_var["img_location"]; ?>');">
        <div class="product_content">
            <h1 class="product_name"><?php echo $product_var["name"]; ?></h1>
            <?php
                if ($product_var["colour"] !== NULL and $product_var["size"] !== NULL) {
                    echo "<h2><div class='circle circle_".strtolower($product_var["colour"])."'></div>".$product_var["colour"]." - ".$product_var["size"]."</h2>";
                } elseif ($product_var["colour"] !== NULL) {
                    echo "<h2><div class='circle circle_".strtolower($product_var["colour"])."'></div>".$product_var["colour"]."</h2>";
                } elseif ($product_var["size"] !== NULL) {
                    echo "<h2>".$product_var["size"]."</h2>";
                }
                ?>
            <a class="get_product" href="/products/<?php echo $product_var["category_name"]."/".$product_var["name"]; ?>">$<?php echo $product_var["price"];?> NZD</a>
        </div>
    </div>
    <?php
}?>
    </div>
<?php

$frame->print_bottom();