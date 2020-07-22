<?php
// This page displays data for all designers
require("../assets/php/frame.php");

$frame = new frame();
$frame->print_top();

$designers_query = $frame->get_designers();
$last_designer_id = -1;
?>
<style>
    .content_list {
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    }
</style>
<script>
    let last_designer = -1;
    function designer_toggle(designer_id) {
        if (last_designer === -1) {
            document.getElementById("content_list_" + designer_id).style.display = "grid"
            last_designer = designer_id
        } else if(last_designer === designer_id) {
            document.getElementById("content_list_" + designer_id).style.display = "none"
            last_designer = -1
        } else {
            document.getElementById("content_list_" + last_designer).style.display = "none"
            document.getElementById("content_list_" + designer_id).style.display = "grid"
            last_designer = designer_id
        }
    }
</script>
Products are sorted by: Designer name (a-z), Price (low - high)
<?php
foreach($designers_query as $i => $product_var) {
    if ($i === 0) {
        echo "<div class='designer_drop'>".$product_var["des_name"]."<span style='float: right; cursor: pointer;' onclick='designer_toggle(".$product_var["designer_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["designer_id"]."'>";
        $last_designer_id = $product_var["designer_id"];
    } elseif ($product_var["designer_id"] !== $last_designer_id) {
        echo "</div><div class='designer_drop'>".$product_var["des_name"]."<span style='float: right; cursor: pointer;' onclick='designer_toggle(".$product_var["designer_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["designer_id"]."'>";
        $last_designer_id = $product_var["designer_id"];
    }?>
    <div class="product" style="background-image: url('../assets/images/<?php echo $product_var["img_location"]."');";
    if ($product_var['image_mode'] === "1") {
        echo "background-size:contain;background-repeat:no-repeat;";
    }?>">
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
            <a class="get_product" href="/products/<?php echo $product_var["product_id"]; ?>">$<?php echo $product_var["price"];?> NZD</a>
        </div>
    </div>
    <?php
}?>
    </div>
<?php

$frame->print_bottom();