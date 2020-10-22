<?php
// Call the frame
require("assets/php/frame.php");
$frame = new frame();
?>
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, inital-scale=10">
        <meta name="author" content ="Jack Hawinkels" />
        <meta name="description" content ="Hello and welcome to Kool Kiwiana! The best website for all of your New Zealand novelties!" />
        <meta name="copyright" content ="&copy: 2020 Jack Hawinkels" />
        <title>Kool Kiwiana</title>
        <link rel="stylesheet" href="assets/css/styles.css" />
    </head>
    <body>
        <div id="mainpage_header">
            <div id="mainpage_header_content">
                <div id="menu_wrapper">
                    <div id="menu">
                        <h1>Kool Kiwiana</h1>
                        <ul id="nav">
                            <li id="search">
                                <form action="search" method="get">
                                    <!-- The 'action' attributes tells the browser to go to /search on the website, and do the query there. -->
                                    <input type="text" name="criteria" placeholder="Search" style="margin:-5px;padding:5px;">
                                </form>
                            </li>
                            <li>Home</li>
                            <li><a href="/designers">Designers</a></li>
                            <li><a href="/categories">Categories</a></li>
                            <li><a href="/genders">Genders</a></li>
                        </ul>
                    </div>
                </div>
                <div id="mainpage_about">
                    <h1 id="mainpage_h1">Kool Kiwiana</h1>
                    <h2 style="margin-top: 0;">Nicky Roundtree <span style="color:gray;">Novelty NZ Products</span></h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In imperdiet sed sapien non accumsan. Nullam finibus congue turpis et laoreet. Nulla ex sem, rhoncus in libero vitae, pulvinar ullamcorper risus. Donec tincidunt porttitor sapien id sollicitudin. Ut at convallis nulla. Integer vulputate lobortis velit, nec rutrum libero interdum vitae. Ut tincidunt mauris elit, id imperdiet lacus commodo eget. Quisque quis diam tortor.</p>

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
        <div id="copyright">&copy; Copyright 2020 - Jack Hawinkels - Tawa College - All Rights Reserved</div>
    </body>
</html>
