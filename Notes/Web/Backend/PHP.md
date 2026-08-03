# PHP Core and Basics

## Introduction

### Language Overview

PHP stands for PHP: Hypertext Preprocessor. It is a widely-used *open source general-purpose scripting language* that is especially suited for web development and can be embedded directly into HTML. Historically, PHP originally stood for *Personal Home Page*, but it later evolved into the recursive acronym used today.

Unlike languages such as Python, which use indentation to define block levels, PHP utilizes curly braces **{}** to define *code blocks* and requires a semicolon **;** to terminate *statements*.

PHP also follows specific *case sensitivity rules*. **Variables** are case-sensitive, while **keywords** and **function names** are not. This means that `$value` and `$Value` are treated as different variables, while `echo`, `ECHO`, and `Echo` are interpreted as the same language construct.

### Standard Tags and File Structure

The *PHP engine* only processes code contained within specific *delimiter tags*. Anything outside of these tags is ignored by the engine and sent directly to the output.

- **Standard Tags**: `<?php ... ?>`. This is the primary and recommended method for declaring PHP code.
- **Short Echo Tags**: `<?= ... ?>`. This serves as a shorthand for `<?php echo ...; ?>` and is frequently used within HTML templates to display variables.
- **Short Open Tags**: `<? ... ?>`. These depend on the `short_open_tag` configuration directive and are generally discouraged in modern development because they may not be enabled on all servers.

PHP scripts must be saved with a `.php` extension for the *web server* to identify and execute the code.

If a file contains exclusively PHP code, the closing tag `?>` is typically omitted. This prevents the accidental injection of *trailing whitespace* or *newline characters* into the *output buffer*, which can cause issues when sending *HTTP headers*.

### Comments

Comments are used to document code and are ignored by the *PHP interpreter* during execution. They are commonly used to explain logic, disable sections of code during debugging, or annotate implementation details.

PHP supports three comment styles:

```php
// Single-line comment

# Another single-line comment style

/*
   Multi-line comment
   Often used for longer explanations
*/
```

### Statement Structure

PHP programs consist of *statements*, which are individual instructions executed by the interpreter. Every statement must end with a semicolon **;**.

Control structures such as conditional statements and loops define *blocks of execution* using curly braces **{}**.

```php
if ($value > 10) {
    echo "Large";
}
```

### Execution Environments

PHP scripts can run in multiple *execution environments*, depending on how the script is invoked.

#### Command Line Interface (CLI)

PHP can run as a standalone script inside a terminal environment. This mode is commonly used for *background processes*, *system administration tasks*, *automation scripts*, and *testing workflows*.

Scripts are executed with the command:

```
php scriptname.php
```

#### Web Server Execution

In a web environment, PHP operates behind a *web server* such as Apache or Nginx. The server receives an HTTP request and forwards it to the PHP interpreter using either a *server module* or *PHP-FPM (FastCGI Process Manager)*.

The typical execution flow follows a simple request lifecycle:

```
Client Request → PHP Script Execution → Generated Response
```

During execution, PHP generates output that is stored in an *output buffer*. Once the script completes, the contents of this buffer are sent to the client browser as the HTTP response.

Improper output, such as accidental whitespace before headers are sent, can cause issues when functions attempt to modify HTTP headers.

### Including External Files

PHP provides several *language constructs* used to load and execute external files. These are essential for organizing code into reusable modules and separating configuration or logic across multiple files.

`include`, `require`, `include_once`, and `require_once` are commonly used for this purpose.

- `include` loads and executes the specified file. If the file cannot be found, PHP emits a **warning**, but the script continues execution.
- `require` behaves similarly but produces a **fatal error** if the file cannot be located, stopping script execution.
- `include_once` ensures the file is included only once during execution, preventing duplicate definitions.
- `require_once` performs the same check as `include_once`, but with the fatal error behavior of `require`.

```php
include "config.php";
require "database.php";
require_once "router.php";
```

These constructs are commonly used for *configuration files*, *database connections*, and *application modules*.

### Basic Output Functions and Constructs

PHP provides several *output mechanisms* used to send data to the output buffer.

`phpinfo()` outputs a large amount of diagnostic information about the current PHP environment, including *version information*, *loaded extensions*, *configuration directives*, and *server environment details*.

- Parameters: `flags` (int) — Optional. Controls which sections are displayed using constants such as **INFO_GENERAL**, **INFO_CREDITS**, or **INFO_MODULES**.
- Returns: (bool) — Returns **true** on success.

`phpversion()` returns the version of the PHP interpreter currently in use.

- Parameters: `extension` (string) — Optional. Specifies the name of an extension to retrieve the version for.
- Returns: (string) — The version string, or **false** if the extension is not installed.

`echo` is a *language construct* used to output one or more expressions to the output buffer. It is the most commonly used output mechanism in PHP.

- Parameters: `arg1` (mixed), `...` (mixed) — A list of expressions to output.
- Returns: (void)

`print` is another *language construct* used to output a string. Unlike `echo`, it behaves similarly to a function because it returns a value, allowing it to be used within expressions.

- Parameters: `arg1` (string) — The value to output.
- Returns: (int) — Always returns `1`.

`printf()` outputs formatted strings using *format specifiers*, allowing variables to be embedded within structured output.

```php
printf("PHP Version: %s", phpversion());
```

This function is commonly used when precise *string formatting* is required.

## Types and Variables

### Variable Declaration and Syntax

Variables in PHP are represented by a dollar sign **$** followed by the name of the variable. Unlike Python, which uses name binding, PHP variables are *containers* that hold values. The variable name is case-sensitive. A valid variable name begins with a letter or an underscore, followed by any number of letters, numbers, or underscores.

PHP also supports *variable variables*, where the name of a variable is determined dynamically using another variable. This is accomplished using a double dollar sign (`$$`).

```php
$name = "status";
$status = "active";

echo $$name; // active
```

PHP is a *weakly typed* language. This means there is no need to declare the type of a variable before using it. The *PHP engine* automatically converts variables to the appropriate data type based on the context in which they are used. This process is known as *type juggling*.

Variables may also reference the same underlying value in memory. When a variable is assigned by reference using the `&`operator, both variables point to the same value.

```php
$a = 10;
$b = &$a;

$b = 20;
echo $a; // 20
```

### Data Types

PHP supports ten fundamental data types, categorized into scalar, compound, and special types.

#### Scalar Types

- **bool**: Represents a boolean value, which can be either **true** or **false**.
- **int**: Represents whole numbers. The size of an integer is platform-dependent. Integers may be written in decimal, hexadecimal, octal, or binary notation.
- **float**: Represents floating-point numbers (also known as doubles). Floating-point values are subject to precision limitations, meaning some decimal values cannot be represented exactly.
- **string**: A sequence of characters.

```php
$decimal = 42;
$hexadecimal = 0x2A;
$octal = 052;
$binary = 0b101010;

echo 0.1 + 0.2;
```

#### Compound Types

- **array**: An ordered map that associates values with keys. It can be used as a traditional array, list, hash table, dictionary, or stack. Numeric keys automatically increment, while string keys create associative arrays.
- **object**: An instance of a class.
- **callable**: Represents a function or method that can be invoked.
- **iterable**: Represents either an **array** or an **object** implementing the `Traversable` interface.

```php
$user = [
    "name" => "Alice",
    "age" => 25
];
```

#### Special Types

- **resource**: A special variable holding a reference to an external resource, such as a database connection or file handle.
- **null**: Represents a variable with no value assigned.

### Type Casting

Although PHP performs automatic type conversion, explicit type casting can be used to convert values to a specific type.

Common casting operators include `(int)`, `(float)`, `(string)`, `(bool)`, `(array)`, and `(object)`.

```php
$value = "25";
$integer_value = (int) $value;
```

### Truthy and Falsy Values

Because PHP performs implicit type conversions, many values evaluate to **false** in a boolean context. These values are often referred to as *falsy values*.

Common falsy values include:

- `false`
- `0`
- `0.0`
- `""`
- `"0"`
- `null`
- `[]`

All other values generally evaluate to **true**.

### Variable Scope

The *scope* of a variable refers to the context within which it is defined. PHP supports three primary variable scopes.

- **Local Scope**: A variable declared within a function is local to that function and cannot be accessed outside of it.
- **Global Scope**: A variable declared outside a function has global scope. To access a global variable within a function, the **global** keyword must be used.
- **Static Scope**: Normally, local variables are destroyed when a function finishes execution. A variable declared with the **static** keyword retains its value between function calls.

```php
function counter() {
    static $count = 0;
    $count++;
    echo $count . "\n";
}
```

### Constants

Constants are identifiers whose values cannot change during script execution. Unlike variables, constants do not use the dollar sign prefix.

Constants can be declared using `define()` or the **const** keyword.

```php
define("APP_VERSION", "1.0");
const MAX_USERS = 100;
```

Constants are commonly written in uppercase to distinguish them from variables.

### Type Manipulation and Checking Functions

`gettype()` retrieves the type of a variable.

- Parameters: `value` (*mixed*) — The variable being checked.
- Returns: (*string*) — Possible values include `"boolean"`, `"integer"`, `"double"`, `"string"`, `"array"`, `"object"`, `"resource"`, `"resource (closed)"`, `"NULL"`, or `"unknown type"`.

`settype()` sets the type of a variable.

- Parameters: `var` (*mixed*) — The variable to be converted (passed by reference), `type` (*string*) — The desired type.
- Returns: (*bool*) — **true** on success or **false** on failure.

`isset()` determines whether a variable is declared and is not **null**.

- Parameters: `var` (*mixed*) — The variable to check.
- Returns: (*bool*) — **true** if the variable exists and is not **null**.

`empty()` determines whether a variable is considered empty. A variable is empty if it does not exist or if its value evaluates to **false**.

- Parameters: `var` (*mixed*) — The variable to check.
- Returns: (*bool*) — **true** if the variable is empty.

`unset()` destroys a given variable and removes it from the current scope.

- Parameters: `var` (*mixed*) — The variable to be destroyed.
- Returns: (*void*)

PHP also provides a family of *type checking functions* that return a boolean value indicating whether a variable matches a specific type.

- `is_int()`
- `is_float()`
- `is_string()`
- `is_bool()`
- `is_array()`
- `is_object()`
- `is_null()`
- `is_callable()`

### Debugging Functions

`var_dump()` outputs detailed information about a variable, including its type, value, and length.

`print_r()` displays human-readable information about a variable, most commonly used with arrays and objects.

```php
$value = 10;
$array = ["a", "b", "c"];

var_dump($value);
print_r($array);
```

### Example

```php
<?php

// Declaration and Type Juggling
$item_count = 10;          // Integer
$price = 15.50;            // Float
$is_available = true;      // Boolean
$label = "Inventory: ";    // String

$total = $label . ($item_count * $price);
echo $total . "\n";

// Variable Scope
$global_context = "System Active";

function check_status() {
    global $global_context;
    static $access_count = 0;

    $access_count++;
    echo $global_context . " - Access number: " . $access_count . "\n";
}

check_status();
check_status();

// Constants
define("APP_VERSION", "1.0");

// Type Checking
if (isset($item_count)) {
    echo "Variable type is: " . gettype($item_count) . "\n";
}

// Debugging
var_dump($item_count);

// Destroy variable
unset($item_count);

?>
```

## Strings and Operations

### String Literal Delimiters

PHP provides multiple ways to specify a string literal. The choice of delimiter determines whether the *PHP engine* performs *variable interpolation* or interprets *escape sequences*.

- **Single Quotes**: Strings enclosed in single quotes ('') are treated as literal text. The only escape sequences recognized are the backslash (\) and the single quote itself ('). Variables inside single-quoted strings are not expanded.
- **Double Quotes**: Strings enclosed in double quotes ("") allow for *variable interpolation* and a wide range of *escape sequences* (e.g., \n for newline, \t for tab). When a variable name is placed inside double quotes, its value is parsed and included in the final string.

### Heredoc and Nowdoc

For multi-line strings or blocks of text containing many quotes, PHP offers *Heredoc* and *Nowdoc* syntax.

- **Heredoc**: This syntax behaves like double-quoted strings. It starts with `<<<` followed by an identifier, then the string content, and ends with the same identifier on a new line. It supports *variable interpolation*.
- **Nowdoc**: This syntax behaves like single-quoted strings. It is specified similarly to a Heredoc, but the initial identifier is enclosed in single quotes (e.g., `<<<'EOT'`). No parsing of variables occurs within a Nowdoc.

### Concatenation

Unlike many languages that use the plus sign (+), PHP uses the dot operator (**.**) for *string concatenation*. To append a string to an existing variable, the **.=** assignment operator is utilized.

### String Functions

The following functions provide essential tools for *string manipulation* and analysis.

`strlen()`: This function calculates the length of a string.

- Parameters: `string` (string) — The string being measured.
- Returns: (int) — The length of the string in bytes.

`strpos()`: This function finds the position of the first occurrence of a substring in a string.

- Parameters: `haystack` (string) — The string to search in, `needle` (string) — The substring to search for, `offset` (int) — Optional. The position to start searching.
- Returns: (int|false) — The numeric position of the first occurrence. If the substring is not found, the function returns **false**.

`str_replace()`: This function replaces all occurrences of a search string with a replacement string.

- Parameters: `search` (array|string) — The value being searched for, `replace` (array|string) — The replacement value, `subject` (array|string) — The string or array being searched and replaced, `count` (int) — Optional. A variable passed by reference that will hold the number of replacements performed.
- Returns: (string|array) — The resulting string or array after replacements.

`substr()`: This function returns a portion of a string.

- Parameters: `string` (string) — The input string, `offset` (int) — The start position (negative values start from the end), `length` (int) — Optional. The length of the returned substring.
- Returns: (string|false) — The extracted part of the string or **false** on failure.

```php
<?php
$language = "PHP";
$version = 8.2;

// Interpolation in double quotes
echo "Learning $language $version is efficient.\n";

// Literal interpretation in single quotes
echo 'The variable $language will not expand here.' . "\n";

// Heredoc syntax
$heredoc = <<<EOD
This is a multi-line string.
It supports interpolation: $language.
EOD;

// String manipulation
$raw_data = "  error_log_2024.txt  ";
$clean_data = trim($raw_data);
$file_ext = substr($clean_data, strpos($clean_data, ".") + 1);

echo "File extension identified: " . $file_ext . "\n";
echo "Character count: " . strlen($clean_data) . "\n";
?>
```

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

## Control Flow

### Overview

Control flow structures in PHP determine the order in which code is executed. They allow conditional execution, repetition (loops), and early termination of scripts.

### Conditionals

PHP provides structures to execute code based on logical conditions that evaluate to a *boolean* value.

#### If, Else, and Elseif

The **if** statement executes a block of code only if the condition evaluates to **true**.

- **else**: Defines a block executed when the **if** condition is false.
- **elseif**: Checks additional conditions if the first **if** is false.

```php
if (condition) {
    // code if true
} elseif (condition2) {
    // code if elseif true
} else {
    // code if all false
}
<?php
$status = "processing";

if ($status === "idle") {
    echo "System is waiting.\n";
} elseif ($status === "processing") {
    echo "System is active.\n";
} else {
    echo "Status unknown.\n";
}
?>
```

#### Switch

The **switch** statement compares one expression against multiple values.

Rules:

- Uses **case** labels and a **default** label.
- **break** is needed to prevent *fall-through*.

```php
switch ($variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code if no match
}
<?php
$day = "Monday";

switch ($day) {
    case "Monday":
        echo "Start of the week";
        break;
    case "Friday":
        echo "End of the week";
        break;
    default:
        echo "Midweek day";
}
?>
```

#### Match (PHP 8+)

The **match** expression is a concise alternative to **switch**.

Rules:

- Uses **strict comparison** (`===`).
- Returns a value.
- No **break** required.

```php
$value = match ($variable) {
    value1 => result1,
    value2 => result2,
    default => default_result,
};
<?php
$status = "processing";
$message = match ($status) {
    "idle" => "Standby mode.",
    "processing" => "Task in progress.",
    default => "Error encountered.",
};
echo $message . "\n";
?>
```

### Iteration

Loops allow repeating code as long as a condition holds.

#### While Loop

The **while** loop checks the condition before each iteration. The code block may never execute if the condition is false initially.

```php
while (condition) {
    // code
}
<?php
$count = 5;
while ($count > 0) {
    echo "Countdown: $count\n";
    $count--;
}
?>
```

#### Do-While Loop

The **do-while** loop executes the code block at least once before checking the condition.

**Syntax:**

```php
do {
    // code
} while (condition);
<?php
$count = 1;
do {
    echo "Count is $count\n";
    $count--;
} while ($count > 0);
?>
```

#### For Loop

The **for** loop is used when the number of iterations is known.

```php
for (initialization; condition; increment/decrement) {
    // code
}
<?php
for ($i = 1; $i <= 5; $i++) {
    echo "Iteration $i\n";
}
?>
```

#### Foreach Loop

The **foreach** loop is designed for iterating over arrays or objects.

Rules:

- Can retrieve just the value: `foreach ($array as $value)`
- Or both key and value: `foreach ($array as $key => $value)`

```php
foreach ($array as $value) { ... }
foreach ($array as $key => $value) { ... }
<?php
$settings = ["timeout" => 30, "retries" => 3];
foreach ($settings as $key => $value) {
    echo "Setting: $key is set to $value\n";
}
?>
```

### Control Flow Functions

#### sleep()

Definition: Pauses script execution for a number of seconds.

Parameters:

- `seconds` (int) — Number of seconds to sleep

Return: int — Returns 0 on success, **false** on error

```php
<?php
echo "Pausing...\n";
sleep(2); // wait 2 seconds
echo "Resumed.\n";
?>
```

#### usleep()

Definiti on: Pauses execution for microseconds (1 million microseconds = 1 second).

Parameters:

- `microseconds` (int) — Number of microseconds to sleep

Return: void

```php
<?php
echo "Waiting 0.5 seconds...\n";
usleep(500000); // 0.5 seconds
echo "Done.\n";
?>
```

#### exit() and die()

Definition: Terminates script execution immediately.

Parameters:

- `status` (string|int, optional) — Message or exit code

Return: void

> [!NOTE]
>
> `die()` is an alias of `exit()`.

```php
<?php
$status = "complete";
if ($status === "complete") {
    die("Process complete. Exiting.\n");
}
echo "This will not run.\n";
?>
```

Perfect! I can rewrite your **Object-Oriented PHP** section in your preferred style, consistent with your **Arrays** and **Control Flow** examples. This means:

- Description first
- Syntax/Rules explained
- Code examples small and focused
- Parameters/Return info for functions

Here’s the rewritten version:

------

# Object-Oriented PHP

## Classes and Objects

### Overview

*Object-oriented programming* (OOP) organizes code around objects, which contain *properties* (data) and *methods*(functions).

- A *class* is a blueprint for creating objects.
- An *object* is an instance of a class.

------

### Class Definition and Properties

A class is defined using the **class** keyword. Inside, variables are called *properties* and functions are called *methods*.

**Rules:**

- Class names usually use *PascalCase*.
- Properties require a *visibility modifier*: `public`, `protected`, or `private`.
- `$this` refers to the current object instance.

```php
class ClassName {
    public $property;

    public function methodName() {
        // code
    }
}
```

------

### Visibility Modifiers

Visibility controls where properties and methods can be accessed:

- **public** — accessible anywhere.
- **protected** — accessible in the class and child classes.
- **private** — accessible only in the class that defines it.

```php
<?php
class Example {
    public $name;      // accessible anywhere
    protected $id;     // accessible in this class and children
    private $secret;   // accessible only in this class
}
?>
```

------

### Inheritance

*Inheritance* allows a class to reuse properties and methods from another class using `extends`.

Rules:

- Only *single inheritance* is supported (one parent per class).
- Child classes inherit **public** and **protected** members.
- Methods can be **overridden** in the child class.
- **final** prevents overriding or inheritance.

```php
<?php
class ParentClass {
    public function greet() {
        return "Hello from parent!";
    }
}

class ChildClass extends ParentClass {
    public function greet() {
        return "Hello from child!";
    }
}

$child = new ChildClass();
echo $child->greet(); // "Hello from child!"
?>
```

------

### Abstract Classes

**Abstract classes** cannot be instantiated directly. They may contain **abstract methods** that child classes must implement.

```php
abstract class Device {
    abstract public function turnOn(): string;
}
```

------

### Interfaces

An **interface** defines a **contract**: a set of methods that a class must implement.

- Use `interface` to define the methods.
- A class implements an interface with the `implements` keyword.

```php
<?php
interface Connectable {
    public function connectToNetwork(string $ssid): bool;
}

class Laptop implements Connectable {
    public function connectToNetwork(string $ssid): bool {
        echo "Connecting to $ssid...\n";
        return true;
    }
}
?>
```

### OOP Utility Functions

#### `class_exists()`

**Definition:** Checks if a class has been defined.

**Parameters:**

- `class_name` (string) — Class name
- `autoload` (bool, optional) — Whether to call autoloader

**Return:** bool — True if the class exists

```php
<?php
if (class_exists("Laptop")) {
    echo "Laptop class exists.\n";
}
?>
```

------

#### `method_exists()`

**Definition:** Checks if a method exists in an object or class.

**Parameters:**

- `object_or_class` (object|string) — Object instance or class name
- `method_name` (string) — Name of the method

**Return:** bool — True if method exists

```php
<?php
$myLaptop = new Laptop();
if (method_exists($myLaptop, "connectToNetwork")) {
    echo "Method exists.\n";
}
?>
```

------

#### `property_exists()`

**Definition:** Checks if a property exists in an object or class.

**Parameters:**

- `object_or_class` (object|string) — Object instance or class name
- `property` (string) — Property name

**Return:** bool — True if property exists

```php
<?php
if (property_exists($myLaptop, "batteryLevel")) {
    echo "Battery property exists.\n";
}
?>
```

------

#### `get_class()`

**Definition:** Retrieves the class name of an object.

**Parameters:**

- `object` — The object to check

**Return:** string — Class name

```php
<?php
echo "Class: " . get_class($myLaptop) . "\n"; // "Laptop"
?>
```

------

### Full Example Combining OOP Concepts

```php
<?php
// Abstract class
abstract class Device {
    protected string $serialNumber;

    public function __construct(string $sn) {
        $this->serialNumber = $sn;
    }

    abstract public function turnOn(): string;
}

// Interface
interface Connectable {
    public function connectToNetwork(string $ssid): bool;
}

// Inheritance and implementation
class Laptop extends Device implements Connectable {
    private int $batteryLevel = 100;

    public function turnOn(): string {
        return "Laptop system booting...";
    }

    public function connectToNetwork(string $ssid): bool {
        echo "Connecting to $ssid...\n";
        return true;
    }
}

// Instantiation
$myWorkLaptop = new Laptop("SN-98765");

if (class_exists("Laptop")) {
    echo "Current Class: " . get_class($myWorkLaptop) . "\n";
}

if (method_exists($myWorkLaptop, "turnOn")) {
    echo $myWorkLaptop->turnOn() . "\n";
}

if (property_exists($myWorkLaptop, "batteryLevel")) {
    echo "Battery property exists.\n";
}
?>
```

## Static Methods and Properties

### Overview

In PHP, the **static** keyword allows for the definition of class *properties* and *methods* that belong to the class itself rather than to a specific *object instance*. This is useful for utility functions or data that should be shared across all instances of a class.

### Static Properties

Static properties cannot be accessed through an instantiated *object* using the arrow operator (**->**). Instead, they are accessed using the *Scope Resolution Operator* (**::**).

**Rules**:

- Declared with the **static** keyword.
- They retain their value throughout the script execution.
- Within a class, they are accessed using the **self** keyword followed by the double colon.

**Syntax**:

PHP

```
class ClassName {
    public static $property = "value";
}
// Accessing outside
echo ClassName::$property;
```

### Static Methods

Like properties, static methods are called on the class, not on an object. They are frequently used for *factory patterns* or *helper methods*.

**Rules**:

- Because static methods are not bound to an instance, the **$this** pseudo-variable is not available inside them.
- They can be called even if no instance of the class exists.

**Syntax**:

PHP

```
class ClassName {
    public static function methodName() {
        // code
    }
}
// Calling outside
ClassName::methodName();
```

### Late Static Binding

PHP uses *Late Static Binding* to resolve the class being called in the context of *inheritance*. While **self** always refers to the class where it is written, the **static** keyword (when used for resolution) refers to the class that was actually called at *runtime*.

### Related Keywords

```
self
```

Definition: A keyword used to reference the current class. It is used to access *static* members or *constants* from within the class definition.

```
parent
```

Definition: A keyword used to access *static* members or *methods* of the *parent class* that are being overridden in the current class.

`static` (as a scope)

Definition: When used in a method, it allows the *PHP engine* to reference the class that was initially called, enabling *polymorphic* behavior for static calls.

PHP

```php
<?php
class SystemConfig {
    public static int $max_connections = 100;

    public static function getLimit(): int {
        return self::$max_connections;
    }
}

class CustomConfig extends SystemConfig {
    // Overriding the static property
    public static int $max_connections = 500;

    public static function getLimit(): int {
        // Late static binding would use 'static'
        // 'self' would return 100 (from SystemConfig context)
        // 'static' returns 500
        return static::$max_connections;
    }
}

echo "Global Limit: " . SystemConfig::getLimit() . "\n";
echo "Custom Limit: " . CustomConfig::getLimit() . "\n";

// Accessing parent property directly
echo "Parent Default: " . CustomConfig::$max_connections . "\n";
?>
```