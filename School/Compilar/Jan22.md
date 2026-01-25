# January 22, 2026

## Compiler vs Inteperter

The **compiler** is a software that translates computer code into an executable version the device understands. The input that a **compiler** gets is called **source** and the output it makes is called **target**. The **source** is the programming language that this needs to translate and the **target** is the output to the specified *instruction set* of the computer so it can execute that.

Not all **compilers** translate code into the *instruction set* code the computer understands and sometimes it turns it into a different high level language; this is called **source to source translation**. An example of this is TypeScript where the code it compiled from TypeScript to JavaScript code.

When describing **compilers**, there are two methods things are done:

1. **Ahead Of Time (AOT)**: This will compile the high level language into the *machine code*. This will create something like the .exe or .out file so the computer can understand ALL the instructions right away
2. **Just In Time (JIT)**: This is will not compile the code down to the *machine code* right away and instead turns in into **bytecode**. Now once executed, this compiles the code at run time rather than have it all done before. To help speed things up, a *hot spot* is when the executioner recognizes a certain part of code (like a function) called over and over so it will compile it and it can be called faster for future references. A good example of the is the *Java JVM* and *Googles V8 engine*.

On the contrast, something called an **inteperter** will not compile the code down and instaead takes the code line by line and execute it. Some examples of this are Python and Ruby.



## Compiler Fundmentals Principles

When it comes to the compiler program, the two fundamental rules are:

1. `The compiler must preserve the meaning of the input program`: This means the compiler has to follow a strict set of rules to get exactly right what the original program intended to do. For example, if a return keyword was forgotton, the compiler should not just assume it needs to add it in as this would be be faithful to the original program.

2. `The compiler must discernibly improve the input program`:

   

   

   # Class Notes Section

   