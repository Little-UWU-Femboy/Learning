<?php
date_default_timezone_set('America/Chicago');
$tempDir = __DIR__ . '/TemporaryData';
$chunkFile = $argv[1] ?? '';

if (!$chunkFile || !file_exists($chunkFile)) exit("Chunk file missing.");

$validDataFile = "$tempDir/valid_" . basename($chunkFile);
$errorDataFile = "$tempDir/error_" . basename($chunkFile);

$validHandle = fopen($validDataFile, "w");
$errorHandle = fopen($errorDataFile, "w");

$handle = fopen($chunkFile, "r");

while (($data = fgetcsv($handle)) !== false) {
    $totalCols = count($data);
    $lineNum = $data[$totalCols - 1]; 
    $actualCols = $totalCols - 1;
    
    $errors = [];
    $rawRowData = implode(",", array_slice($data, 0, $actualCols));
    $timeOccurred = date('Y-m-d H:i:s');

    if ($actualCols == 0 || ($actualCols == 1 && empty(trim($data[0])))) {
        $errors[] = "ERROR: All columns empty";
    } elseif ($actualCols < 3) {
        $errors[] = "ERROR: Less than three columns";
        if (empty($data[0])) $errors[] = "ERROR: Missing device type";
        if (empty($data[1])) $errors[] = "ERROR: Missing device brand";
    } elseif ($actualCols > 3) {
        $errors[] = "ERROR: More than three columns";
    } else {
        $type = trim($data[0]);
        $brand = trim($data[1]);
        $sn = trim($data[2]);

        $missingType = empty($type);
        $missingBrand = empty($brand);
        $missingSn = empty($sn);

        if ($missingType && $missingBrand) $errors[] = "ERROR: Missing device type, device brand";
        elseif ($missingType && $missingSn) $errors[] = "ERROR: Missing device type, serial number";
        elseif ($missingBrand && $missingSn) $errors[] = "ERROR: Missing device brand, serial number";
        else {
            if ($missingType) $errors[] = "ERROR: Missing device type";
            if ($missingBrand) $errors[] = "ERROR: Missing device brand";
            if ($missingSn) $errors[] = "ERROR: Missing serial number";
        }

        if (!$missingSn && (strlen($sn) !== 67 || substr($sn, 0, 3) !== 'SN-')) {
            $errors[] = "ERROR: Incorrect serial number size";
        }
    }

    if (!empty($errors)) {
        foreach ($errors as $errorMsg) {
            fputcsv($errorHandle, [$rawRowData, $errorMsg, $lineNum, $timeOccurred]);
        }
    } else {
        $cleanType = preg_replace('/[^A-Za-z]/', '', $data[0]);
        $cleanBrand = preg_replace('/[^A-Za-z]/', '', $data[1]);
        fputcsv($validHandle, [$cleanType, $cleanBrand, $data[2], $timeOccurred]);
    }
}

fclose($handle);
fclose($validHandle);
fclose($errorHandle);

// Fork process to store data
$pid = pcntl_fork();
if ($pid == -1) {
    die("Could not fork process.");
} else if ($pid) {
    pcntl_wait($status); 
} else {
    // Child process: execute Store.php
    shell_exec("php " . __DIR__ . "/Store.php " . escapeshellarg($validDataFile) . " " . escapeshellarg($errorDataFile));
    exit(0);
}
?>
