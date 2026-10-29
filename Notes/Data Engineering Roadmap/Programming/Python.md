# How To Run Python Programs

## Python Language

### Syntax

Python is a high level programming language that defines the syntax, semantics, and rules used to express computational instructions. However, Python source code cannot be executed directly by a computer's processor. Instead, a Python implementation provides the software infrastructure necessary to translate and execute those instructions.

<u>For Example</u>

```python
print("Hello, World")
x = 0
print(x)
```

### Interpreter

The most widely used implementation, CPython, is written primarily in C. CPython contains a compiler, a bytecode interpreter, an object system, a memory manager, and supporting libraries. Together, these components allow Python programs to execute on a computer.

However, CPython is just one implementation of how this can be written. Other languages like Java (Jython) and C# (IronPython) can also be used to make it.

### Execution

Although CPython is implemented in C, this does not mean that Python programs automatically execute at C like speeds. The compiled C implementation executes native machine instructions, but it must also perform additional work to implement Python's dynamic typing, object model, name resolution, memory management, and other language features.

### Total Process

The total process 