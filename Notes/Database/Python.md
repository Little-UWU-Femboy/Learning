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

### Declaring Variable

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

###  Python Keywords

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

### Data Types

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

A string can also be made with three single/double quotes. This are really used to create multi-line strings since it will keep the formatting of text spaning multiple lines.

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

A special syntax for strings is using the multiplication symbol. This will take the string and append that thing to itself n - 1 times. For example:

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

Going past the available index length will raise the appropriate exception.

There is a method that the **str** class has that all string types have access to called `replace()`. This will take two arguments with a third optional one. The first is the substring to be placed. The second is the substring that it will be replaced by. The optional third will be the maximum times the substring will be replaced. This does not affect the original copy since it returns a new copy of the made string.

### String Slicing

Another way to get a substring is using *string slicing*. This also uses the square bracket notation, but it a different index notation. The syntax of it is `start:end:skip`.

1) start: this will be the starting index where the letters will be copied from.
2) end: this will be the last index the character will copy from. This is non-inclusive so this really would copy from start to (end - 1).
3) skip: this will be how many indexes to skip before copying the next letter. This is the only optional parameter and if nothing is specified then it will skip nothing.

> [!NOTE]
>
> Because the third parameter is optional, this means the slice specification can also just be `start:end`. Also, if the entire is to be copied, then all that needs to be done is put `:` for the string slice. Any of these parts can be omitted, 

To get the total size of a string, use the `len()` function. This is a function that will return an integer value of the number of characters in the string.

A specific string only function is called the `split()`. This means anything that is considered part of the str class has access to this method. This function will return 0 or more sub strings of the split content by a certain separator; an example is csv data. This takes one argument only and that is the thing to split the string by. If nothing is specified then it will split by then it uses all whitespace characters (spaces,newline, and tabs).

```python
x = "Jack, 32, Linux 123 st"
print(len(x)) # outputs --> 22
print(x.split(",")) # outputs --> ['Jack', ' 32', ' Linux 123 st']
print(x[1:12]) # outputs --> ack, 32, L
```

Another class **str** specific method is `join()`. This is the opposite of `split()` since this joins strings together based on the specified separator. This takes only one value, that being the list of strings to join together. However, the actual string this method is called on is the thing that it will join based on.

> [!NOTE]
>
> A string does not have to be assigned to a variable to use the methods of the respected type. A good example of this is when called the `join()`, this used that particular method.
>
> ```python
> x = ["Yes", "No", "Maybe"]
> print("\n".join(x))
> 
> # OUTPUT
> # ---------
> # Yes
> # No
> # Maybe
> 
> # The returned string will all be one single string
> ```

There are ways to check certain things in a string to see if a certain pattern is there like for a prefix and suffix. The other **str** specific methods are:

1.  `startswith()`: This takes a single string argument and checks if the string starts with that specific string in the argument.
2.  `endswith()`: This takes a single string argument and checks if the string ends with that specific string in the argument.
3.  `removeprefix()`: This takes a single string argument and remove that string from the start of the string if it does exist.
4.  `removesuffix`: This takes a single string argument and remove that string from the end of the string if it does exist.



There is another method called `strip()` that removes content from the string. This is useful to remove whitespace, newlines, tabs, etc. This function takes one argument and that is what the specific type of thing to remove. However, is nothing is provided then it will remote all the different whitespace types. The string provided can contain multiple different things to remove and does not just have to be one. This does NOT remove the content from the middle of the string and JUST the left and right most side of it.

```python
x = "   Silly ?! Earth"

print(x.strip(" !")) # outputs --> Silly ?! Earth

# The returned string does not have the spacing issue before the "Silly" word
```

There are two specific **str** functions to find a particular word in a string which are `find()` and `index()`. These both work the same in that they will search the entire string and return the lowest index position that pattern is found. The difference between them is how they handle errors. `find()` will return -1 if the string pattern is not found. `index()` will raise an exception making sure that the issue of the sub string not being there is addressed right away. Both of these take the same arguments:

1.  The specified string pattern to look for
2.  The starting index this will look in the string
3.  The ending index - 1 this will look in the string

```python
def start():
    text = "hello world"

    # Using find()
    print(text.find("world"))   # found
    print(text.find("Python"))  # not found

    # Using index()
    print(text.index("world"))  # found
    print(text.index("Python")) # not found (this will crash!)

if __name__ == "__main__":
    start()

# OUTPUT
# ----------
# 6
# -1
# 6
# Traceback (most recent call last):
#  File "C:\Users\Owner\HOME\Learning\Code\Python\Main.py", line 13, in <module>
#    start()
#    ~~~~~^^
#  File "C:\Users\Owner\HOME\Learning\Code\Python\Main.py", line 10, in start
#    print(text.index("Python")) # not found (this will crash!)
#         ~~~~~~~~~~^^^^^^^^^^
#ValueError: substring not found
```

There is a **str** method to check how many times a substring occurs in the actual string called  `count()`. This just takes a single argument of a substring and returns the total number of times that was found.

There are some special methods that just change the words of the string. These are: 

- `capitalize()`: This takes no argument and just caps the first letter of the first word of the string
- `title()`: This takes no argument and caps all the first letter of the first word of the entire string
- `upper()`: This takes no argument and returns the whole string in capped letters
- `lower()`: This takes no argument and returns the whole string in lowercased version
- `swapcase()`: This takes no arguments and returns capped letter uncapped and vice versa

There are some methods to deal with alignment of strings as well like:

- `center()`: This takes a singe argument and it is an integer for how much space there should be added on both sides of the string to make it even
- `ljust()`: This takes a singe argument and it is an integer for how much space there should be added on the left side of the string to make it left justified
- `rjust()`: This takes a singe argument and it is an integer for how much space there should be added on the right side of the string to make it right justified 

When it comes to printing out formatted data, there is the old and new way to do it:

- Old way: this version is like C with the %d, %s, etc.
- `format()` method: 
- **f-string** (recommended) : this uses the **f-string** syntax to complete this. The string will first start with the letter "f", but placed outside right at the start of the ". Inside the string use curly braces and inside those put the name of the value or variable and that will have the variable name replaced with the actual value. Inside the braces can even be complex single like operations like `len(x.count("This"))` or math operations.

```python
def start():
    name = "Alice"
    age = 30
    price = 4.56789

    print(f"My name is {name} and I am {age} years old.")
    print(f"Next year I will be {age + 1}.")
    print(f"The price is ${price:.2f}")


if __name__ == "__main__":
    start()
```



## Chapter 5: Bytes and Bytearray

Skipped for now as not important for core class leaning, but come back to this



## Chapter 6: if and match

### If statement

When it come to making an if statement, the basic version is made with the keyword **if** and **else**. The syntax for this is:

This has a weird syntax because python sorts the code can tell what is part of what by  using indentation rules and using the colon to indicate when something like an if statement started and the next following lines will need to be indented to be part of that statement. Also, important to note the condition area does not use parentheses and it just needs to be written.

Python uses the keyword **elif** instead of "else if" like other languages.

```python
if FirstLogicComparision:
  # Code for if here
elif SecondLogicComparision:
  # Code for elif here
else:
  # Code for else here

# Rest of program here
```

The normal equality operators ==, !=, <, <=, >, >= are used the same as in other languages. However, when ot comes to making more complex comparisons, pyhon does uses **and**, **or**, and **not** instead of &&, |, or !. This would also be the time to use parentheses if needing to group stuff together to make complex logic comparisons.

```python
def start():
    age = 17
    has_id = True
    is_admin = False

    if age >= 18 and has_id:
        print("Adult with ID")

    if age < 18 or is_admin:
        print("Minor or admin access")

    if not has_id:
        print("ID required")


if __name__ == "__main__":
    start()
```

Whenever the need to make multiple comparisons is needed and insead of making a long if statement chain, use the **in** keyword which is a *membership comparison*. This test if a certain value exist in a collection or sequence like a string. For example, if wanting to test if a letter is a vowel, instead writing mutiple if statements or using a bunch of **or** keyword, use **in**. This returns false if not part of it and true otherwise.

```python
def start():
    fruits = ["apple", "banana", "orange"]
    name = "Alice"
    letter = "A"

    if "apple" in fruits:
        print("Apple is in the list")

    if "z" not in name:
        print("The letter 'z' is not in the name")

    if letter in name:
        print("Letter found in name")


if __name__ == "__main__":
    start()
```

There is a way to create a *ternary operator*, which is a shorter more concise way to make an if statement to assign a variable to it. The syntax for this is `VariableName = TrueValue if Condition else FalseValue`. 



### Match statement

There is something called **match** which is like a *switch statement* in C except the use of the **break** keyword is not needed at the end of each case to prevent fall through. However, there are different types of **match** statements that can be made:

#### Simple C like with strings

```python
def start():
    command = "start"

    match command: # thing that will be match against
        case "start": # Pattern to match
            print("Program starting...") # Code to run
        case "stop":
            print("Program stopping...")
        case "pause":
            print("Program paused.")
        case _: # Default Case
            print("Unknown command")


if __name__ == "__main__":
    start()
```

#### Structural Match

This is used to match multiple variables at once when the thing to match is a **tuple**, **dict**, **list**, **set**, and object. For example:

```python
def start():
    x = 50

    match (x, 5): # This is a tuple
        case (0, 0):
            print("Testing")
        case (x, 0):
            print("Only 5")
        case _:
            print("Who knows")


if __name__ == "__main__":
    start()
```



### Structural Guards

There is something called **structural guard** syntax. This allows putting an if statement in the *case statement*. This allows for extra protection in the **match** statement to see if the original . The way these are evaulated is ONLY IF the case statement check passes, then it move on to the **structural guard** and evaulates that, but if the case statement does not pass, then it will not run the **structural guard**. These 

````python
def start():
    x = 50
    match x:
        case 1:
            print("Testing")
        case 50 if x >= 100:
            print("Successful")
        case _:
            print("Who knows")

if __name__ == "__main__":
    start()
````

There is a special way to declare variables using the **walrus operator**. This is the `:=` like in Go. This is used to declare variables at certain times without having to declare them beforehand. If trying to do the same thing without using the **walrus operator** then this would cause a run time error since it would've needed to be declared before hand.

```python
def start():
    numbers = [3, 7, 10, 15]
    if (n := len(numbers)) > 3:
        print(f"The list has {n} items")

if __name__ == "__main__":
    start()
    # This example puts parentheses around the if statement to make sure the variable
    # can be declared and be used.
```



## Chapter 7: For and While

### While

To make a **while** loop do:

```python
while Condition:
  # CODE HERE
```

To have the while loop go until a specific event occurs, the condition can be set to *True* and then use the **break** keyword to leave the loop. The keyword **continue** can also be used to skip the rest of the code to run in the loop and go back to the top of the loop right away.

There is a way to use an **else** with the **while** syntax. This would go at the end of the **while** loop and indented at the same line. However, this **else** code block will only execure IF the **while** loop did not break and exited normally by the condition evaulating to false.

```python
x = 0
while True:
  print("Test")
  x++
  if (x >= 10):
    break
else:
  print("Loop completed without breaking")
```

### For

The **for** loop works a little differently compared to something like C; the syntax is:

```python
for PlaceHolder in CollectionThing:
  # CODE HERE
```

This make it so the "CollectionThing" will be the thing that will be itterated over. The "PlaceHolder" will be the thing that hold the actual data at the current index the loop is in.

Just like the **while** loop, the **break** and **continue** keywords can be used here as well.

Just like the **while** loop, it can have an ending **else** part that will only execute if the **for** loops exits natually.

There are times when there is no collection to itterate over and just want to do something a set number of times. This is when the `range()` syntax must be used. The `range()` has similar syntax to how string slicing works except it is seperated by commas and not slices. The syntax is `range(StartIndex, EndingIndex-1, Skip)` with the first parameter being required and the last two being optional.

```python
def start():
    # Loop from 0 up to 4
    for i in range(5):
        print(i)

    # Loop from 2 up to 6
    for i in range(2, 7):
        print(i)

    # Loop from 10 down to 2, step -2
    for i in range(10, 1, -2):
        print(i)

if __name__ == "__main__":
    start()
```



## Chapter 8: Tuples and Lists

A common way to store data in a data structure is a **tuple** and **list**.

### Tuple

A **tuple** is a way to store data in an indexed collection, but once that is made then the data inside can never change like adding/remove indexes or changing index values. To make a **tuple** use a set of parentheses and put the data inside comma seperated or can make an empty **tuple** by just putting the parentheses without data.

> [!NOTE]
>
> If only adding a single element inside the **tuple**, then it has to end with a comma even if no extra values are inside it. Otherwise, this will see that single value and just assign that single specified value inside it and not make a **tuple**.

When making the **tuple** with multiple values, this can be done by putting the data inside the parentheses and comma seperating it or drop the parentheses and just assign the variable to the comma seperated values and this makes a **tuple** as well. However, it is a little safer and cleaner to use the parentheses.

There is something called *unpacking* that is a way to extract all the data from a **tuple** and assign it to seperate variables. This is done by declaring variables on a single line comma seperated and assigning them to the made **tuple**. This will assign the values to the variables in the respective order of the **tuple** data. It is important that there is EXCATLY the same number of variables made as the size of the **tuple** else an error is raised.

There is a `tuple()` that is used to type cast another collection type to a **tuple**. Just put the other collection type inside the `tuple()` as this will be the only argument.

When it comes to accessing the **tuple** data, it uses normal indexing with brackets.

Two **tuples** can be added together and this will return a new **tuple** copy with the values from both combined.

When comparing two **tuples**, this works with the == syntax. This will return *True* only if the **tuples** are the exact same size and have same values in the same order. Otherwise return *False*. Can also use the >, <, etc symbols to compare the size of them as this will also return *True* or *False*.

Going back to the **for** loop, this is where it comes in handy. If the size of the **tuple** is not known, then can use the **for in**  syntax to loop through a collection like `for x in items:`.

### List

A **list** is almost the same as a C array except this does, the data inside it does not have to be of a specific type and can contain any mixture of data types. A **list** is mutable so indexes can be removed or added dynamically.

A **list** is made by using brackets and putting the data inside it. This can be an empty **list** by just assigning a variable to a set of brackets or can place values inside it comma seperated.

> [!NOTE]
>
> Unlike a **tuple**, if the **list** contains a single value, there is no need to end it with a comma like a **tuple**. This will keep this as a **list** type.

Just like **tuples**, there is a `list()` function to convert a different collection type to a **list** type.

An example of a **list** being used is the `split()` method for strings. This returns a **list** of the split substrings.

Just like a **tuple**, **list** elements are accessed using the bracket notation with the specified index.

Just like strings, the *slice* notation can be used on **list** types to return a new **list** with the specified values to copy. The notation syntax is EXACTLY the same as the string one.

> [!TIP]
>
> A trick to reverse a list it to do `listName[::-1]`. This will go starting from 0 to end of **list** and move starting from the right moving left and place that item at the top of the list. However, there is a function called `reverse()` that is on ALL collection types that ARE MUTABLE. So this would not be available on a **tuple** or **str**, but will be on a **list** type. However, unlike slicing, `reverse()` does modify the original mutable collection variable.
>
> 

```python
def start():
    # List: mutable, can change elements
    fruits = ["apple", "banana", "cherry"]
    print(fruits)
    fruits[0] = "orange"  # modify first element
    fruits.append("kiwi") # add new element
    print(fruits)

    # Tuple: immutable, cannot change elements
    dimensions = (1920, 1080)
    print(dimensions)
    # dimensions[0] = 1280  #  This would raise an error
    
    testTuple = ("YES",) # Make a single tuple object
    
    # Tuple unpacking
    x, y = dimensions # Now x = 1920 and y = 1080

    # Accessing elements (same for list & tuple)
    print(f"First fruit: {fruits[0]}")
    print(f"Width: {dimensions[0]}")

if __name__ == "__main__":
    start()
```

There is a function called `type()` that takes one argumet and this returns the data type of the variable in a string.



I am learning python right now. When I give you a function, keyword, or module. I want you to write an example using it for me, parameters it takes, return values, how it works, and when to use it and why. I just need need these example small and to the point. Here is an example of what I wrote for showing the use of f-string string --> 

```python
def start():
  name = "Alice"
  age = 30
  price = 4.56789
  print(f"My name is {name} and I am {age} years old.") print(f"Next year I will be {age + 1}.")
  print(f"The price is ${price:.2f}")
if __name__ == "__main__":
  start()
```

There is a specific method `append()` that does works on the **list** type. This can take one value and will add that value to the end of the **list**. This also increases the **list** size. Techenically, there are two parameters to this:

1. The first is optional, but this specifies the particulat index to add this into
2. The second is not optional, but this tell what actual value to append

There is a specific method `extend()` that takes a **list** and appends that to the end of the **list** this was called on. The other way this can be done is just by adding them together where the first operand will have the second operand apped to it. This of course returns a copy and not modify the original.

When it if a **list**, is appended to another **list**, then it not add the elements to the other **list**. Instead, it will add the actual **list** as an index. This is a way to make a 2D array.

When it comes to changing values in the indexes, just use the bracket syntax and select the needed index and assigning it a new value. 

Can also use the *slice* notation to change multiple values at once in the list. The *slice* syntax will be used on the **list** that will have its values changes. Then assign this to a list of values.

When it comes to removing an index from the **list**, use the **del** keyword followed by the index of the **list** item that needs to be deleted like `del indexer[0]` will delete the first value index from the **list** and decrease the size by 1.

A method that can be used is `remove()`. This does not take the index, instead this takes takes the value that needs to removed. If this passes then the value will be removed and index will decrease by 1. If it is not there then an error will be raised and needs to be dealt with.

A **list** can use the `pop()` method. This will remove the index, but it will return the value that was removed so it can still be used. This only takes one value and that is an integer. If no value is passed in then it will auto use -1 which will remove the item of the **list**.

There is another method called `clear()` that will just remove all of the elements from the list and make the size 0.

A method called `index()` is used to get the index of where the value lives in the **list**. The only parameter this needs is the value that is being sought. However, there is another way this is done which is more common and that is using the **in** keyword to check if a value exist in collection type. The syntax is `ValueToCheck in CollectionVariable` and this will return *True* or *False*.

A method called `count()` is used to see how many times a certain value appears in the **list**. The parameter for this is the value being searched for and returns an integer of the numebr of times it was found.

The method `sort()` and function `sorted()` are can be used to sort a **list** and check if it is sorted. The first does not need an argument and this just sorts (in place) the collection passed which affects the original, but it does return *None*. The second returns a bool value if it sorted.

> [!NOTE]
>
> The one argument that can be passed to `sort()` is "reverse=True" and this reverse sorts the **list**.

The function `len()` can be used to check the length of the **list** as an integer.

When assigning a **list** variable equal to another variable, these end up sharing the same referece object in memory. This means that changing the index value of one affects both. For example:

```python
def start():
    testing = [1, 2, 3, 4, 5]
    print(testing)
    tmp_case = testing  # Both reference same object in memory
    print(tmp_case)
    tmp_case[0] = "I WAS CHANGED"
    print(testing)


if __name__ == "__main__":
    start()
```

> [!NOTE]
>
> The code above does work. If copied into the editor, the line #6 will show an error. However, that is just the IDE saying the value was originally an int and now being switched to a string so this could be very bad. The python inteperter does not actually care about this and will do the change.

To prevent this double reference to a **list**, it has the method `copy()`, function `list()`, or using the *sliceing* syntax. These are used by:

- `copy()`: This returns a new copy of the **list** this was called on, so another variable can be the same **list** and be separate to there original.
- `list()`: This is just the function to convert something into a **list** type. Just past the original **list** to be copied and it will return a new copy.
- *slicing* syntax: When doing this, it returns a **list** version of this. So can do something like `x = listExample[:]`.

When it comes to copying **list**, the `copy()` only copies the "first layer" of the **list**. For example, if a **list** contained another **list** inside, then the `copy()` will return a new **list** and its values, but the **list** item does not become a new copy and instead still shared the same object reference as the new one. To prevent this from happening, use the function `deepcopy()`. The only parameter `deepcopy()` takes is the **list** item to be coped.

> [!NOTE]
>
> The `deepcopy()` function is actually in the module "copy", so have to do `import copy` at the top of the file and then do `copy.deepcopy(ListVariable)`.

When it comes to compaing **list**, this is just like a comparing a **tuple**. Meaning both have the same rules.

Can also use the **in** keyword for membership just like a **tuple** as well.

There is a function called `zip()`. This is a way to itterate through multiple sequences during the same **for** loop without having to write nested **for** loops. This takes at least one collection data type, but can be more by comma separated. For each collection that needs to be itterated over, there needs to be a data parameter to accept it. For example, if there are two collection types passed in, the **for** loop needs to have two receiving parts before the **in** keyword.

```python
x = [1,2,3,4]
y = [5,6,7,8]

for xHolder, yHolder in zip(x,y);
    print(f"xHolder = {xHolder} and yHolder={yHolder}")
```

> [!WARNING]
>
> The `zip()` will stop going over all the collection types one the shortest one is completed. Meaning the shortest collection is what stops the **for** loop.

There is another version of the `zip()` called `zip_longest()`. This almost has the same rules as the normal version except this goes on for the longest collection size and not the shortest. This if a shorter collection type would have no more data to itterate through, then for that specific type it would get returned *None* for the respected list itterable variable.

> [!NOTE]
>
> The `zip_longest()` is located inside the module "itertools", so that needs to be imported before this can be used. Also, there is a secret parameter called "fillvalue" that can be set equal to something that this is what the value *None* will be replaced with if no value is in the collection type.

> [!TIP]
>
> The `zip()` and `zip_longest()` are able to be used on a string since it is considered an itterable thing.

The `zip()` and `zip_longest()` can be used without being in a **for** loop; that was just a way to itterate over multiple collection types at the same time. Using one of these functions normally will create a whole zip object type that holds each version of these. Wrap the returned value from it in a `list()` and the indexes of the **list** get filled with **tuples** of the same index type. For example:

```python
x = [1,2,3,4]
y = ["Yes", "No", "Maybe", "Should"]

print(list(zip(x,y)) # OUTPUT --> [(1, 'Yes'), (2, 'No'), (3, 'Maybe'), (4, 'Should')]
```

There is something called *list comprehension*. This is a slightly more optomized way to create a list compared to using a **for** loop to do so. Doing this is the same as creating a **for** loop that calls the `append()` method each time and adding the expression value to the **list**. The parts of this are `[ExpressionThing for IndexValueHolder in ListItem]` and each part means:

1. ExpressionThing: this will be the part that modifies, if wanted, the IndexValueHolder value returned from it.
2. IndexValueHolder: this is the variable name that is used to represent the current index value of the **list**.
3. ListItem: this is the actual **list** to iterate over

An even more complex *list comprehension* can be made by using the **if** or **if-else** guard statements to help filer the data. If can have an if statement after the whole **for** loop syntax, so this will only add the item to the **list** if it meets the requirements. When using the **if-else** version then it is the **if** portion first then the **else** part followed by the *list comprehension* part.

```python
a = [x**2 for x in range(5)]
b = [x for x in range(10) if x % 2 == 0]
c = ["even" if x % 2 == 0 else "odd" for x in range(5)]

print(a) # OUTPUT --> [0, 1, 4, 9, 16]
print(b) # OUTPUT --> [0, 2, 4, 6, 8]
print(c) # OUTPUT --> ['even', 'odd', 'even', 'odd', 'even']
```



## Chapter 9: Dictionaries and Sets

### Dictionary

A **dictionary** is similar to a **list**, but the order of items doesn’t matter, and they aren’t selected by an offset such as 0 or 1. Instead, specify a unique key to associate with each value. This key is often a string, but it can be any of Python’s immutable types: **Boolean**, **integer**, **float**, tuple, **string**, custom defined one, and others. **Dictionaries** are mutable, so they can add, delete, and change their key-value elements.

To create a. **dictionary**, use a set of curly braces. To make an empty one just assign to a variable curly braces. To initalize values inside it do `key:value` and comma separated to add more than one. To access the indeces, it now uses the key name instead of the normal index selecting; unless a number is used at the *key*.

Another way to make a **dictionary** is using the `dict()`. This creates the pairs much more differently compared to doing with a normal curly braces. Inside, put `IndexName=IndexValue` and this will automatically make the *key* be a string and the value for it be normal.

```python
x = {"Riley": 20, "Me": 22}
y = dict(Riley=20, Me=22)
print(x) # OUTPUT --> {'Riley': 20, 'Me': 22}
print(y) # OUTPUT --> {'Riley': 20, 'Me': 22}
```

Can also use the `dict()` to convert a two value sequence pair of collection items. For example:

```python
def start():
    lol = [["a", "b"], ["c", "d"], ["e", "f"]]  # A list with nested two pair list aka 2D array
    letters = ["ab", "cd", "ed", "fg"]
    dict(lol)
    print(dict(letters))
    print(lol)  # OUTPUT --> {'a': 'b', 'c': 'd', 'e': 'f'}]

if __name__ == "__main__":
    start()
```

When it comes to adding elements to a **dictionary**, just pretend there is a *key* being accessed and assign it a value. This will auto create an item in the **dictionary**.

```python
x = dict(Name="Test", Age="Test")
print(x) # {'Name': 'Test', 'Age': 'Test'}
x[1] = 40
print(x) # {'Name': 'Test', 'Age': 'Test', 1: 40}
```

A restriction when choosing the *key* name is it has to be hashable. This means the content cannot change at any time.

When it comes to accessing the elements inside this, just use the *key* of the element that should be accessed and this will return the value. However, if trying to access a *key* that does not exist then an exception will occur.

Again, the **in** keyword can be used to check if a *key* (not value) is in the **dictionary** with `KeyName in DictionaryName`.

Another way to get data is using the `get()` method from the **dictionary** class. This takes one required value and a second optional. The first is the *key* being looked for. The second optional one is to specify what backup value should be returned in case the desired value is not found. If the second parameter is not specified then *None* is returned. 

When using the **for** loop, this also can iterate over the **dictionary**. A key thing is this returns the *keys* and not the actual value at that *key* location. The **dictionary** class has a `keys()` method that a specific "dict_keys" which is just an iterable view of the *keys*. However, just convert this with the `list()` and it will make it.

There is a specific method called `values()` and this returns the values instead of the *keys*.

There is one more specific method called `items()` and this returns a **tuple** of the *key* and value in that order. This means the value holder is a **tuple** of size 2.

```python
def start():
    x = {"Yes": 1, "No": 2, "Maybe": 3, "Should": 4}
    print(x.keys())
    print(x.values())
    print(x.items())
    
    for i in x:
        print(i)
    
    for i in x.keys():
        print(i)

    for i in x.values():
        print(i)
    
    for i in x.items():
        print(i)

if __name__ == "__main__":
    start()
```

Can get the total length of the **dictionary** using the `len()` function and pass it in.

It has the method `update()` as this is used to copy all the keys and values from one **dictionary** from one to another. The **dictionary** passed in as the argument will be copied.

Can use a special syntax that will use the bar symbol. This combines the two **dictionaries** together, but if two of the same *keys* exist then the **dictionary** on the right hand side of the bar will win and that value will be replaced. It is important to note this will not replace the original.

Another way to do the combinations is using the *unicorn glitter* syntax. This requires using the curly braces and inside, put in comma separated, the **dictionaries** to be copied over with each one having `**` in front of it. Just like the previous syntax, the right most one will have the highest priority if the *key* already exist in another **dictionary**.

```python
first = {"Yes": 1, "No": 2, "Maybe": 3, "Should": 4}
second = {'No': 'platypus'}

print(first|second) # OUTPUT --> {'Yes': 1, 'No': 'platypus', 'Maybe': 3, 'Should': 4}
print({**first,**second}) # OUTPUT --> {'Yes': 1, 'No': 'platypus', 'Maybe': 3, 'Should': 4}
```

When it comes to removing an item from the **dictionary**, use the **del** key and after put the **dictionary** variables key value using the bracket syntax. Just like a **list**, the `pop()` method can be used and this will not only delete the key value pair, but also return the value of that key. If that *key* does not exist then an error is raised.

To delete all content from the **dictionary** use the `clear()` method.

This also has access to the `copy()` method to copy it over, but it can also use the `deepcopy()` function from the module "copy" to do deep copying.

These can also be compared with == and !=. The biggest difference between comparing on a **list** or **tuple** is the order in which these values are in the **dictionary** does not matter. However, these two operators are the only ones that work.

The **dictionaries** also can have *list comprehension* and it is all the exact same thing as with **lists** except the expression thing `{KeyExpression: ValueExpression for Expression in IterableVariable}`.



### Set

This is a way to have only unique pairs in a collection, so if any duplicates are in it they are removed until one copy is left. This is made the same way as a **dictionary** with curly braces. However, a **set** cannot be empty; if it is then it is converted into a **dictionary**.

Another way a **set** can be made is with the `set()` function. This can also be used to convert one collection type to a **set**.

> [!NOTE]
>
> If the `set()` is used on a **dictionary**, this will not keep the values of each *key*, but will keep the *keys* themself.

Can use the `len()` function to get the length of the **set**

Can use the `add()` method to add a single item in the **set**

Can use the `remove()` method to remove a single item in the **set**

Just like **dictionaries**, can use the bar (|) notation to combine two sets.

A **for** statement can be used just like all the other collection types. Can also use the **in** syntax to check if the desired data is in the **set**.

When it comes to combining **sets**, this is done with a single & symbol. When combining **sets**, there are a few different operations that can be done: union, intersection, difference, complement, subset, proper set, etc. There are a few ways all this can be done:

- union: this is just combining all the items of two different **sets** to make a single set containing all unique values. This can be made by using the bar (|) notation of the two **sets**. Can also just use the method `union()`.
- intersection: this makes a new **set** containing ONLY the element that appeared in both **sets**. This can be made by using the & symbol between two **sets**. Can also just use the method `intersection()`.
- difference: this make a new **set** containing ONLY the elements that were not in one **set** and the order this is written matters. Writing order $A-B$ would read "All elements that are in A but not B". This is made using the - sign. Can also just use the method `difference()`.
- symmetric difference: this makes a **set** where the elements it does not have elements that appeared in both sets and only contains the unique items found in each of the sets. The way to do this is find the <u>difference</u> between the two sets in both ways $A-B$ and $B-A$ then <u>union</u> the two newly made sets. Can also just use the function `symmetric_difference()`.
- subset: this is when all the elements in one **set** are also found in another **set**. This can be found by using the method `issubset()` or doing <=. This takes one argument of another **set** and returns *True* or *False*.
- proper set: this is when a new **set** has all the same values of another **set** AND even more values that the other does not have. Can calculate using the < and >. Return a bool type.
- superset: Can check if something is a superset with the `issuperset()` method which returns *True* or *False*.

> [!NOTE]
>
> The method the **set** is called on will be the A and the **set** that is passed in will be the B for all functions mentioned above.

## Chapter 10: Functions

### Basic Functions

To create a function start with the **def** keyword, followed by the name of the function, parentheses where arguments are made, then by the colon symbol like `def FunctionName():`. If a function is not going to be implemented right away, can use the keyword **pass** and put only that.

To call the function just use the name and parentheses and pass data inside. Make sure that it is called on the proper indentation or else the function will not be considered made or could be out of scope.

> [!TIP]
>
> Just like C, the functions have to be declared BEFORE they can be called as this is not like javascript that hooks all functions to the top.

When it comes to returning a value, just use the **return** keyword. However, unlike C, this does not need to specify a return type and can just return anything if it wants to or not. However, if no specific return value is given, then by default it will return *None*.

When *function parametes* are added, they do not need a data type and will just be the parameter name.

Can just assign a variable equal to the function call to have it get the return value.

```python
def adding(x,y):
  return x + y

x = adding(1,2)
print(x) # OUTPUT --> 3
```

### Keyword and Default Arguments

When it comes to calling a function of or in any way, there is something called *keyword arguments*. Usually when calling a function, the arguments must be passed in the exact same order as written in the function. However, python is different. This gives the ability to put in any order the arguments by doing `(FunctionParameterName = Value)`.

There is another thing called *default values*. This is applied on the actual function parameters itself. Set the paremeter to any value of choosing and when the function is called, if no value is given for that positional parameter then it willl get that value.

```python
def Test(string, number = 4):
  print(f"This is a {string} and number {number}")

# Named paremeter pasted, so string got no value even though it came first in the arguments 
print(Test(number=10))

# Default paremeter test so even though number got no value it still has the value 4
print(Test(string="Yes"))
```

There is a way to take any number of arguments for a function and these will be stored in a **tuple**. This should either be the ONLY argument in the function or should be the last one to take any number of arguments. This is done by putting the * in front of the variable name and the data will be stored in a **tuple**. There is another version of this with two ** instaed of one. Instead of being a **tuple** it is now a **dictionary** and the data passed in like `KeyName=Value`.

### First Class Citizens

Functions are considered first class citizens in python. This means other functions can be passed as parameters to one function and variables can also be assigned to functions like in Golang. To pass in a function as an argument, just use the function name WITHOUT the parentheses as putting them on will call that function. If a function is assigned like a variable, just use the function name and this will assign the function to that so now that variable can be called like a function and it will execute that function code.

```python
def add(x, y):
    print("add function was called")
    return x + y


def FunctionCaller(function, x, y):
    print("FunctionCaller was called")
    return function(x, y)


if __name__ == "__main__":
    x = FunctionCaller(add, 2, 4)
    print(x)
```

### Closures

There is something called *inner functions* and this just gives the ability to create other functions inside other functions. However, there is something special called **closures**. A **closure** is when a function is declared inside another function and returned back as an instance of that function which gives the ability to call a function and have it remember state. This is created by just returning the function name.

````python
def OuterString(stringName):
    def Inner():
        print(f"WOW THIS WAS MADE AND NOW HOLDS {stringName}")

    return Inner


def OuterNumber(x):
    def Inner():
        nonlocal x
        print(x)
        x += 1

    return Inner


if __name__ == "__main__":
    x = OuterString("String here")
    y = OuterNumber(0)
    x()
    y()
    y()
    y()
    print(x)
    print(y)

````

### Lambda Function

There is a way to declare a function that is not created globally like other functions and these are called **lambda functions**. This is a way to create a single use instance of a function to do something small. These should only be used when it is needed temporary. This is also done with the **lambda** keyword. The rules to these are they fan take ANY number of arguments, but can ONLY take one expression line (logic to execute). The syntax is `VariableName = lambda <arguments>: single execution line`. This variable now is a function and can be used to call and complete the small function task. This also does not take a return function as it will automatically return the computed value.

```python
square = lambda x,y: y * x

print(square(5))  # 25
```

### Generators

This is a very special thing in python that allows for memory efficency and cool use cases. This render the data on the fly and do not store the entire complete list of data. An example of this is the `range()` function. This returns a range object that will go through the specified values, but compute each value on the fly rather than store all values like in a list at once. However, one drawback is once that value instance has been used, it can never go back.

*Generators* are useful with functions since they can help functions remember "state". These are not the same as *closures* because these do not finish execution of a function once it is called, instead it return a value, something else does something with that then the function resumes until the cycle is completed. This is done with the **yield** keyword and not the **return** keyword. Once a **yield** is reached, it will return that value, but pause the function so when it is called again it will continue where it left off until the final **yield** is met.

```python
def gen_numbers(n):
    x = 0
    while x < n:
        yield x+1
        x+=1


def start():
    for num in gen_numbers(6):
        print(num, end=" ")
    print("\n")


if __name__ == "__main__":
    start()
```

### Namespace

The scope in which variables are declared and accessable is the same as all other languages. Functions are local scoped, global variables, etc. Trying to access a global variable inside a function for a read is ok. However, trying to access it for a write will just make a local version of that variable. To be able to access a global variable from within a function and be able to change the data, the use of the **global** keyword is used. Within the function do `global GlobalVariableName` and this will make it so python knows it is accessing the global variable and when changing the variable data it chanes the global one.

There are two functions `locals()` and `globals()` that will return a dictionary of all the local (current namespace) and global variables in the program.

There is another keyword called **nonlocal**. This also affects namespace usage, but not for global variables. Instead, this is for functions within other functions. If a nested function needs to access a variable in the outer function namespace, then it need to do `nonlocal VariableName` just like with the global version. This will reference a variable in the nearest enclosing (non-global) scope.

```python
# ------------------------------
# 1) Without global or nonlocal
# ------------------------------

print("1) Without global or nonlocal")

x = 10


def show():
    # Just reading a global variable (allowed)
    print("Inside show():", x)


show()
print("Outside show():", x)


# ------------------------------
# 2) Using global
# ------------------------------

print("\n2) Using global")

y = 10


def change_global():
    global y
    y = 20  # Modifies the module-level variable


change_global()
print("After change_global():", y)


# ------------------------------
# 3) Using nonlocal
# ------------------------------

print("\n3) Using nonlocal")


def outer():
    z = 10

    def inner():
        nonlocal z
        z = 20  # Modifies z from outer()

    inner()
    print("After inner():", z)


outer()
```

### Exceptions

There are certain times when breaking errors can affect the program and need to be handles right away. For example, when trying to access a list index that is non-existent and throws and error of --> IndexError: list index out of range

To deal with these errors, the code has to go in a **try except** block. The **try** portion is made by just putting the word followed by colon and all code inside that scope will run under the **try** portion. After, there needs to be an **except** portion and this portion of code will run ONLY if an error was thrown from any of the code in the **try** block.

The **except** portion, if written in the basic way above, will catch all exceptions and is considered generic exception handling. However, there is a way to catch and handle specific exceptions errors by doing `excpet ExceptionErrorName` or `except ExceptionErrorName as AliasName`. This will make it so that **except** block will go off only if that specified exception is thrown. Because of this, there does not need to be a single **except** block as there can be many of them. However, these are like **if-elif** statements where the exceptions are checked in the ordered declared. When specifying the excpetions, can put a set of parentheses and put multiple comma separated inside so that block will trigger for those group of errors.

There is one more final optional portion of this called **finally**. This will at the end of all the **except** blocks and will execute the code inside regardless of what failed or succedded in any of the blocks. This part should be used to close resources, print final messages, etc.

There is a way to make custom error types. This requires creating a class object and having it inheriting the Exception class. Creating a class and all that will be talked about in the next section, but that will be shown how to do here. To use the custom exception, just put the exception name like before when specifiying a specific error type.

There is a way to throw an error by hand using the **raise** keyword. This will give the ability to call ANY exception object made or premade. Each one can take in an argument to help specify the error message.

There is an **assert** keyword that allows for testing if something is true or false. This helps by ensuring that certain assumptions in the code are true. The syntax is `assert condition, StringMessageIfFalse`. The condition must be something that can be evaulated to true. This can also be written without the string message part as well. If this were to become false, then this will toss an --> AssertionError.

```python
class MyCustomError(Exception):
    pass


my_list = [1, 2, 3]

try:
    print("Accessing index 5 in the list...")
    print(my_list[5])  # This will raise IndexError

    # 3. Assertion example
    x = 10
    assert x > 20, "x should be greater than 20"  # Will raise AssertionError

except IndexError as ie:
    print(f"Caught an IndexError: {ie}")

except (ValueError, TypeError, AssertionError) as e:  # Example of multiple exceptions in one block
    print(f"Caught a ValueError or TypeError: {e}")

except Exception:
    print("Caught a generic exception")

finally:
    print("This finally block runs no matter what!")

try:
    raise MyCustomError("This is a manually raised custom error.")
except MyCustomError as mce:
    print(f"Caught a custom error: {mce}")
except Exception:
    print("Generic exception")

print("Program continues running normally...")
```



> [!TIP]
>
> When it comes to making a generic exception catch, it is conventional to use `except Exception` and not just `except`. This just uses the main Exception object so this still means to catch call exceptions raised.

## Chapter 11: Objects

Since everything in python is an object, there is a way to make custom object data types that can be used. This helps to create user defined variables for different cases. 

### Declaring Class

To make a custom object first put the **class** keyword followed by the name of the object. This traditionally follows pascal casing followed by the colon like `class ObjectName:`.

### Dunder Methods and Normal Methods

There are special methods called **dunder** method. These are special method names that are already "pre-declared" as these help to give special functionality as it defines how the object will work. The **dunder** methods are called:

1. `__init__`: This is used to initialize the object when it is first called
2. `__del__`: This is used to describe what to do before the object is marked for cleanup and destroyed. This can be anything with the data the current object has, prints, etc.
3. `__str__`: This is used to make a custom representation of what string should be output when someone tries to print the object like `print()`.
4. `__call__`: This is kind of a way to make it so the class object itself can be called on without having to declare an instance of the object. So can just do something like `obj()` or if it is declared then can do `DeclatedObjName()`. This will take any number of parameters and **self**. This can be useful to help keep state of the object like how many versions of that object exist.
5. `__add__`: This defines how two objects of the same type are going to be able to add to each other. So doing `ObjOne + Obj2` really means. However, it is important to use the `ininstance()` which is just like `type()` except it returns *True* or *False* if the object is of the specified type. This is useful to make sure that the thing being passed as an argument is actually the desired object or else it can do something else with the passed in value.
6. `__sub__`: This is the same as #5 except this is for subtracting
7. `__mul__`: This is the same as #5 excpet this is for multiplying
8. `__truediv__`: This is the same as #5 excpet this is division using single /
9. `__eq__`: This is the same as #5 excpet this is equal comparisons
10. `__lt__`: This is the same as #5 excpet this is less than comparisons
11. `__gt__`: This is the same as #5 excpet this is for greater than comparisons
12. `__lte__`: This is the same as #5 excpet this is for less than equal comparisons
13. `__gte__`: This is the same as #5 excpet this is for greater than or equal comparisons
14. `__ne__`: This is the same as #5 excpet this is for not equal to comparisons
15. `__len__`: This is what is called when an object is called by the `len()` function. Just return the size of the object by doing --> return self.size
16. `__getitem__`: This is what allows indexing an object with the bracket notation. Always make sure to check that index being accessed exist so test if the index is greater then or equal to 0 and less than the self.size call. The first parmeter of this will be **self** and the second should be something to represent the variable name index as this is going to be what is used to determine the position of what is being accessed. So can now do --> Obj[0]
17. `__setitem__`: This is like #16 except this is for assigning an index position a value
18. `__delitem__`: This is like #16 except this is for when the **del** keyword is called and trying to delete a specific index.
19. `__contains__`: This is kinda like #16 except this won't expect an index and actually is for using the **in** keyword to check for a membership.
20. `__enter__`: When working with *context managers* like the **with** keyword and the object instance is made like normal, then it will call this particular method afterwards and start execition and once done with that then it can continue to be used while in the scope of the **with** scope. This just needs the single **self** keyword. It is important to return the keyword **self** ONLY.
21. `__exit__`: This is what is called once out of the *context manager* scope. In fact, this will be called no matter what happens like raised error for example. This will have four paramaters of **self**, exception type, exception value, and trackback in that order and these can have any name. When returning from this, if returing *True*, then it will suppress the exception and not crash the program, but *False* will pass the exception up the tracestack and up to the next part of code to deal with it.
22. `__repr__`: This is basically like the same as the `__str__` version except by convention this is used as a developer debugging tool. When things like `print()` need to print an object, it does not call this one and instead uses the `__str__` one. This should return a string with the format using a *f-string* and doing --> ObjectName(variable=Value, ...). The way this would be used is calling the `repr()` and passing the object inside. If something is not defined then error is raised.

When first making a custom class object it always need the `__init__` **dunder** method. Each of the **dunder** methods are declared like regular functions excpet the function name must be the **dunder** method desired.

When it comes to declaring normal methods for this, this is the same as declaring a normal function except it is within the scope of the class object.

> [!WARNING]
>
> When making the *content manager* methods `__enter__` and `__exit__`, they both MUST be present or else this will not work at all with them.

There is a special function called `property()` that is applied to functions. This is a special function that can bind a certain class attribute that when used in certain ways it will call defined function that are inside the current class object. This will take at most four arguments and they are:

1. fget: this function will be called when trying to print the variable or basically any read operations
2. fset: this function will be called when trying to assign a new value to that variable
3. fdel: this function will be called once the specific variable (not class object instance) is deleted with the **del** keyword.
4. doc: this is not a function and will be a string. This string should describe 

### Class Variables

Unlike Java, where instance variables are explicitly declared at the class level (often using access modifiers like `private` or `public`) before they are used in methods, Python does not require separate variable declarations.

In a Python class, instance variables are created when they are assigned to `self`, typically inside the `__init__` method. The names of the parameters passed into `__init__` do NOT determine the names of the instance variables. Instead, the instance variables are defined by whatever attributes are assigned to `self`.

> [!NOTE]
>
> Variables can be declared outside the `__init__` method and these will be declared as *class varibles*. This means declaring an instance of the class object is not needed and can do something like `x = ClassObjName.PI` as this will not make the actual class object and just assign it the value of PI. These need to be declared right after declaing the class name and before the `__init__` method.

> [!TIP]
>
> The variable declared outside the `__init__` are called *class variables* and the ones declared inside it are called *instance variables*.

> [!IMPORTANT]
>
> Since python does not have access modifiers like the private in Java, conventions are used. Declaring a variable normally without the underscore, this is considered a public variable accessible to all. If it starts with a single underscore, are considered protected variables meaning they should not be accessed outside the class/subclass. If it starts with double underscore then it is considered a private and to help enforce this the interpreter does something called *name mangling* which makes it SUPER HARD to try to access the variable directly. For example, something like `__name` turns into `_ClassName__name`. This naming property also applied to all functions made inside the class as well

One VERY IMPORTANT thing to note is EVERY method inside the class MUST first have the argument keyword **self** and this is how python knows the current object in the interpreter step. Then to use any data inside the class object itself, it have to use the **self** keyword followed by the variable for that class.

To actually use the obect, just assign it to another variable with the class objects name and call it with parentheses with the needed arguments.

### Single and Multi Inheritance

There is a way to do *inheritance* and instead of just doing `class ClassName:` do `class ClassName(ClassToInherit)`. The class new class object will get all the needed stuff from the other. This is also where the special function `super()` comes in since it is what allows of calling the parents `__init__` method. The `super()` needs to be called inside the new class objects `__init__` method.

When using the actual `super()` inside the `__init__` method, it is called like `super.__init__(ParametersHere)` as it needs to be specified what is being called by `super()`. However, this is just single inheritance.

When it comes to multi *inheritance*, this just means a class inherits more than one class. This can be done by comma separating the classes in the parentheses of the class declaration section. 

> [!NOTE]
>
> When it comes to declaring a method in python, this does NOT support *method overloading* like in Java or C++, but it can be done. The way python does it is when making a class and it inherits another class, just redeclare the name of a function inside it and python will know to use that one. However, if wanting to use the parent version of a methd, use the `super()` keyword followed by a dot then the function to call like normally.

There is a way to check if an object is a subclass of another using the `issubclass()` function with the first parameter being the thing to check and the second being the object to see if it is that.

### Decorators

When it comes to making methods for a class object, there is a way to have functions just be part of a class that can be called without having to create an instance of a class. The first thing to do is replace the **self** keyword with the **cls** keyword. Next, use something called a *decorator* to the function as this is what truly marks that function as a class function instead of method. The *decorator* to use is **@classmethod** and this will be placed right on top of the function defination. The **@classmethod** gives the ability to access class level variables and functions only. For example, can return something like `cls.ClassVariable` from a function.

Another way to declare a function in a class is using the *decorator*  **@staticmethod**. This works almost just the same as the **@classmethod** except this cannot access ANYTHING about the actual class. This would be just a function within that namespace (function lives in that class for organizing). Another important thing is this does not take the **self** or **cls** keyword at all, so it is made as a normal function.

There is a unique set of decorators called **@property**, `@Variablename.setter`, and `@VariableName.deleter`. This is a way to not have to declare something like *getters* and *setters* methods, but still declare some function to do something to add more functionality. This needs the **self** keyword and the first two property types can have extra arguments. Also, for EACH of these, the method name MUST be the same as the attribute variable name. These are something that auto execute when trying to read data, get data, or delete data with the **del** keyword.

> [!TIP]
>
> This helps to be able to make variables private using the _VariableName syntax as this is what should be used most of the time anyways.

There is something called *class doc* and this is a way to document what the class is for, how to use, or anything that needs to be documented for it. This can be seen with an IDE when it detects that class object is being made. It can also be accessed manually by doing  `className.__doc__` without having to declare an instance of the document. To declare this, just put a triple quoted string RIGHT AFTER declaring class name part. This can even be used on function by just declaring it RIGHT after declaring the function and on the next line.

Another important thing to know is *inheritance* vs *composition*. In OOP design patterns, *inheritance* is considered a "is-a" relationship between another class because the new class is a version of that thing it is inheriting. The *composition* does not inherit anything. Instead, it just uses another class inside it as a property so the that class has a other class inside

Each class object created will have access to the **dunder** method `__dict__` that is called on an instance of the object like `Object.__dict__` and this returns a **dictionary** of the *instance variables* in that class. Because this is really just a **dictionary**, this can also be accessed with the bracket notation and add a new custom key-pair value and add a whole new instance variable that is part of the function. Can even do something like `ObjectInstance.x=20` and this will create a new *instance variable* for that class instance. However, this should never be done.

However, there is something else called `__slots__` which replaces classes underline **dictionary** so the `__dict__` no longer exists. The way this works is it preallocates a small chunk of memory that is ONLY enough for the variables that were specified there. This make the object slightly more memory efficient and little faster to access data values. This done by putting `__slots__ = ("DataNamesHere")` which is assigning it a **tuple** and has the normal rules of a **tuple**. This should be placed after the class name and *class doc*, but before the `__init__` method. If something is trying to be added to the instance variables then an error is raised.

> [!NOTE]
>
> If the object being created is going to be inherited by a different object, that other object must use the `__slots__` syntax again or else it will automatically go back to using `__dict__` (which uses a **dictionary** under the hood) which prevents the memory efficiency trying to be achieved.

### `__name__` dunder variable

In Python, `__name__` is a special double-underscore (dunder) attribute that identifies the name of a module, function, or class. For functions and classes, it stores the identifier used at definition time (name of thing), allowing access to their declared names programmatically. In the case of modules, its value depends on how the file is executed: when a Python file is run directly (python3 FileName.py), the interpreter sets `__name__` to `"__main__"` in that file, indicating that the file is acting as the entry point of the program. When the same file is imported into another module, `__name__` is set to the module’s filename (excluding the `.py` extension). This distinction enables the widely used `if __name__ == "__main__":` pattern, which ensures that certain code runs only when the file is executed directly and not when it is imported. Through this mechanism, `__name__` provides both identification metadata and a practical way to control execution flow within Python programs.

When accessing a *class variable*, if the variable does not exist then an error is raised. However, there is a way to get around this using the `getattr()` function. The first argument is the object to check while the second parameter is the name of the variable to check. If it does then returns the value and if it does not then returns *None*. But, this can take an optional third parameter and this is can be the specific variable to be returned if nothing is found.

### Dataclass

This is a special decorator called **@dataclass** that comes from the *dataclasses* module. This is something that is put above the class declaration and it will auto generate an `__init__`,`__eq__`, and `__repr__` methods and it follows correct python conventions. To use this, *type hints* must be used on the variables and they are just declared after the class name and look like `Name: DataType`. This will look like:

```python
from dataclasses import dataclass

@dataclass
class Test():
  	name: str
    age: int
    DOB: str
```

> [!NOTE]
>
> This is just the very bare minimum of this. However, there is [more](https://docs.python.org/3/library/dataclasses.html#class-variables) that can be learned that goes way more advanced.

## Chapter 12: Modules, Packages, and Libraries

When it comes to organizing code, python has three different different terms used:

1. *Module*: This is a single python file
2. *Package*: This is folder that contains many modules
3. *Library*: This is a folder that contains many packages

Another file can get the code from a different file using the **import** keyword followed by the file name without the extension. The syntax is `import ModuleName`. Now to use anything from that file do `ModuleName.ThingToAccess`.

Another way to access code from a *module* is using the **from** keyword along with the **import** keyword to get something specific from that file any nothing else. The syntax is `from ModuleName import SpecificThingName`.

> [!CAUTION]
>
> Can also do `from ModuleName import *` and this will import all the content from it, but without the module namespace thing. This is highly discouraged since this can interfear with other things in the program having the same name.

> [!CAUTION]
>
> When importing modules from a differnt file, all that code is basically copied and pasted into the file importing. Meaning all that code will run in the new file. So any global content inside will run in the new file. That is why, like mentioned in chapter 11, it is important to use the `__name__` dunder method syntax for files.

When importing a module, the name given of the file does not have to be used. This is done by making an alias to it. 















2k@NLxoktB!pT[!T

