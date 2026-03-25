<?php
$conn = new mysqli("localhost", "User", "2k@NLxoktB!pT[!T", "ResourceManagement");
if ($conn->connect_error) die("Connection failed: " . $conn->connect_error);

$tempDir = __DIR__ . '/TemporaryData';

$processEntities = function($filename, $table) use ($conn) {
    if (($handle = fopen($filename, "r")) !== false) {
        $stmt = $conn->prepare("INSERT IGNORE INTO $table (name) VALUES (?)");
        while (($data = fgetcsv($handle)) !== false) {
            if (isset($data[1]) && (int)$data[1] >= 10000) {
                $stmt->bind_param("s", $data[0]);
                $stmt->execute();
            }
        }
        fclose($handle);
        $stmt->close();
    }
};

$processEntities("$tempDir/TypeProcessed.csv", "device_type");
$processEntities("$tempDir/BrandProcessed.csv", "device_brand");
$conn->close();
?>
