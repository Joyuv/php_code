<?php

$segundosv = $argv[1];

$hor = intdiv($segundosv, 3600);

$seg = $segundosv % 3600;

$min = intdiv($seg, 60);

$seg = $seg - ($min * 60);

var_dump ($hor. "h". $min. "m". $seg. "s");