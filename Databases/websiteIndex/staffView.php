<?php
//Get the frame
require('assets/private/php/frame.php');
$frame = new frame();

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $frame->save_teacher($_POST);
    $frame->print_message();
}
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
            width: 100%;
            min-height: 50px;
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
            width: 75px;
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
            cursor: pointer;
        }
    </style>
</head>
<body>
<div class="banner">
    <div class="content"><h1>Teacher Board</h1></div>
    <script>
        function imageUpdate() {
            let input = document.getElementById('image_input');
            let files = input.files

            if (FileReader && files.length) {
                let fr = new FileReader()
                fr.onload = function() {
                    document.getElementById('profileImage').src = fr.result;
                }
                fr.readAsDataURL(files[0])
            }
        }

        function cancel() {
            window.location = window.location.href.replace("staffView.php", "")
        }
    </script>
</div>
<div id="contentWrapper">
    <div id="content">
        <form method="POST" enctype="multipart/form-data">
            <?php
            $teacher = $frame->get_teacher($_GET['cypher']);
            ?>
            <div id="profileImageBox">
                <img id="profileImage" src="assets/public/uploads/images/<?php echo $teacher['image']; ?>"/>
                <label for="image_input" id="image_upload_label" type="button">Upload Image</label>
                <input type="file" onchange="imageUpdate()" accept="image/jpeg" style="display: none" id="image_input" name="profile_pic"/>
            </div>
            <div>
                <?php
                echo "<input type='text' value='".$_GET['cypher']."' style='display:none' name='cypher' /><input type='text' value='".$_GET['cypher']."' style='display:none' name='old_cypher' />";
                echo "<h1><input type='text' placeholder='Surname' value='".$teacher['teacher_surname']."' name='teacher_surname'/>, <input type='text' placeholder='Fits Name' value='".$teacher['teacher_christan']."' name='teacher_christan'/> (".$_GET['cypher'].")</h1>";
                echo "Born: <input type='number' class='small_input' min='1900' max='2100' name='yob' value='".$teacher['yob']."' name='yob'/> - Started: <input type='number' class='small_input' min='1900' max='2100' name='started' value='".$teacher['started']."' />";
                ?><br><br>
                <button style="background-color: blue;color:white;border-color: blue;">Save</button><button type="button" onclick="cancel()">Cancel</button>
            </div>
        </form>
    </div>
</div>
</body>
</html>