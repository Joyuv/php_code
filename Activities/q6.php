<?php

$v1 = $argv [1];
$v2 = $argv [2];
$v3 = $argv [3];

if ($v1 >= $v2 && $v1 >= $v3){

    var_dump (intval($v1));

    die();

}

if ($v2 >= $v1 && $v2 >= $v3){

    var_dump (intval($v2));

    die();

}

if ($v3 >= $v1 && $v3 >= $v2){

    var_dump (intval($v3));

    die();

}