# IMPORTANT INFORMATION

All this information will all be for ARM32 Linux. This code will not run on am AMD/Intel chip as these are x86_64 based. Also, this will not run on an Apple M1/2/3/4 chip as these are ARM, but can only run ARM64 version. Also, Mac assembly is different than Linux assembly in the sense there are some commands and registers that are ran differently. For example, 

# Assembly Basics: ARM

## Basic Information

Course learning on Youtube from [freeCodeAcademy](https://www.youtube.com/watch?v=gfmRrPjnEw4).
[CPU Simulator](https://cpulator.01xz.net/?sys=arm-de1soc) here.

Unlike normal programming languages were knowing where information is stored in memory is not important, in assembly that is done by the programmer. In this case, it is important to know about something called *registers*. These are special spots were data is actually accessed and stored right away for quick and fast operations. *registers* are closest thing of memory to the CPU also making it the fastest memory in any device. The only downside to these are there can only be a select number of them. This means the data being stored there has to be managed carefully.

When looking inside a register, it will contain eight 0's (depending on the machine). Each of these 0's are a *hexadecimal* number (values 0 - F). Also, each hexadecimal number is 4 bits, so a pair makes 1 byte.

Since this simulator only has 8 hexadecimal values in the register, this means this course will cover a 32 bit system only. In assembly, when working with 32 bits of data, even if in a 64 bit system, this is called a *word*. There are other special naming conventions used when working with different sizes of data and they are:
- byte --> When working with 8 bits only
- half word --> When working with 16 bits only
- word --> When working with 32 bits only
- double word (dword) --> When working with 64 bits only

> [!CAUTION]
> It is important to know that if working on a 16 bit system, then the *word* would be used when working with 16 bits.

Although there are many registers, not all are used for just anything. For example, register 0 - 6 are considered *general purpose*. Register 7 is related to storing system call data like asking the operating system for some resource or even free a resource or like ending a program.

There are some other registers that have special names like **sp**, **pc**, **lr**, **spsr**, and **cpsr**. However, it is important to note that naming conventions for these can differ between architecture. For example, x86_64 might not use **lr** to hold the current return address and could be named something like "pa" for previous address, but both would do the same thing functionally.

- **sp** -->  short for "stack pointer". tyhis ties into another topic called *stack memory*. This special memory that is stored on the actual computer (RAM), but this is slower to access compared to getting data from registers. However, much more data can be stored on RAM compared to register. Now going back to **sp**, this is what holds the data to say where the next available stack memory is in the system.
- **lr** --> short for "link register". This stores the information of the current memory location the program is in before jumping to the function memory location. This is because when a function is called, that data might be stored in a different section of memory that does not continue the sequential flow of instructions in 4 byte format. If this did not happen then there is a chance some instructions would be skipped and the program could mess up.
- **pc** --> short for "program counter". This keeps track of where the next instruction in memory to executed is.
- **cpsr** --> short for "current program status register". This is used to store information about the program. For example when working with positive and negative number, this can tell the CPU that the last result was a negative number or positive number. This is done by having *flags* set. There are many *flag* values that can be set like if the result was zero, there is overflow in the bits, carry operation, etc. This is an ARM exclusive register.
- **spsr** --> This is 

> When it comes to stack memory, this will show a bunch of lines with values broken up into byte sized parts with 4 per row to form a *word* worth of data for a line. Usually, on the left hand most side there is a special extra part and this is used to represent the *address* of the data. Typically, this will show the start of data being covered from that line. For example, line one will have 00000000 and the second line would have 00000010 which means the first line holds bits 0 - 31 and the second line starts holding bits at 32 - 63. If lucky, there will be a unique right hand side of information that will show what the actual data is being held in that spot.
>
> > [!CAUTION]
> >
> > Is is important to note that the way the addresses in being shown here is in hexadecimal for. So 00000010 is actually 16 in decimal number system. There are some other simulators that use decimal version instead for this.
>
> ![image-20260328140432280](C:\Users\Owner\HOME\Learning\Notes\Embedded\assets\image-20260328140432280.png)

## Program Structure

### Basic Layout

In the simulator there two lines added to the program automatically. The first one is `.global _start` and the second is `_start:` in that order. They are used to tell the starting point of the application. Here is what that means:

1. The `.global` is used to signal to the *linker* an *assembler* that this label function can be called by other files. A good comparison is to a private and public function in C++, all functions under the private section will be accessible to other files to use. However, the private section makes those functions only accessible to that file.
2. The `_start:` is called a *label*. This is basically the assembly version of a function. So this will go to that code block and start to execute the code there. Particularly, the name of `_start` is the the `main` equivalent in some other programs.

Anything that starts with a dot in front of the name is called a *assembler directive*. This makes it so a special thing occurs in the program.



When it comes to interacting with the operating system, the result of the operation will be stored in register 7 since this is the special register designated for that. The two ways that a program interacts with the operating system is with *system interrupts* and *system call numbers*.

- *System interrupt* --> this is a special instructions that signals to the operating system that it can take over and needs to do something. The way this works is it reads what is in register 7 and depending on what value it has it knows what to do. The result of the operation is returned to register 0.
- *System call numbers* --> this is when a specific number is given to register 7 that tells the system specifically what to do like the read, write, open, exit, etc operations.

> For example, if register 7  was given the number 4, then when the OS checks this it signals that a write operation needs to be done. Another number is 1 which signals that the program is ready to end.

### Opcodes

When it comes to actually giving instructions on what to do, this is done with *opcodes*. These are like the keywords of programming languages that signal what the program needs to do. The opcode is then followed by *operands* which are like arguments that it needs to do the operation. The format they follow is typically `opcode <operands>`. Particularly, the operand section follows `<destination>, <source 1>, <source 2>`, `<destination>, <source>`, etc.

> [!CAUTION]
>
> Different systems and architectures might not follow the same syntax when writing operands. It is important to check each architectures syntax before coding in it.

The first *opcode* is **MOV**. This used to put specified data into a memory area of choice. The syntax for this is `MOV destination, source` where the destination will be where to store the data and the source will be the actual data to store.

When it comes to referring to registers, the way this is `R#` where # is an actual number for the register like R4 or R5.

When it comes to using actual numbers, unlike normal programming languages, normal numbers do not work. Instead, they have to be prefixed with #. For example, #4 is the same as 4 in C. Also, hexadecimal values can be put into the registers by following the syntax except also put 0x right after the # and write the two parts of data like 0x01.

> For example, `MOV R0,#4` will put the constant value 4 into register R0.

Another opcode is **SWI** which stands for software interrupt. This is how to trigger an interrupt so the operating system can take over and perform the specified system call based on the number in register 7. Typically, this is just followed by the number 0 without the #. That is some ARM devices just ignore the number anyways. However, for some ARM systems that can be used to signal different things. For here, will just use 0 to signal for the operating system to take over.

### Commit

When writing these commands, each statement does not end with anything like a semi-colon. This is because a semi-colon is actually used to write commits. So anything that comes after then is considered a commit.











When it comes to compiling code, this is typically done in stages like:

1. Preprocessing --> This takes all the things like import, #include, etc and adds them to the file.
2. Compilation --> This note takes that source code and does *syntax analysis* when it checks for syntax and sematic correctness. After, it also tries to make code optimizations for better performance, but in assembly. Once this part is done then it makes an assembly file (.asm or .s).
3. Assembler --> This takes all the assembly files and converts them into a new machine code file (.o) that the CPU can execute. However, this is not fully done yet as the file might still have some unresolved references to functions or variables. 
4. Linker --> This takes all the object file (.o) and combines them together to make an executable that is actually able to be ran. This will resolve all the missing references that the files might have.

> Not all programming languages follow these steps above. It is mostly C/C++/Go/Rust that follow this since they compile down directly into machine code the CPU can run. However, languages that use thing like virtual machines or are intenerated do not follow this convention.

# Assembler Directives

- `.global` --> This is used to make functions public to other assembly files. The syntax is `.global <label name>, <label name>`.
- `.include` --> This is used to include code from other assembly files to then be able to call functions from them with syntax `.include "file names", "names"`.
- `.extern` --> This signals that an external function does exist, but not in the current file. However, this will only work if the label exist somewhere in another file AND that file is already compiled to an object (.o) file. Otherwise an error will be thrown about not being able to find the reference.
