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
    <style>
        form {
            display: grid;
            grid-template-columns: 200px 1fr;
            grid-gap: 20px;
        }

        #profileImage {
            border: solid;
            height: 250px;
        }

        h1 > input {
            font-size: 24pt;
            width: 200px;
        }

        input {
            padding: 5px;
            border:none;
            border-bottom: solid 1px;
            border-radius: 3px;
            /*Prevent selected field outline on chrome*/
            outline: none;
        }

        input:active, input:focus {
            padding: 5px 5px 4px 5px;
            border:none;
            border-bottom: solid 2px blue;
        }

        .small_input {
            width: 50px;
        }

        button {
            margin: 10px 20px 10px 0;
            padding: 10px 20px;
            background-color: unset;
            font-weight: bold;
            border-radius: 3px;
        }

        #image_upload_label {
            background-color: blue;
            color:white;border-color: blue;
            margin: 10px 0 10px 0;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 3px;
            display: block;
        }
    </style>
</head>
<body>
<div class="banner">
    <div class="content"><h1>Teacher Board</h1></div>
    <script>
        function imageUpload() {
            let formData = new FormData();
                let content =
            }
    </script>
</div>
<div id="contentWrapper">
    <div id="content">
        <form method="POST">
        <div id="profileImageBox">
            <div id="profileImage"></div>
            <label for="image_input" id="image_upload_label" type="button">Upload Image</label>
            <input type="file" accept="image/*" style="display: none" id="image_input" />
        </div>
        <div>
            <?php
            $teacher = $frame->get_teacher($_GET['cypher']);
            echo "<h1><input type='text' placeholder='surname' value='".$teacher['teacher_surname']."' />, <input type='text' placeholder='first_name' value='".$teacher['teacher_christan']."' /> (".$_GET['cypher'].")</h1>";
            echo "Born: <input type='number' class='small_input' min='1900' max='2100' name='yob' value='".$teacher['yob']."' /> - Started: <input type='number' class='small_input' min='1900' max='2100' name='started' value='".$teacher['started']."' />";
            ?><br><br>
            <button style="background-color: blue;color:white;border-color: blue;">Save</button><button>Save & Exit</button><button>Cancel</button></div>
        </form>
    </div>
</div>
</body>
</html>