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
        <meta name="viewport" content="width=device-width, inital-scale=10">
    </head>
    <body>
        <div id="mainpage_header">
            <div id="mainpage_header_content">
                <div id="menu">
                    <ul id="nav">
                        <li>
                            <form action="search" method="get">
                                <!-- The 'action' attributes tells the browser to go to /search on the website, and do the query there. -->
                                <input type="text" name="criteria" placeholder="Search" style="margin:-5px;padding:5px;">
                            </form>
                        </li>
                        <li>Home</li>
                        <li><a href="/designers">Designers</a></li>
                        <li><a href="/categories">Categories</a></li>
                    </ul>
                </div>
                <h1>Kool Kiwiana</h1>
                <div id="mainpage_about">
                    <h1 style="font-size: 100pt; margin-bottom: 0;">Kool Kiwiana</h1>
                    <h2 style="margin-top: 0;">Novelty NZ products <span style="color:gray;">Nicky Roundtree</span></h2>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In imperdiet sed sapien non accumsan. Nullam finibus congue turpis et laoreet. Nulla ex sem, rhoncus in libero vitae, pulvinar ullamcorper risus. Donec tincidunt porttitor sapien id sollicitudin. Ut at convallis nulla. Integer vulputate lobortis velit, nec rutrum libero interdum vitae. Ut tincidunt mauris elit, id imperdiet lacus commodo eget. Quisque quis diam tortor.

                    <p style="font-size: 0.9rem;font-style: italic;"><a href="https://www.flickr.com/photos/32052617@N03/3231534430">"Image"</a><span> by <a href="https://www.flickr.com/photos/32052617@N03">JacksonPF</a></span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/2.0/?ref=ccsearch&atype=html" style="margin-right: 5px;">CC BY-NC-SA 2.0</a><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/?ref=ccsearch&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-by_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-sa_icon.svg" /></a></p>                </div>
                </div>
            </div>
        </div>
        <div id="group_select">
            Products are sorted by price (low - high)
        </div>
        <div class="content_list" id="product_content">
            <?php
            $data = $frame->get_all_products(true);
            foreach ($data as $i => $product) {
                ?>
                <div class="product" style="background-image: url('assets/images/<?php echo $product["variations"][0]["img_location"]."');";
                if ($product["variations"][0]['image_mode'] === "1") {
                    echo "background-size:contain;background-repeat:no-repeat;";
                }?>">
                    <div class="product_content">
                        <h1 class="product_name"><?php echo $product["name"]; ?></h1>
                        <a class="get_product" href="/products/<?php echo $product["product_id"]; ?>">$<?php echo $product["variations"][0]["price"]; ?> NZD</a>
                    </div>
                </div>
                <?php
            }
            ?>
        </div>
    </body>
</html>
