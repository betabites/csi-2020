<?php
//Get the frame
require('assets/private/php/frame.php');
$frame = new frame();
?>

<!DOCTYPE html>

<html lang="en">
    <head>
        <title>Teacher Board</title>
        <link rel="stylesheet" href="assets/public/css/styles.css">
    </head>
    <body>
        <div class="banner" id="title">
            <div class="content"><h1>Teacher Board</h1></div>
        </div>
        <div id="contentWrapper">
            <div id="content">
                Logged teachers:
                <form method="GET">
                    <strong>Sort By:</strong>
                    <select name="sort_field">
                        <?php if (isset($_GET['sort_field'])) {?>
                            <option <?php if ($_GET['sort_field'] == "Cypher") echo "selected"; ?>>Cypher</option>
                            <option <?php if ($_GET['sort_field'] == "First Name") echo "selected"; ?>>First Name</option>
                            <option <?php if ($_GET['sort_field'] == "Last Name") echo "selected"; ?>>Last Name</option>
                            <option <?php if ($_GET['sort_field'] == "Year of birth") echo "selected"; ?>>Year of birth</option>
                            <option <?php if ($_GET['sort_field'] == "Started Year") echo "selected"; ?>>Started Year</option>
                        <?php } else { ?>
                            <option selected>Cypher</option>
                            <option>First Name</option>
                            <option>Last Name</option>
                            <option>Year of birth</option>
                            <option>Started Year</option>
                        <?php } ?>
                    </select>
                    <select name="sort_direction">
                        <?php if (isset($_GET['sort_direction'])) {?>
                            <option <?php if ($_GET['sort_direction'] == "Ascending") echo "selected"; ?>>Ascending</option>
                            <option <?php if ($_GET['sort_direction'] == "Descending") echo "selected"; ?>>Descending</option>
                        <?php } else { ?>
                            <option selected>Ascending</option>
                            <option>Descending</option>
                        <?php } ?>
                    </select><br>
                    <strong>Find Criteria: </strong>
                    <input type="text" placeholder="Cypher" name="find_cypher" value="<?php if (isset ($_GET['find_cypher'])) echo $_GET["find_cypher"];?>">
                    <input type="text" placeholder="Last Name" name="find_lname" value="<?php if (isset ($_GET['find_cypher'])) echo $_GET["find_lname"];?>">
                    <input type="text" placeholder="First Name" name="find_fname" value="<?php if (isset ($_GET['find_cypher'])) echo $_GET["find_fname"];?>">
                    <select name="find_room">
                        <option value="" selected>Any room</option>
                        <?php foreach($frame->get_rooms() as $room) {
                            echo "<option value='".$room["room_id"]."'>".$room["name"]."</option>";
                        }?>
                    </select>
                    <button>Search & Sort</button>
                </form>
                <ul class="list1">
                    <?php
                    $teachers = $frame->get_teachers();
                    while ($teacher = mysqli_fetch_assoc($teachers)) {
                        echo "<li><a href='staffView.php?cypher=".$teacher['teacher_cypher']."'>".$teacher['teacher_cypher']." - ".$teacher['teacher_surname'].", ".$teacher['teacher_christan']."</a></li>";
                    }
                    ?>
                </ul>
            </div>
        </div>
    </body>
</html>