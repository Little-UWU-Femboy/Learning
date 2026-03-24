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

### Basic File Outline

It is important to note that java is case sensitive when it comes to naming things.

```java
void main(){
    IO.println("Hello, World");
}
```

> [!IMPORTANT]
>
> The code above is not the common standard prior to java versions 25. This was an in development feature. Normally this would look like:
> ```java
> public class Main{
>     public static void main(){
>         System.out.println("Hello, World");
>     }
> }
> ```
>
> The first list will be the same EXACT name as the class file. The second line will be named the normal main function with other extra properties.



Just like in C/C++, the use of curly brackets is used to define a scope of a function.

In java, "functions" are actually called a *method*.

To have the program actually run, there has to be a method called main in the program. This is like the important main method in something like C/C++.

The IO part of the program is something called a *class*. A class is a container for the program logic that defines the behavior of an application.

In java, everything is considered a class.

When it comes to naming conventions of class files, they use PascalCasing.

### Commets

To leave commets, this is the same as C with // for single line and /**/ for multi-line commets.

Each statement has to end with a semi-colon as this is the only way to mark that the statement is done. This means that multiple parts of a single statement can span multiple lines like the following below:

```java
void main(){
    System. // Single line commit
    out.
    println("This is a test");
    /*
    Multi line
    commet
    */
}
```

There is a special type of commet called a doc commet. This is basically the same as the the multi line commet except, there is an extra * at the top part of the commit like /***/. Will talk about later when talking about automatic documentation generation.

### Data Types

Java has 8 primitive data types and these must be used when declaring a variable.

#### Integers

- **byte** --> holds integers -127 - 126. This takes 1 byte of memory.
- **short** --> holds integers -32,768 - 32,767. This takes 2 bytes of memory.
- **int** --> holds integers –2,147,483,648 - 2,147,483,647. This takes 4 bytes of memory.
- **long** --> holds integers –9,223,372,036,854,775,808 - 9,223,372,036,854,775,807. This takes 8 bytes of memory.

This data types memory sizes are fixed no matter the max CPU bit size. For example, in Golang when giving a variable of type int it can be a 32 or 64 bit number depending on the CPU architecture. However, in java an int will always be 4 bytes no matter what.

When choosing the **long** data type, the number of this should end with the suffix L like `long x = 8000000000L`.

There other smaller data values that can be given like:

- Hexadecimal numbers start with 0x prefix
- Octal numbers start with 0
- Binary numbers start with 0b or 0B

Java allows underscores between numbers to imroving readablility.

Unlike C/C++, java does not have a unsigned version of the integer values.

#### Floating Point

There is only **float** and **double** types here. The first will takes 4 bytes and the second will take 8 bytes. However, their value ranges are not exact and instead an approximation. The first is about 6 - 7 decimal digits while the other is about 15 decimal digits.

It is important that the **float** type ends with the suffix F just like the **long** integer type. If not, then even if this is specified to be of type float it will still come out to be of type double and could throw an error.

All floating point numbers follow the IEEE754 specification. There is a pdf file about this in the Assets folder called IEEE754.pdf

When decimal point number, the result of dividing a positive floating-point number by 0 is positive infinity. Dividing 0.0 by 0 or the square root of a negative number yields NaN.

There is a class called Double that has access to special methods and variables that cover different cases.

- `Double.POSITIVE_INFINITY` --> This is when the value is positive infinity
- `Double.NEGATIVE_INFINITY` --> This is when the value is negative infinity
- `Double.NaN` --> This is when the value in undefined
- `Double.IsNaN(float)` --> This is method is used to check if the variable is of not a number type

#### Char

To represent a single character use the **char** data type. Unlike something like C/C++, the char type here takes 2 bytes instead of 1.

This type is created by using single quotes around the character. The value can be a literal single ANSCII character or something like a unicode character. A hexadecimal number value can be placed inside there so represent a more complex unicode value.

To represent a raw unicode value, prefix the 4 numbers with \u. There are other common escape sequences that are used to represent something else like:

- \n for newline
- \t for tab space
- \\\ for backslash literal
- \\" for double quote literal
- \\' for single quote literal
- \\s for single space
- \u3042 for あ

When a Unicode character falls within the *Basic Multilingual Plane* (U+0000 to U+FFFF), it can be represented using a single 16-bit char in Java.

For characters outside this range (U+10000 to U+10FFFF), Java uses a *surrogate pair*, which consists of two char values stored next to each other in memory. These two char's together represent a single Unicode code point. However, the use of the **String** data type is needed. While this will be talked about later, but fornow a string is just a collection of characeter types.

```java
public class Main {
    public static void main(String[] args) {
        // Unicode for 'あ' is U+3042
        char japaneseChar = '\u3042';
        char japaneseCharLiteral = 'あ';
        char thing = 'x';
        String BIG_THING = "\uD83D\uDE00"; // 

        // Print the character
        System.out.println("The Japanese character raw is: " + japaneseChar);
        System.out.println("The Japanese literal is: " + japaneseChar);
        System.out.println("Regular Character is : " + thing);
    }
}

```

> [!CAUTION]
>
> When using the unicode \u literal, this is processed before even the text or commets in the file are. This mens if something like "\u0022+\u0022" is written this this actually turns into trying to add together 2 empty string like ""+""

#### Boolean

To represent a true or false value, use the **Boolean** data type. This is used to only represent true or false values. The values for true and false in java are literally "true" and "false". Another way these are represented is any non-zero value is considered true and any zero value is considered false.

### Variables

#### Declaring a Variable

Java is a *strongly typed* language. This means each variable has to have the type specified and this type cannot be changed once declared. The rule for declaring a variable is data type followed by name space separated and ending with a semicolon like `int x;` . 

> [!IMPORTANT]
>
> Java versions from 21 and above, there is a special variable called _ that is already predefined. This is used to symbol that a variable that is syntactially required but never used.

When declaring multiple variables of the same data type, they can be name comma separated instead of having to be declared on separate lines like `int x, y, z;`.

#### Giving a Value

Once a variable is declared, it has to be assigned a value before it can be used anywhere. If it does not get a value before being used then an error in the program will occur.

To give a value, just use the = symbol and the value on the left side will get the value on the right hand side of the equal symbol. The two ways to actually assign a value to one is:

1. Do it while declaring the variable like `int x = 50;`
2. Do it after variable is declared like `int x;` then doing `x = 50;`

Java has a keyword called **var**. This can be in palce of the data type and declare the name like normal. This makes it so the data type of the variable can be infered instead of having to specify the data type. This is helpful when declaring object types which will be talked about later.

The only requirement for the **var** keyword is a value must be assigned to the variable once it is being declared.

#### Constant

To declare a variable who's value should never change (like π will always be 3.14), the use of the keyword **final** will be used. This keyword will go before declaring the data type.

If this variable's value is attempting to be changed during run time, then an error will appear.

It is a common practice to have constants be named all upper case and have _ be a separator between the names.

#### Enum

In Java, the **enum** keyword defines a specialized data type used to represent a fixed set of constants. This prevents the use of invalid or "magic" values by restricting a variable to only the names defined within the enum container.

There are two primary ways to implement an enum. The most basic form is a simple list of names, which is ideal for categorizing items like sizes or days of the week. The second form involves using a *constructor* to attach specific data to each name. When this is done, parentheses containing the data follow each constant. To store and retrieve this data, the enum must include a field and a method. While the data types for these values must be consistent across all constants in a single enum, the specific values assigned to them can vary.

Under the hood, Java enums are much more powerful than simple integers. Each enum constant is an instance of a class that inherits from `java.lang.Enum`. This structure allows enums to behave like objects, providing access to built-in methods while maintaining a fixed, restricted set of possible values.

```java
// Case 1: Basic Enum - Used for simple categorization
enum Difficulty {
    EASY, MEDIUM, HARD
}

// Case 2: Enum with Data - Each constant carries an associated value
enum Currency {
    // Each constant passes a symbol to the constructor
    USD("$"), 
    EUR("€"), 
    JPY("¥");

    // Field to store the constructor data
    private String symbol;

    // Constructor - must match the data type passed in the constants
    Currency(String symbol) {
        this.symbol = symbol;
    }

    // Method to retrieve the stored data
    public String getSymbol() {
        return this.symbol;
    }
}

public class Main {
    public static void main(String[] args) {
        // --- Working with Basic Enums ---
        // Declaration and assignment
        Difficulty level = Difficulty.EASY;
        System.out.println("Current Difficulty: " + level);

        // Reassignment
        level = Difficulty.HARD;
        System.out.println("Updated Difficulty: " + level);

        // --- Working with Enums with Data ---
        // Accessing the constant and its internal method
        Currency money = Currency.USD;
        System.out.println("Currency: " + money);
        System.out.println("Symbol: " + money.getSymbol());

        // Direct access without a variable
        System.out.println("The symbol for Yen is: " + Currency.JPY.getSymbol());
    }
}
```

