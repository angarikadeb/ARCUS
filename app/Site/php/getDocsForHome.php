<?php

$pdo = new PDO('sqlite:../../data/db/ARCUS.sqlite');

$sql= "SELECT pk, citation FROM documents";

$statement=$pdo->prepare($sql);
$statement->execute();
$results=$statement->fetchAll(PDO::FETCH_ASSOC);
$json=json_encode($results);
echo $json;

?> 
