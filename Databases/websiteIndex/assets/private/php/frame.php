<?php

class frame {
    private $mysqli;
    private $class_location;
    private $message = [
        "type" => "", //Either ERROR or INFO
        "content" => "" //The content of the error
    ];

    function __construct() {
        //Connect SQL
        $this->mysqli = mysqli_connect("localhost", "root", "", "school_manager");
        $this->class_location = str_replace("frame.php", "", (new ReflectionClass('frame'))->getFileName());
    }

    //This function returns a list of all teachers
    function get_teachers() {
        $sql = "SELECT * FROM `teachers` WHERE ";
        $find_criteria = [];
        //Apply find criteria
        if (isset($_GET['find_cypher']) and $_GET['find_cypher'] != "") {
            array_push($find_criteria, "LOWER(`teacher_cypher`) LIKE CONCAT('%', LOWER('".addslashes($_GET['find_cypher'])."'), '%') ");
        }

        if (isset($_GET['find_fname']) and $_GET['find_fname'] != "") {
            array_push($find_criteria, "LOWER(`teacher_christan`) LIKE CONCAT('%', LOWER('".addslashes($_GET['find_fname'])."'), '%') ");
        }

        if (isset($_GET['find_lname']) and $_GET['find_lname'] != "") {
            array_push($find_criteria, "LOWER(`teacher_surname`) LIKE CONCAT('%', LOWER('".addslashes($_GET['find_lname'])."'), '%') ");
        }

        if (isset($_GET['find_room']) and $_GET['find_room'] != "" and $_GET['find_room'] !== "1") {
            array_push($find_criteria, "LOWER(`room`) = ".addslashes($_GET['find_room'])." ");
        }

        if ($find_criteria == []) {
            //No find criteria was applied
            $sql .= "1 ";
        } else {
            //Add find criteria to query
            $sql .= join(" AND ", $find_criteria);
        }

        if (isset($_GET['sort_field'])) {
            if ($_GET['sort_field'] == "First Name") {
                $sql .= "ORDER BY `teacher_christan` ";
            } elseif ($_GET['sort_field'] == "Last Name") {
                $sql .= "ORDER BY `teacher_surname` ";
            } elseif ($_GET['sort_field'] == "Year of birth") {
                $sql .= "ORDER BY `yob` ";
            } elseif ($_GET['sort_field'] == "Started Year") {
                $sql .= "ORDER BY `started` ";
            } else {
                $sql .= "ORDER BY `teacher_cypher` ";
            }
        } else {
            $sql .= "ORDER BY `teacher_cypher` ";
        }

        if (isset($_GET['sort_direction'])) {
            if ($_GET['sort_direction'] == "Ascending") {
                $sql .= "ASC";
            } elseif ($_GET['sort_direction'] == "Descending") {
                $sql .= "DESC";
            }
        } else {
            $sql .= "ASC";
        }
        echo "QUERY: ".$sql;

        return $this->mysqli->query($sql);

    }

    function get_teacher($cypher) {
        //Gets a teacher based on the inputted cypher
        $query = $this->mysqli->prepare('SELECT * FROM `teachers` WHERE `teacher_cypher` = ?');
        $query->bind_param("s", $cypher);
        $query->execute();
        $result = $query->get_result()->fetch_assoc();
        $query->close();
        return $result;
    }

    function save_teacher($data) {
        $image_location = "";
        if (isset($_FILES["profile_pic"]) and $_FILES["profile_pic"]["tmp_name"] !== "") {
            //Save image
            $image = $_FILES["profile_pic"];

            $target_dir = $this->class_location."../../public/uploads/images/".$data['cypher'].".".pathinfo($image["name"], PATHINFO_EXTENSION);
            //Check uploaded file is an image
            $image_size = getimagesize($image["tmp_name"]);
            if($image_size == false) {
                //File is not an image
                $this->message = [
                    "type" => "ERROR",
                    "content" => "That's not an image."
                ];
                return "Not Image";
            } else {
                //File is an image
                move_uploaded_file($image["tmp_name"], $target_dir);

                $image_location = $data['cypher'].".".pathinfo($image["name"], PATHINFO_EXTENSION);
            }
            $query = $this->mysqli->prepare("UPDATE `teachers` SET `teacher_cypher`= ?,`teacher_surname`= ?,`teacher_christan`= ?, `yob`= ?,`started`= ?,`image`= ?, `room` = ? WHERE `teacher_cypher` = ?");
            $query->bind_param("sssiisis", $data['cypher'], $data['teacher_surname'], $data['teacher_christan'], $data['yob'],$data['started'],$image_location,$data["room_id"],$data['old_cypher']);
            $result = $query->execute();
            $query->close();
        } else {
            $query = $this->mysqli->prepare("UPDATE `teachers` SET `teacher_cypher`= ?,`teacher_surname`= ?,`teacher_christan`= ?, `yob`= ?,`started`= ?, `room` = ? WHERE `teacher_cypher` = ?");
            $query->bind_param("sssiiis", $data['cypher'], $data['teacher_surname'], $data['teacher_christan'], $data['yob'],$data['started'],$data["room_id"],$data['old_cypher']);
            $result = $query->execute();
            $query->close();
        }


        $this->message = [
            "type" => "INFO",
            "content" => "Saved!"
        ];

        return $result;
    }

    function print_message() {
        if ($this->message["type"] == "INFO") echo "<div id='info'>".$this->message["content"]."</div>";
        else echo "<div id='error'>".$this->message["content"]."</div>";
    }

    function get_rooms() {
        //Returns a list of all rooms
        return $this->mysqli->query("SELECT * FROM `rooms` WHERE 1 ORDER BY `name` ASC");
    }
}