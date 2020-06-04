<?php

class frame {
    private $mysqli;

    function __construct() {
        //Connect SQL
        $this->mysqli = mysqli_connect("localhost", "root", "", "school_manager");
    }

    //This function returns a list of all teachers
    function get_teachers() {
        $sql = "SELECT * FROM `teachers` WHERE 1 ";
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
        $image = '';
        var_dump($data);
        $query = $this->mysqli->prepare("UPDATE `teachers` SET `teacher_cypher`= ?,`teacher_surname`= ?,`teacher_christan`= ?, `yob`= ?,`started`= ?,`image`= ? WHERE `teacher_cypher` = ?");
        $query->bind_param("sssiiss", $data['cypher'], $data['teacher_surname'], $data['teacher_christan'], $data['yob'],$data['started'],$image,$data['old_cypher']);
        $result = $query->execute();
        $query->close();
        return $result;
    }
}