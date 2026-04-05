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

1. When running the script like ./ then it does not run in the current shell process. The current shell process will create a *subshell* called a child shell process. The script is ran in an issolated environment. This means once that script is finished that child subshell process will be destroyed and changes to the system like changing directories or creating variables will be destoyed once gone. For example, if the script changes to the directory ~/Learning/Code/Python/ and list all the file in it, then once the script is over 

### Variables



### Data Types



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