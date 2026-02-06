# Python Introduction

## Python Basics

### Basic File Setup & Base Knowledge

When it comes to seting up a python file, there is no special setup that needs to be done unlike other languages like C, Rust, Java, etc.

Python is considered a scripting language and does not actually be compiled. This also allows it to be a dynamic progamming language.

Another thing about python is it does not need an ending semi-colon like Golang, except unlike Golang where it addes the semi-colons when being compiled, python does not do this at run time

To print stuff to the screen, python uses `print(Data Here)`. It is like Java where the data just needs to be place inside it and it will print that out.

To create and run a python file, create the file with the _.py_ extension and then do `python3 FileName.py` to run it.

Since python is a dynamic language, it creates an object in the heap of that data type and on the stack it has the variable name that points to the memory address of that on the heap creating a reference to that object; which the object itself keeps track of the number of references. However, this does not keep track of what references it.

Python is also a garbage collected language so it deals with memory itself. The way that memory is cleared is once an object has no more references to it, it is then able to be marked to be cleared out by the GC.

There is one major different thing in python compared to other languages, it does not use curly braces. Instead, it relies on indentation to represent something is part of a function, loop, if statement, etc. It also used a colon at the marker to where something like function, loop, if statement, etc starts

```python
print("Hello, World!")

# --> OUTPUT <--
# Hello, World!
```

### Variable

To make a variable, just do `VariableName = value`. Since python is a dynamic programming language, it can be assigned a value of any time at any time. However, python does allow a way to see what current data type a variable is by using something called _type hints_; which work by putting `VariableName: dataType = value`. This specified type will not be enforced at run time, but will give an error to note that the rule was not followed.

To check a variable at run time use the `type(Variable)` or `isinstance(Variable, DataType)` function. The `type()` will just return the data type of the variable. The `isinstance()` will return true or false if the variable is the specified type wanted.

The data types are:

- int -- > part of numeric class
- str --> part of string class
- float -- > part of numeric class
- bool --> part of boolean class --> *true* and *false*
- list --> part of list class
- tuple --> part of tuple class
- range --> part of range class
- dict --> part of dict class
- set & frozenset --> part of set/frozenset class
- *None* --> used to check if value is "nothing"



Python does not have a way to declare constants, so it uses the normal syntax (All capped variable name) to denote a variable is constant.



### if statement

To do an if statement do:

```python
if condition(s):
    code here
```

```python
if condition:
    code here
elif condition:
    code here
else:
    code here
```

> [!TIP]
> In the if statements above, it shows how to use the indentation rules mentioned in <u>Basic File Setup & Base Knowledge</u>.

### comparison types

Unlike other languages, python has an easier way to do comparisons and some that are the same. It uses the same `==` sign to see if two variables are equal and `!=` to see if it is not equal like in C or Java. It also uses the traditional `<=`, `<`, `>`, and `>=` like in C or Java.

It starts to differ with the keyword `is` which checks if two variables are the same object in memory. Another comparision is `not`. This is the same as ! in C and Java.

```python
x = 40
y = x
z = 40

if x is y:
 print("x and y are the same")
else:
 print("x and y are not the same")

if x is z:
 print("x and z are the same")
else:
 print("x and z are not the same")

# OUTPUT
# x and y are the same
# x and z are not the same
```

A special features in python is **chained comparisons**. This allows for doing things like `x < y <= 5` for the actual comparison. The C equivalent of this `(x < y && y <= x)`.

When comparing boolean values, this is like C where under the hood the *true* and *false* value is really 1 and 0.

There is another special comparison called `in`. This checks if a variable is inside a collection of data like an array. This will be mentioned more later on the collection types.



### For & While Loop

To make the basic for loop it is like in C



### Learing Path



- Variables
- If statements
- Loops
- functions
- IO operations
- Classes
- dunder methods
- list
- tuples
- dictionary
- sets
- Exceptions
- advanced strings
- keyword arguments
- operators
- Modules
- context managers
- Iterators & generators
- Concurrency
- Functional tools
- NumPy
- Pandas
- MatPlotLib
- Core modules & packages
- memory mangement
- How python works under hood



