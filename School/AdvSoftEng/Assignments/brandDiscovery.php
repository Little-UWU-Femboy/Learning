<?php

$inputFile = "tps757.csv";
$outputFile = "uniqueBrands.txt";

$uniqueBrands = [];

function cleanText($text) {
    $cleaned = preg_replace('/[^a-zA-Z]/', '', $text);
    
    return strtolower($cleaned);
}

if (($handle = fopen($inputFile, "r")) !== false) {
    while (($row = fgetcsv($handle)) !== false) {

        if (isset($row[1])) {
            $rawValue = trim($row[1]);
            $cleanedValue = cleanText($rawValue);

            if (!empty($cleanedValue) && strlen($cleanedValue) >= 3) {
                $uniqueBrands[$cleanedValue] = true; // associative array = set
            }
        }
    }
    fclose($handle);
}

file_put_contents($outputFile, implode(PHP_EOL, array_keys($uniqueBrands)));

echo "Clean unique brands written to {$outputFile}\n";

?>
