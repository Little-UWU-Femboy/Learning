<?php
$inputFile = 'tps757.csv';
$tempDir = __DIR__ . '/TemporaryData';

$types = [];
$brands = [];

$handle = fopen($inputFile, "r");
if ($handle) {
    while (($data = fgetcsv($handle)) !== false) {
        if (count($data) >= 2) {
            // Remove special symbols, leaving only A-z
            $type = preg_replace('/[^A-Za-z]/', '', $data[0]);
            $brand = preg_replace('/[^A-Za-z]/', '', $data[1]);
            
            if ($type !== '') $types[$type] = ($types[$type] ?? 0) + 1;
            if ($brand !== '') $brands[$brand] = ($brands[$brand] ?? 0) + 1;
        }
    }
    fclose($handle);
}

$typeFile = fopen("$tempDir/TypeProcessed.csv", "w");
foreach ($types as $t => $count) fputcsv($typeFile, [$t, $count]);
fclose($typeFile);

$brandFile = fopen("$tempDir/BrandProcessed.csv", "w");
foreach ($brands as $b => $count) fputcsv($brandFile, [$b, $count]);
fclose($brandFile);
?>
