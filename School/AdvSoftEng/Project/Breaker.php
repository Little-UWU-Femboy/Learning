<?php
$inputFile = 'tps757.csv';
$partsDir = __DIR__ . '/parts';

if (!is_dir($partsDir)) {
    mkdir($partsDir, 0777, true);
}

$handle = fopen($inputFile, "r");
if ($handle) {
    $fileNum = 1;
    $lineNum = 1;
    $chunkSize = 100000; 
    $outHandle = fopen("$partsDir/chunk_$fileNum.csv", "w");

    while (($data = fgetcsv($handle)) !== false) {
        $data[] = $lineNum; // Append original line number
        fputcsv($outHandle, $data);
        
        if ($lineNum % $chunkSize === 0) {
            fclose($outHandle);
            $fileNum++;
            $outHandle = fopen("$partsDir/chunk_$fileNum.csv", "w");
        }
        $lineNum++;
    }
    fclose($handle);
    if (is_resource($outHandle)) fclose($outHandle);
}
?>
