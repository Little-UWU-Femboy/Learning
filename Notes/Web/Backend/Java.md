# An Introduction To Java



## The Java Programming Environment

All java files will have the .java extension.



When it comes to downloading the java versions, there are different terminology used for this.

| Name                     | Acronym | Description                                                  |
| ------------------------ | ------- | ------------------------------------------------------------ |
| Java Development Kit     | JDK     | The software for programmers who want to write Java programs. |
| Java Runtime Environment | JRE     | The software for running Java programs, without development tools. Only supported until Java 8. This is not wanted. |
| Standard Edition         | SE      | The Java platform for use on desktops and simple server applications. This is wanted. |
| OpenJDK                  | N/A     | A free and open-source implementation of Java SE.            |
| Hotspot                  | N/A     | The “just in time” compiler developed by Oracle.             |
| GraalVM                  | N/A     | An “ahead of time” compiler for executables that start quickly, but don’t support all Java features. |
| Long Term Support        | LTS     | A release that is supported for multiple years, unlike the six-month releases that showcase new features. Choose the latest LTS release |



The way to run a java file it to use the command on the CLI **java** followed by the java file name with the extension like `java Main.java`. There is another version of this called **javac** where this does compile the .java files, but does not compile the code to machine code like in C. Instead, this turns into something called *bytecode*. This creates a new file with the same name, but ends with .class instead. When there is a .class file and wanting to run it, it does not need to have the extension behind it and can just have it without the extension like `java Main`.

> *Bytecode* is just an intermediate step in the compilation process that makes the instructions for the code platform independent. This means that the JVM that actually runs the code can spit out whatever correct instructions for any OS to use correctly.

## Fundamentals of Programming Java

It is important to note that java is case sensitive when it comes to naming things.

```java
void main(){
    IO.println("Hello, World");
}
```

> [!IMPORTANT]
>
> 



Just like in C/C++, the use of curly brackets is used to define a scope of a function.

In java, "functions" are actually called a *method*.

To have the program actually run, there has to be a method called main in the program. This is like the important main method in something like C/C++.

The `IO` part of the program is something called a *class*. A class is a container for the program logic that defines the behavior of an application.

In java, everything is considered a class.

When it comes to naming conventions of class files, they use PascalCasing.

