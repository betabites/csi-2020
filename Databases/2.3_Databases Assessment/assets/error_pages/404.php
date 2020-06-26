<?php
// Get the frame
if (! isset($frame)) {
    require (__DIR__."/../php/frame.php");
    $frame = new frame();
}

// Print the header
$frame->print_top();
?>
    <h1>HOOPS!</h1>
    <p>That page can't be found!
<?php
// Print the bottom
$frame->print_bottom();
?>