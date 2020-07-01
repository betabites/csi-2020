<?php

class img_processer {
    private $image_location;

    function __construct($image_location) {
        $this->image_location = $image_location;
    }

    function web_op() {
        // Changes image resolution to 72dpi/72ppi
        imageresolution($this->image_location, 72, 72);
    }
}