# C++ Basics

## Introduction to C++ Programming

### Basic Layout

#### Sample thing

The basic structure of a program, just like C, contains a main function that is the starting point for the program. The function is set up the same way as in C. However, when it comes to including standard library header files, here they do not need the .h extension.

The library for standard I/O here is called \<<u>iostream</u>\>. This header file will be included the same way as in C with the **#include** which is a *preprocessor directive*.

To print text to the terminal, use `std::cout`. Unlike C, this does not have the text go inside a function and uses << instead. The << is like saying to send the text to output. Multiple << can be tacked on to this. The `std::endl` is just a way to put an end of line character or can do \n in the string. However, C++ way is to use the `std::endl`.

Each statement must end with a semi-colon.

```c++
#include <iostream>
int main(){
  std::cout << "Hello World" << std::endl;

  return 0;
}
```
