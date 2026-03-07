# Java

## Arrays

### Overview

In PHP, an **array** is an ordered map that associates **keys** with **values**. Arrays are extremely flexible: they can behave as lists (indexed arrays), dictionaries (associative arrays), stacks, queues, and even multidimensional structures.

### Array Initialization

Arrays can be created in different ways like *indexed*, *associative*, or *mixed arrays*.

Syntax:

- `array(value1, value2, ...)` — older syntax
- `[value1, value2, ...]` — short syntax (PHP 5.4+)
- Associative arrays: `[key => value, ...]`

```php
<?php
// Indexed arrays
$os_list = array("Linux", "Unix", "Windows"); // old syntax
$os_list2 = ["Linux", "Unix", "Windows"];    // short syntax

// Associative array
$user_data = [
    "id" => 101,
    "role" => "admin",
    "active" => true
];

// Mixed array (numeric and string keys)
$mixed = [
    0 => "zero",
    "one" => 1,
    2 => "two"
];

// Empty array
$empty = [];
?>
```

### Indexed Arrays

An *indexed array* uses numeric keys, typically starting from 0. You can access elements by their index.

```php
$array[index]
<?php
$fruits = ["Apple", "Banana", "Cherry"];
echo $fruits[0]; // Outputs "Apple"
?>
```

### Associative Arrays

An **associative array** uses keys that are strings or integers. These arrays map keys to values like a dictionary.

Rules:

- Keys must be unique. Duplicate keys will overwrite previous values.
- Values can be any type.

```php
$array[key] = value
<?php
$person = [
    "name" => "Alice",
    "age" => 25
];

echo $person["name"]; // Outputs "Alice"
?>
```

### Multidimensional Arrays

An array containing other arrays. Often used to represent tables, matrices, or JSON-like structures.

```php
$array[row_index][column_index] // for numeric arrays
$array[row_index]["key"]       // for associative arrays
<?php
$matrix = [
    [1, 2, 3],
    [4, 5, 6]
];
echo $matrix[1][0]; // Outputs 4

$users = [
    ["id" => 1, "name" => "Alice"],
    ["id" => 2, "name" => "Bob"]
];
echo $users[1]["name"]; // Outputs "Bob"
?>
```

### Iterating Over Arrays

 `foreach` is a PHP construct used to loop over arrays easily. It iterates through each element without manually managing indexes.

```php
foreach ($array as $value) { ... } // For indexed arrays
foreach ($array as $key => $value) { ... } // For associative arrays
```

Rules:

- `$value` is the element at the current iteration.
- `$key => $value` gives both key and value for associative arrays.

```php
<?php
$colors = ["Red", "Green", "Blue"];
foreach ($colors as $color) {
    echo $color . "\n"; // Prints each color
}

$person = ["name" => "Alice", "age" => 25];
foreach ($person as $key => $value) {
    echo "$key => $value\n"; // Prints key-value pairs
}
?>
```

`for` is the standard numeric loop for arrays where it is known the number of elements.

```php
for ($i = 0; $i < count($array); $i++) { ... }
<?php
$colors = ["Red", "Green", "Blue"];
for ($i = 0; $i < count($colors); $i++) {
    echo $colors[$i] . "\n";
}
?>
```

### Common Array Functions

`count()` the number of elements in an array or countable object. Can count recursively.

Parameters:

- `value` (array|Countable) — Array or object to count
- `mode` (int, optional) — `COUNT_RECURSIVE` to count nested arrays

Return: int — Number of elements

```php
<?php
$numbers = [1, 2, 3];
echo count($numbers); // 3

$nested = [[1, 2], [3, 4]];
echo count($nested, COUNT_RECURSIVE); // 6
?>
```

`array_push()` adds one or more elements to the end of an array.

Parameters:

- `array` (array, by reference) — Input array
- `values` (mixed) — Values to add

Return: int — New array length

```php
<?php
$stack = ["a", "b"];
array_push($stack, "c", "d");
print_r($stack); // ["a", "b", "c", "d"]
?>
```

`array_pop()` removes and returns the last element of an array.

Parameters:

- `array` (array, by reference) — Array to modify

Return: mixed — Removed element

```php
<?php
$stack = ["a", "b", "c"];
$last = array_pop($stack);
echo $last; // "c"
?>
```

`array_merge()` merges one or more arrays. Later arrays append to the first.

Parameters:

- `arrays` (array...) — Arrays to merge

Return: array — Merged array

```php
<?php
$arr1 = [1, 2];
$arr2 = [3, 4];
$result = array_merge($arr1, $arr2);
print_r($result); // [1, 2, 3, 4]
?>
```

`array_keys()` returns the keys of an array, optionally filtered by a value.

Parameters:

- `array` — Array to search
- `filter_value` (optional) — Only return keys for this value

Return: array — Keys

```php
<?php
$user = ["id" => 101, "role" => "admin"];
$keys = array_keys($user);
print_r($keys); // ["id", "role"]
?>
```

`in_array()` checks if a value exists in an array.

Parameters:

- `needle` — Value to search for
- `haystack` — Array to search
- `strict` (optional) — Also checks type

Return: bool — True if value exists

```php
<?php
$fruits = ["Apple", "Banana"];
if (in_array("Apple", $fruits)) {
    echo "Found Apple!";
}
?>
```

`array_column()` extracts values from a single column in a multidimensional array.

Parameters:

- `array` — Input array
- `column_key` — Column to extract
- `index_key` (optional) — Keys to use for output array

Return: array — Column values

```php
<?php
$users = [
    ["id" => 1, "name" => "Alice"],
    ["id" => 2, "name" => "Bob"]
];
$names = array_column($users, "name");
print_r($names); // ["Alice", "Bob"]
?>
```

### Sorting Functions

Definition: Sort arrays by value or key.

- `sort($array)` — Sort ascending values
- `rsort($array)` — Sort descending values
- `asort($array)` — Sort values ascending, preserve keys
- `ksort($array)` — Sort keys ascending

```php
<?php
$numbers = [3, 1, 2];
sort($numbers);
print_r($numbers); // [1, 2, 3]
?>
```



