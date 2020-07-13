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
        } else {
            document.getElementById("content_list_" + last_designer).style.display = ""
            document.getElementById("content_list_" + designer_id).style.display = "grid"
            last_designer = designer_id
        }
    }
</script>
<?php
foreach($designers_query as $i => $product_var) {
    if ($i === 0) {
        echo "<div class='designer_drop'>".$product_var["des_name"]."<span style='float: right; cursor: pointer;' onclick='designer_toggle(".$product_var["designer_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["designer_id"]."'>";
        $last_designer_id = $product_var["designer_id"];
    } elseif ($product_var["designer_id"] !== $last_designer_id) {
        echo "</div><div class='designer_drop'>".$product_var["des_name"]."<span style='float: right; cursor: pointer;' onclick='designer_toggle(".$product_var["designer_id"].")'>Show available products</span></div><div class='content_list' style='padding: 20px 0; display: none;' id='content_list_".$product_var["designer_id"]."'>";
        $last_designer_id = $product_var["designer_id"];
    }?>
    <div class="product" style="background-image: url('../assets/images/<?php echo $product_var["img_location"]; ?>');">
        <div class="product_content">
            <h1 class="product_name"><?php echo $product_var["name"]; ?></h1>
            <h2>$<?php echo $product_var["price"];?></h2>
            <a class="get_product" href="/products/<?php echo $product_var["des_name"]."/".$product["name"]; ?>">View</a>
        </div>
    </div>
    <?php
}?>
    </div>
<?php

$frame->print_bottom();