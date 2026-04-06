# Bash Basics

## Basics

### File Setup

The top of each file will have something called a *shebang* line. This is a special line that tells the operating system which interpreter to use to run the script. This will first have a special part like **#!**. Followed by that, with no space, will be the path to the inteperator to use. A popular location for using the *bash* inteperator is at "/bin/bash". For example, for bash the shebang is `#!/bin/bash`. 

The downside of the *shebang* above is that is suggesting that the inteperator is located at that location. In the case that somenes device does not have it in that location then this wil cause an error. The other way to do this is `#!/usr/bin/env <inteperator>`. This checks where that thing is in the users PATH rather than that specific path given.

Once finished with this, the file needs to be granted the execution permission. This can be done using the CLI command **chmod** and run something like `chmod +x <FileName>`. After, run the file executable with `bash ./<FileName>`.

All bash scripts end with the extension ".sh" or ".bash".

To print stuff to the text, use the CLI command **echo** followed by text.

To write commits in bash use the # symbol. All text after it will be a commit. Also, bash does not have a multi-line commit.

> [!NOTE]
>
> A bash file is just a bunch of CLI commands that are written together so the task does not have to be written out each time and it can be automated. If linux commands are known, then writing a bash file is the same thing except all the commands are ran one after the other.

> [!TIP]
>
> The bash file does not techenically need to end with the .sh or .bash extension. This is just to signal to the user what that file type is. The *shebang* is what actually determines what type of script file this is.

```bash
#!/usr/bin/env bash
echo "Hello, World!"
```

### Sourcing VS Executing Scripts

Running the bash script can be done in two different ways. This matters because it determines if the current shell process runs the script or a child process will run the script.

1. When running the script like `./<FileName>` or `bash <FileName>` then it does not run in the current shell process. The current shell process will create a *subshell* called a child shell process. The script is ran in an isolated environment. This means once that script is finished that child subshell process will be destroyed and changes to the system like changing directories or creating variables will be destroyed once gone. For example, if the script changes to the directory ~/Learning/Code/Python/ and list all the file in it, then once the script is over. This method is called *executing*.
1. However, another way to run this is in the current shell environment. This is done by doing `source <FileName>` or `. <FileName>`. So any variables or anything done that changes the environment will affect the actual main shell and retain from the rest of the program. This method is called *sourcing*.

Most of the time this will be ran in *executing* mode as this will keep the current environment clean and prevent overriding current environment variables. Only use the *sourcing* method like modifying the PATH variable, .bashrc, importing list of reusable functions, etc.

There are something called *alias* that can be made. This can be made with the **alias** keyword. To make one do `alias <AliasName>=CommandsToRun`. This should be made if the file would be a short one-liner command. For example, instead of writing a single bash for three different commands then this could be like `alias biggest='du -ah . | sort -rh | head -10'` so this can now just be ran by called `biggest` and this will do all of this.



### CLI Commands Built-in vs External

When it comes to two different command categories:

1. *Built-ins* are programs that are precompiled and built into the bash executable itself. Some examples of these are **cd**, **echo**, **alias**, **export**, and **pwd**.
2. *Externals* are programs that live in a system directory for example like `/usr/bin`, `/usr/local/bin`, and `/bin`. These are programs that do not execute natively. Instead, these commands need to be "forked" into a new process and then ran in that subshell. Before the subprocess is created, the file must be found in the PATH variable listing then a "fork" will be ran and then the command there.

To see a commands category, use the comnand **type** followed by the command name. If it returns  "\<CommnadName\> is a shell builtin" then this falls under the *built-in* category, but if it returns a file path then this is an *external* command. There is a special -a that is available and this will show all possible matches for that command by returning each file path type. For example, `type cd` or `type -a cd`.

There is another special command called **which** that will work on *external* commands only. This will locate which executable fill will be called when that command is ran. This is important because there could be two executables with the same name in different locations and they can both do two different things. This helps to ensure that when that command is ran the correct file is executed. This returns the file path to the *external* command.

When it comes to 

There is another command **help** that will show all *built-in* commands available in bash.

When it comes to performance, using *built-in* commands is better since this requires less overhead. However, if for some reason the system path is broken then the *built-in* commands will not be able to run.

Another command called **man**. This is short for "manual". The syntax for this is `man <Command>`. This will tell what the command does, types of flags and what they do, and more.

## Variables & Arrays

### Variables

To create a variables do `VariableName=Value`. It is important that there is no space between the equal sign, value, and name. If there is then this will 

### Data Types

Unlike C/C++, bash treats most values as strings. For example, 50 and "50" are really both strings. However, there are ways to get a number to work in an arithmetic context.

### Functions



### Loops



### Conditionals



- File Setup 
- Variables
- Data Types
- Functions
- Loops
- Conditionals
- CLI Arguments
- Shell Expansion & Substitution
- Quoting & Escaping
- CLI commands
- I/O
- Processes
- Exit Codes & Error Handling
- Debugging & Testing
- Signal Handling
- Coprocesses
- Subshells vs Current Shell
- Word splitting & $IFS
- Arrays
- "\$@" and \$@
- Environment & Shell Behavior
- Text Processing Power
- Built-in Commands vs External Tools
- Pipes and Command Chaining
- Job Control
- Sourcing vs Executing Scripts
- Traps