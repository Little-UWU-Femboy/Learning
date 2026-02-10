# Python

## Chapter 1: Introduction

To check python version do `python3 --version`.

All python files end with the **.py** function.

There are two ways to run python code:

1. Using the *python interactive shell*. To do this just type `python` on the CLI, then just type python code and hit enter.
2. Using the python interpeter to run a file with `python3`, then follow it by the python file.

To print text to the screen, use the function `print()`.

In each of the python versions, it comes with standard libraries. To do this, use the **import** keyword followed by the python package name.

When importing content from Standard libraty, there is a keyword called **from** that will take only the specified content from that library. It will look like `from <library> import <content(s)>`.

Python is like Java where no manual memory needs to be done. Instead, it uses the *garbage collecton* to do the memory clean up.

## Chapter 2: Types and Variables

To create a variable, do `VariableName = Value`. However, unlike other languages, the way python stores the data values is different. Other languages have a pointer thing that points directly at the memory address of the data *(statically typed*). However, python is a *dynamically typed* language, meaning it keeps track of data differently. It treats the variable as just a name and stores the data like id, data type, value, reference count, etc in memory on the heap. Because of this, python can reassign a variable to ANY data type at any time unlike a statically types language.

Exploring the different parts of the way data is stored:

- **variable name**: This is just the name that data is called in memory and is called the *label* or *reference*.
- **id**: Each object in memory will have a unique ID number. This helps to identify each variable in memory differently. The ID value of a **variable name** can be see by using the `id(VariableName)` function. This will just return that variables ID value.
- **types**: This tracks the type of data that it is storing.
- **value**: This stores the actual bits and bytes to represent the data being stored.
- **reference count**: This tracks how many different variables are referencing this same memory data. Once the reference count hits 0, no variables can reference the data any more. This means python marks it for garbage clean up.

> [!NOTE]
>
> When reassigning ANY, be it the same or different, variable data; this creates a whole new object in memory.

> [!IMPORTANT]
>
> For optomiation, python actually creates objects for values -5 to 255. This means

```python
x = 50 # This is a variable and creates an object
x = 60 # This creates a new object to point and hold the data 60 with a new ID value
x = "Yes" # This now holds string data and has a whole new ID value in memory again
```

Unlike java, python does have a manual way to get rid of a variable in memory manually using the **del** keyword. It is not a function call and use it like `del VariableName`. This will delete that variable reference and deincrement that objects reference count.



Pythons reservered keywords are:

- False
- None
- True
- and
- as
- assert
- async
- await
- break
- class
- continue
- def
- del
- elif
- else
- excpet
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield

When it comes to naming variables, python using the *snake casing* convention (disgusting). Python using *pascal casing* when defining custom classes. When making a variable name, it follows the standard naming rules: can have letters A-Z,a-z, and underscore. 

> [!WARNING]
>
> Python does not have a way to make constant variables. However, it uses the convention of having the word all upper caps with the snake casing like `MAX_AGE`. This symbolizes that variables data should never be reassigned.

> [!NOTE]
>
> Python for OOP, python does not have a private keyword, so to indicate a variable is representing a private variable, put a single underscore when naming the variable like `_name`. Anything that starts with a double underscore has a special usage when creating object classes. Names that start AND end with a double underscore are called **dunder methods** that are also used for object classes.



When it comes to the data types python can have are:

- **bool**: values *True* and *False*. This is not mutable.

- **int**: values 47, -2, 4999494, etc. This is not mutable.
- **float**: values 3.2, 2.7e5, -1.0, etc. This is not mutable.
- **complex**: 3j, 5 + 9j, etc. This is not mutable.
- **str**: "yes", 'no', "Live, Like, Love", `:```Testing``` :`(only need the triple back ticks, but typora quirk) etc. This is not mutable.
- **list**: This is used to store an array style of data. This is mutable.
- **tuple**: This is another way to store data like an array. This is not mutable.
- **bytes**:  Hard to describe the values for this; look it up later. This is not mutable.
- **Bytearray**: Hard to describe the values for this; look it up later. This is mutable.
- **set**: Kind of like an array, but for making sets. This is mutable.
- **frozenset**: This is like a set except it is not mutable.
- **dict**: This is a way to make key value pairs. This is mutable.



## Chapter 3: Numbers

This section talks about the python basic data types.

### boolean

Python has a way to convert a value to a **bool** type by using the type casting `bool(VariabeName, ...)`. This turns the variable(s) inside to be a *True* or *False* value.  Anything is considered *True* if the value is anything besides 0 or a non-empty string and *False* otherwise.

### Integer

An integer can start with 0b, 0o, or 0x and this will make an binary, octal, or hexadecimal number respectfully. 

To make negative number do - in front of number.

Python allows putting _ between number to improve readability like 5_000_000 for 5 million which is the same as 5000000.

#### Integer Operations

This has the normal: + (addition), - (subtraction), * (multiplication), / (floating point division), and % (module remainder). 

There are two special things that can be done:

1. `**`: For doing a number reaised to the power; syntax is x**y where x is the base and y is the exponent.
2. `//`: For division as well, except this will round the number down to the nearest whole number. Unlike the normal version that keeps it inflating point form.

> [!NOTE]
>
> When dividing with /, this will always return a floating point number even if the two numbers being divided are whole numbers.

Can also do the short had opertaions like *= , +=, etc.

There is a special function called `divmod()` that takes two arguments. The first is the number to be divided and the second it the number that it is going to be divided by. This willl return two values with the first being the number of times divided into and the second will be the remaineder. However, the numbers are returned as a **tuple**.

There is a function called `chr()` that takes a number and returns a single UTF-8 encoded character. There is a function called `ord()` that takes a single charctar and returns the integer value for it.

To convert something to an integer use the `int()` function that takes a single argument. The return values are:

- **bool**: *True* and *False* will return 1 or 0,
- **float**: Returns a whole number rounded down.
- **string**: If the string is a number then it will return the numeric value for it. Anything else will cause an error. Even trying a float string number to convert will not work as well

### Floats

A float type can use and handles operations the same as integers.

To convert something to a float use the `float()` function that only takes one value. This works exactly like the `int()` version except it can convert decimal string values into a float number.

There is a function called `round()` that takes a single float value and optional second value. This will round the number number all the way up to the nearest whole number or if a second parameter was specified then it will remove that many decimal point numbers from the right most side. One important thing to note this does not affect the original value and instead just returns a new copy of the value.

There is a special **module** called "fractions". This is a different way to handle divinig floating point numbers.



## Chapter 4: Strings

Strings are an example of squenced ordered data which is just a squence of characters. Some information you can get are:

- If a particular element is in the string
- Index of element and its value
- Element at particulat index
- Slice of element in given range
- Length of squence
- Min and max element values

In python, string are *immutable*. Meaning once assigned to a variable it cannot changes its value, but it can return a new copy subset of the original.

A string made by double or single quotes is treated the same way unlike in C where the difference matters.

There are a few special ways to make a string in python:

- **f-string**: This string type will start with the letter "f" BEFORE the quotation marks and not inside. This is used to get string formatting. 
- **r-string**: This is a raw string. This will not intepert ANYTHING in the string and will keep it in its raw form. This prevents things like escape characters from being converted. This is made the same way as an **f-string** except stats with an "r".
- **unicode string**: This is the same thing as making a normal string and really no need to put this. However, this does start with a "u"
- **byte string**: This is used to make a string of bytes.

The reason single or double quotes can be used to make a string is they can both do small different things. If a double quote is used, it can use single quotes inside without having to escape it and vice versa with single quotes.

A string can also be made with tree single/double quotes. This are really used to create multi-line strings since it will keep the formatting of text spaning multiple lines.

With strings, there is a special value called **EOL** and this means the end of line was reached.

Something can be type casted into a string with the `str()` function that takes a single argument. This can take an integer, number, and boolean (return the string version True or False).

Can use the \ to escape the special characters in a string to be able to use them like \t, \n, \\`, \\", \\\, etc.

To combine two stirngs, the use of the addition operator is used and this concats the strings. The first stirng will have the second added to the back of it.

```python
x = "Yes"
y = "No"

concat = x + y 
print(concat)
# OUTPUT --> YesNo
```

A special syntax for strings is using the multiplication symbol. This will take the string and appead that thing to itself n - 1 times. For example:

To access individual characters in a string, use the bracket notation and use the index starting from 0 to n - 1.

```python
x = 4 * "Yes"
print(x)
print(x[2])
# OUTPUT
# ----------
# YesYesYesYes
# s
```

> [!WARNING]
>
> Unlike other languages, indexes can be accessed using negative numbers inside it. Except, this just starts in the opposite direction going from right to left. For example
>
> ```python
> letters = "abcdefg"
> print(letters[0])
> print(letters[-1])
> print(letters[-2])
> # OUTPUT
> # ----------
> # a
> # g
> # f
> ```

Going past the available index length will raise the apporiate exception.

There is a method that the **str** class has that all string types have access to called `replace()`. This will take two arguments with a third optional one. The first is the substring to be placed. The second is the substring that it will be replaced by. The optional third will be the maximum times the substring will be replaced. This does not affect the original copy since it returns a new copy of the made string.

Another way to get a substring is using *string slicing*. This also uses the square bracket notation, but it a different index notation. The syntax of it is `start:end:skip`.

1) start: this will be the starting index where the letters will be copied from.
2) end: this will be the last index the character will copy from. This is non-inclusive so this really would copy from start to (end - 1).
3) skip: this will be how many indexes to skip before copying the next letter. This is the only optional parameter and if notihng is specified then it will skip nothing.

> [!NOTE]
>
> Becasue the third paremeter is optional, this means the slice specification can also just be `start:end`. 
