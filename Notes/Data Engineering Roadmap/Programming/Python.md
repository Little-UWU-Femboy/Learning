# How Python Works

## Making a file

All files will end with the extension `.py`. However, this rule only applies to "imported" python files. A source code file (one being ran) does not need to have that extension and in fact can have any extension or none!

However, it is convention to have all files end with the `.py` extension

## Different meaning of python

There are two different ways to talk about python:

1. Python in terms of the syntax. This is what defines the rules on how to write python.
2. *Python interpreter* is the software that actually understands and runs the python code. Since this is just the software that runs the program, there are different version of this that can be made. For example, the most popular version of python is called CPython (written in C). There is also another version called Jython (written in Java).

## How running works

When a file is first ran, it take the source code of the file and converts it into *bytecode*. This is used to speed up execution. The *bytecode* files will SOMETIMES be created and end with the extension `.pyc` and be located in a folder called `__pycache__`.

These *bytecode* files:

1. The python program itself has write access to the machine.
2. The there is more than one file needed in the operation (aka file importing).

The *bytecode* files will also ONLY be made for non-top level files like file imports or 

> *bytecode* is just a platform independent version of the code that any machine can run using an intermediate form of that code

## Python Executables

While python code is never really compiled all the way down to binary machine code, there is still a way to create an executable in python. In python this is typically called a *frozen binary*.

This works by bundling the PVM (python virtual machine), *bytecode* of source files, and any python support files and libraries needed. However, this does not increase the speed of the program and still runs at the same speed as if it was just ran normally.