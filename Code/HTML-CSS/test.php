<?php

declare(strict_types=1);

/**
 * Cool PHP Demo
 * - 11 functions
 * - 1 nested function
 * - Simple class
 * - CLI/web compatible
 */

// --------------------------------------------------
// Functions
// --------------------------------------------------

function generateId(int $length = 8): string
{
    $chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    $id = '';

    for ($i = 0; $i < $length; $i++) {
        $id .= $chars[random_int(0, strlen($chars) - 1)];
    }

    return $id;
}

function slugify(string $text): string
{
    $text = strtolower(trim($text));
    $text = preg_replace('/[^a-z0-9]+/', '-', $text);
    return trim($text, '-');
}

function randomColor(): string
{
    return sprintf(
        '#%02X%02X%02X',
        random_int(0, 255),
        random_int(0, 255),
        random_int(0, 255)
    );
}

function formatBytes(int $bytes): string
{
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];

    for ($i = 0; $bytes >= 1024 && $i < count($units) - 1; $i++) {
        $bytes /= 1024;
    }

    return round($bytes, 2) . ' ' . $units[$i];
}

function fibonacci(int $n): int
{
    if ($n <= 1) {
        return $n;
    }

    return fibonacci($n - 1) + fibonacci($n - 2);
}

function isPalindrome(string $text): bool
{
    $clean = strtolower(preg_replace('/[^a-z0-9]/i', '', $text));
    return $clean === strrev($clean);
}

function average(array $numbers): float
{
    return array_sum($numbers) / max(count($numbers), 1);
}

function greeting(string $name): string
{
    $hour = (int) date('G');

    if ($hour < 12) {
        return "Good morning, {$name}";
    }

    if ($hour < 18) {
        return "Good afternoon, {$name}";
    }

    return "Good evening, {$name}";
}

function createBadge(string $label, string $color): string
{
    return sprintf(
        '<span style="background:%s;color:white;padding:4px 8px;border-radius:8px;">%s</span>',
        htmlspecialchars($color),
        htmlspecialchars($label)
    );
}

function countdown(int $from): array
{
    return range($from, 0);
}

/**
 * Function with a nested function.
 */
function calculateStats(array $numbers): array
{
    // Nested function
    function variance(array $values): float
    {
        $mean = array_sum($values) / count($values);

        $sum = 0;
        foreach ($values as $value) {
            $sum += ($value - $mean) ** 2;
        }

        return $sum / count($values);
    }

    return [
        'min'      => min($numbers),
        'max'      => max($numbers),
        'average'  => average($numbers),
        'variance' => variance($numbers),
    ];
}

// --------------------------------------------------
// Class
// --------------------------------------------------

class MiniLogger
{
    private array $entries = [];

    public function log(string $message): void
    {
        $this->entries[] = '[' . date('H:i:s') . "] {$message}";
    }

    public function getEntries(): array
    {
        return $this->entries;
    }
}

// --------------------------------------------------
// Demo
// --------------------------------------------------

$logger = new MiniLogger();

$id = generateId();
$slug = slugify('Cool PHP Demo Project');
$color = randomColor();

$logger->log("Generated ID: {$id}");
$logger->log("Slug: {$slug}");
$logger->log("Color: {$color}");

$stats = calculateStats([12, 44, 17, 29, 88, 31]);

?>
<!DOCTYPE html>
<html>
<head>
    <title>Cool PHP Demo</title>
    <style>
        body {
            background: #0f172a;
            color: #e2e8f0;
            font-family: Arial, sans-serif;
            padding: 30px;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            border-radius: 12px;
            max-width: 700px;
        }

        pre {
            background: #111827;
            padding: 10px;
            border-radius: 8px;
            overflow: auto;
        }
    </style>
</head>
<body>

<div class="card">
    <h1><?= greeting('Developer') ?></h1>

    <p><strong>ID:</strong> <?= htmlspecialchars($id) ?></p>
    <p><strong>Slug:</strong> <?= htmlspecialchars($slug) ?></p>
    <p><strong>Random Color:</strong> <?= htmlspecialchars($color) ?></p>

    <p><?= createBadge('ACTIVE', $color) ?></p>

    <h2>Stats</h2>
    <pre><?= htmlspecialchars(print_r($stats, true)) ?></pre>

    <h2>Fun Stuff</h2>
    <p>Fibonacci(10): <?= fibonacci(10) ?></p>
    <p>Palindrome Check ("Racecar"): <?= isPalindrome('Racecar') ? 'Yes' : 'No' ?></p>
    <p>Formatted Bytes: <?= formatBytes(123456789) ?></p>

    <h2>Countdown</h2>
    <pre><?= implode(', ', countdown(10)) ?></pre>

    <h2>Logs</h2>
    <pre><?= htmlspecialchars(print_r($logger->getEntries(), true)) ?></pre>
</div>

</body>
</html>