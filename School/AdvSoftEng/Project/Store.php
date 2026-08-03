<?php
$validDataFile = $argv[1] ?? '';
$errorDataFile = $argv[2] ?? '';

$conn = new mysqli("localhost", "User", "2k@NLxoktB!pT[!T", "ResourceManagement");

$typeMap = [];
$res = $conn->query("SELECT id, name FROM device_type");
while ($row = $res->fetch_assoc()) $typeMap[$row['name']] = $row['id'];

$brandMap = [];
$res = $conn->query("SELECT id, name FROM device_brand");
while ($row = $res->fetch_assoc()) $brandMap[$row['name']] = $row['id'];

$lockFile = fopen(__DIR__ . '/TemporaryData/db_write.lock', 'c');
flock($lockFile, LOCK_EX);

$conn->begin_transaction();

if (file_exists($validDataFile) && ($handle = fopen($validDataFile, "r")) !== false) {
    $stmt = $conn->prepare("INSERT IGNORE INTO processed_data (device_type_id, device_brand_id, serial_number, time_written) VALUES (?, ?, ?, ?)");
    while (($data = fgetcsv($handle)) !== false) {
        $typeId = $typeMap[$data[0]] ?? null;
        $brandId = $brandMap[$data[1]] ?? null;
        if ($typeId && $brandId) {
            $stmt->bind_param("iiss", $typeId, $brandId, $data[2], $data[3]);
            $stmt->execute();
        }
    }
    fclose($handle);
    $stmt->close();
}

if (file_exists($errorDataFile) && ($handle = fopen($errorDataFile, "r")) !== false) {
    $stmt = $conn->prepare("INSERT INTO error_data (actual_row_data, error_type, line_number, time_occurred) VALUES (?, ?, ?, ?)");
    while (($data = fgetcsv($handle)) !== false) {
        $stmt->bind_param("ssis", $data[0], $data[1], $data[2], $data[3]);
        $stmt->execute();
    }
    fclose($handle);
    $stmt->close();
}

$conn->commit();
$conn->close();

flock($lockFile, LOCK_UN);
fclose($lockFile);
?>
