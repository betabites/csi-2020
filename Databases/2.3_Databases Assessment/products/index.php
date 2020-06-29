<?php
// The product directory is programmed to allow the user to access urls like '/products/mr-tee/happiness t-shirt' without the directory actually existing.

// Get the name of the product
$temp = explode("/", str_replace("/products/", "", $_SERVER["REQUEST_URI"]));
$designer_name = urldecode($temp[0]);
$product_name = urldecode($temp[1]);

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
$product = $product_query->fetch_assoc();
$variations = $frame->get_product_variations($product["product_id"]);
?>
<div id="product_data_display">
    <div>
        <?php
        $variations_output = [];
        foreach ($variations as $i => $variation) {
            array_push($variations_output, $variation);
            if ($i == 0) {
                echo "<img src='/../assets/images/".$variation["img_location"]."' style='width:100%;' id='primary_image' /><br><br><strong>Variations:</strong><br>";
                echo "<img src='/../assets/images/".$variation["img_location"]."' class='subitem' id='pro_variation_".$i."' onclick='change_variation(".$i.")' style='box-shadow: 0 2px 5px black; z-index: 2'>";
            } else {
                echo "<img src='/../assets/images/".$variation["img_location"]."' class='subitem' id='pro_variation_".$i."' onclick='change_variation(".$i.")'>";
            }

        }
        ?>
        <script>
            let variations = <?php echo json_encode($variations_output); ?>;
            let current_variation = 0

            function change_variation(variation_id) {
                document.getElementById('primary_image').src = "/../assets/images/" + variations[variation_id]["img_location"];
                document.getElementById('pro_variation_' + current_variation).style.boxShadow = "";
                document.getElementById('pro_variation_' + current_variation).style.zIndex = ""
                document.getElementById('pro_variation_' + variation_id).style.boxShadow = "0 2px 5px black";
                document.getElementById('pro_variation_' + variation_id).style.zIndex = "2"

                current_variation = variation_id

            }
        </script>
    </div>
    <div>
        <h1><?php echo $product_name; ?></h1>
        <h2>[Product Variation goes here]</h2>
        <?php echo $product["about"];?>
    </div>
</div>
<script>
    function select_data(id) {

    }
</script>
<?php
$frame->print_bottom();
