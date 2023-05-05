<?php

//Escreva um algoritmo que receba um número n e exiba os números de 0 até n separados por um espaço.

$n = $argv[1];
$a = 1;
$palavra = "";

while ($a <= $n) {
    $palavra .= "".strval($a)." ";

    $a++;
}

var_dump($palavra);