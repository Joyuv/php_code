<?php

// 5.Dada a idade de uma pessoa, escreva um programa que classifique-a em uma das seguintes categorias:
//     Menor = até 17 anos
//     Adulto = 18 a 59 anos
//     Idoso = 60 anos ou mais
    
$idade = $argv[1];

if ($idade < 18){

    var_dump ("Menor");

}

if ($idade >=18 && $idade <=59) {

    var_dump ("Adulto");

}

if ($idade >=60){

    var_dump ("Idoso");

}
