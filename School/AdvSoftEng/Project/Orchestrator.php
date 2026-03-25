<?php
$startTime = microtime(true);

$bootstrapConn = new mysqli("localhost", "User", "2k@NLxoktB!pT[!T", "ResourceManagement");
if ($bootstrapConn->connect_error) {
    die("Bootstrap connection failed: " . $bootstrapConn->connect_error);
}

$stmt = $bootstrapConn->prepare("SELECT username, password FROM accounts WHERE username = 'User'");
$stmt->execute();
$result = $stmt->get_result();
$accountData = $result->fetch_assoc();

$dbUser = $accountData['username'];
$dbPass = $accountData['password'];

$stmt->close();
$bootstrapConn->close();

echo "Starting Analysis...\n";
shell_exec("/usr/bin/php Analyze.php");

echo "Starting Creation...\n";
shell_exec("/usr/bin/php Creation.php");

echo "Starting Breaker...\n";
shell_exec("/usr/bin/php Breaker.php");

$partsDir = __DIR__ . '/parts';
$files = array_diff(scandir($partsDir), array('.', '..'));

echo "Starting Processing (Parallel Batching)...\n";
$activeProcesses = 0;
$maxProcesses = 4; // Optimized for 2 vCPU

foreach ($files as $file) {
    $chunkPath = $partsDir . '/' . $file;
    
    $pid = pcntl_fork();
    if ($pid == -1) {
        die("Could not fork in orchestrator.");
    } else if ($pid) {
        $activeProcesses++;
        if ($activeProcesses >= $maxProcesses) {
            pcntl_wait($status);
            $activeProcesses--;
        }
    } else {
        shell_exec("/usr/bin/php Process.php " . escapeshellarg($chunkPath));
        exit(0);
    }
}

while ($activeProcesses > 0) {
    pcntl_wait($status);
    $activeProcesses--;
}

$endTime = microtime(true);
$totalTime = $endTime - $startTime;

$conn = new mysqli("localhost", $dbUser, $dbPass, "ResourceManagement");
if ($conn->connect_error) {
    die("Report connection failed: " . $conn->connect_error);
}

$totalOriginalRecords = (int)trim(shell_exec("wc -l < tps757.csv"));

$res = $conn->query("SELECT COUNT(*) AS total FROM processed_data");
$totalProcessed = $res->fetch_assoc()['total'];

$res = $conn->query("SELECT error_type, COUNT(*) as c FROM error_data GROUP BY error_type");
$errorStats = "";
while ($row = $res->fetch_assoc()) {
    $errorStats .= "- " . $row['error_type'] . ": " . $row['c'] . "\n";
}

$res = $conn->query("SELECT error_type, line_number FROM error_data"); 
$errorLines = "";
while ($row = $res->fetch_assoc()) {
    $errorLines .= "Line " . $row['line_number'] . " -> " . $row['error_type'] . "\n";
}

$conn->close();

$effectiveSpeed = $totalTime > 0 ? round($totalProcessed / $totalTime, 2) : 0;

$reportContent = "
DATA IMPORT RESULTS
===================
Total records in original CSV: $totalOriginalRecords
Total time to import: " . round($totalTime, 2) . " seconds
Effective rows per second: $effectiveSpeed rows/sec
Total records stored without error: $totalProcessed

ERROR SUMMARY:
$errorStats

DETAILED ERRORS:
$errorLines
";

$tempDir = __DIR__ . '/TemporaryData';
file_put_contents("$tempDir/Results.txt", $reportContent);

echo "Process complete. Report generated in TemporaryData/Results.txt\n";
?>
