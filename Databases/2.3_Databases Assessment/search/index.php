<?php
// This page displays data for all categories
require("../assets/php/frame.php");

$frame = new frame();
$frame->print_top();

// Perform the search
$sql = "SELECT * FROM `products` JOIN `product_variations` ON `product_variations`.`product_id` = `products`.`product_id` WHERE ";
$sql_criteria = [];
$keywords = explode(" ", $_GET['criteria']);
foreach ($keywords as $criteria_keyword) {
    array_push($sql_criteria, "LOWER(`products`.`name`) LIKE LOWER('%".addslashes($criteria_keyword)."%') OR LOWER(`products`.`about`) LIKE LOWER('%".addslashes($criteria_keyword)."%')");
}
$sql .= join(" OR ", $sql_criteria);
$data = $frame->mysqli->query($sql);
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
<?php
if ($data->num_rows == 0) {
    // Print an error when there are no results
    echo "<h1>Hmmm...</h1>We couldn't find any products matching your search. Try adjusting your keywords.";
} else {
    echo "<div id=\"search_results\">";
    $last_product_id = -1;

    // Calculate relevance and sort by it, then name
    $results = [];
    foreach ($data as $result) array_push($results, $result);

    foreach ($results as $i => $result) {
        $results[$i]["score"] = 0;
        foreach ($keywords as $keyword) {
            if (strpos(strtolower($result["name"]), strtolower(" ".$keyword." "))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["about"]), strtolower(" ".$keyword." "))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["name"]), strtolower(" ".$keyword))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["about"]), strtolower(" ".$keyword))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["name"]), strtolower($keyword." "))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["about"]), strtolower($keyword." "))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["name"]), strtolower($keyword))) $results[$i]["score"] += strlen($keyword);
            if (strpos(strtolower($result["about"]), strtolower($keyword))) $results[$i]["score"] += strlen($keyword);
        }
    }


    function sort_function($a, $b) {
        return $a["score"] < $b["score"];
    }

    usort($results, "sort_function");

    foreach ($results as $result) {
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
echo "</div>";
?>
<?php
$frame->print_bottom();