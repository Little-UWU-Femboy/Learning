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

To create a variables do `VariableName=Value`. It is important that there is no space between the equal sign, value, and name. This same style is used when assigning values to variables again as well.

When it comes to actually refercing the variable later, the $ must be put in front of the name like `$VariableName`.

<u>For Example</u>

```bash
x=50 # This creates a variable
y=$x # Creates a variable y and gets the values from x. Must use the $ since it is being referenced
x=100 # Do not need to use the $ on the x since this is not being referenced to be use else where

echo $x # Needs to use the $ again because this is being referenced to get its value.
```

### Data Types

Unlike C/C++, bash treats most values as strings. For example, 50 and "50" are really both strings. However, there are ways to get a number to work in an arithmetic context.

While bash likes to treat all variables values as strings, there is a way to specifically declare that something is a variable or should be read only (aka constant). Use the **declare** keyword to do this. Followed by that keyword will be a flag like argument then followed by the variable mame. The syntax for this is `declare [options] <VariableName>=value`. Here are some of the options here:

- -i --> this will declare that the value will be a number of type integer
- -r --> this will declare that the variable will be read only (aka constant)
- -a --> this will declare that this variable is an array
- -A --> this will declare that this variable is an associative array
- -x --> this will declare that the variable is to be exported. This means that child processes will have access to this. Like creating a global variable.
- -l --> this will make the string value lowercase
- -u --> this will make the string value uppercase
- -f --> this will tell if a function exist or not. This must have the same name as the function itself. Also, this is not actually a variable, but just a way to check if a funcion does exist. This returns what the function actually looks like, but does not execute the code. However, this output can be stored in a variable by wrapping the whole thing in `$()`. For example `x=$(declare -f FunctionName)`.

### Global Variable/Function

Bash has the typical local variables and global variables. However, there is an extra scope of variables that are allowed. This is when child processes are created from the current process. If it needs to use a variable that was declared in the parent process this would fail since it would not have access to it. To fix this, there is a keyword `export` that will give the ability to have that variable be seen by child processes. Place the keyword in front of the variable name.

This same thing applies to functions as well. The same steps are takes for functions to make the function available to the child process as well. The only difference is the -f option must be added to this like if using the **declare** keyword.

### Array

#### Creating array

To declare an array, set this equal to parentheses and put values inside it like normal. However, unlike other languages to add more than one value it is space separated and not comma separated. For example `arr=(1 2 3)` or `arr=(1)`.

Just like python list, these can have any data of any type. For example, `arr=(4 "yes" 9 "")`.

#### Accessing Indexes

To access a value from the array, the syntax is `${ArrayName[Index]}` where the index is zero based meaning starts at 0 and ends at $\text{Max Length}-1$. There is a special way to access all the elements at once by putting the @ symbol inside the brackets. This @ symbol will make this return all the values from inside the array at once. For example:

```bash
arr=(4 "yes" 9 "")
echo ${arr[@]}
```

#### Adding Indexes

To add a value to the the array it can be appended or added at a specific index.

- To append a value just do the shorthand syntax += followed by () and the values inside it as there can be one or more values.
- To add to a specific index just use the bracket syntax and select the index (current size does not matter) to put this in then just assign this a value.

Since a value can be added to any index at any point, this means doing something like `arr[10]=50` when there is only 2 indexes currently in the array will not create empty indexes that are missing. Instead, this will make it so only the indexes 0,1, and 10 exist.

#### Removing Indexes

To remove a value from the array there is a keyword **unset** that must be used. This will be placed before the variable name and using the bracket notation on it. For example `unset arr[1]` will remove the index 1 from the array. However, the array will not be reindexed; which means if the array has indexes 0,1, and 2 and 1 is removed then the indexes 0 and 2 exist as this will not be remade to 0 and 1 indexes.

> [!NOTE]
>
> To fix the messed up indexing issue, reassign the value of the array to the same thing using the @ symbol syntax for the index. For example `arr=(${arr[@]})` will reassign an array to the same variable again and then the indexes will be fixed.

#### Unique Syntax

To get the total size of the array using the syntax `${#ArrayName[@]}`, but this will not say the values inside or the index they are at. Can also specify a specific index and will return the total size of that index (in characters even if a number).

To get all the indexes that values exist at, not the values themselves, use the syntax `${!ArrayName[@]}`.

To get all the values, but not the indexes they exist at or total number of index values, use the syntax `${ArrayName[@]}`.

> [!TIP]
>
> It is important to wrap the array when being accessed with $, no matter how, with double quotes. This is just to help prevent breaking logic changes to the content. For example, if there is a string "Hello World" that exist in the array and wanting to loop throgh the array will treat this as two separate values ("Hello" and "World") if done without quotes, but with them will treat it as "Hello World".

#### Associative Array

These are like dictionaries in python. Unlike a normal array, to first declare this the use of the **declare** keyword must be used with the specific -A flag. To give it values when being created the syntax is `declare -A AssocArr=([Key]=Value)`.

When it comes to all the rules of making, using, add, removing, etc stuff from the associative array this is the same thing as a normal array. Only difference is [] will contain a key of the specified value.



#### Storing CLI output

Arrays are a good place to store CLI command output in. For exampe, doing `arr="$(ls)"` will store the output of command "ls" inside this array.

### Quoting, Escaping, & Word Splitting

When deciding which quote types to use there are two different versions:

- Using single quotes around stuff when it should be treated as that literal string. For example `echo '$x'` will literally print "$x" and not the value inside x.
- Using double quotes when expansion and escaping is wanted. For example `echo "$x\n"` will print the value of x and add a newline. If done with single quotes then this would print "$x\n" literally.
- There is a special syntax called *escaping*, just like in C/C++, where things like \n, \\\, \\" , etc are used for special meaning.

There is a special predefined variable **$IFS** which stands for internal field separator. What this does is determines how text is split (or parsed) into words. This will split when space, tab, or newlines occur. The cases this is automatically used is:

- Text spliting --> like having a string value that contains a sentence
- Getting input --> getting input from the user like entering in CLI arguments or typing in arguements the program ask for.
- Parsing lines --> something like a CSV file will have the newline character at the end of each row to indicate it is over

This value can be changed and this will affect when text content is parsed in the entire program. To reassign this something just put the thing inside double quotes. For example `IFS=",:"` will split strings when encountering a comma or colon symbol. This can be useful when wanting to read a csv file row by row and not have to do any manual split of strings.

When changing the value of this globally, this can be dangerous since this might affect more than actually intended or forgetting to switch back to the old version once done with the new version. To use this safely do:

1. Redeclare this inside a local scope, like a function, so when done this will reset the variable to its default values
2. Assign the content of the variable to a temporary value, then change it in a global scope. This will make it so it can be used for any amount of time and when needing to go back to normal then it can be reassigned the value in the temporary value
3. Putting it right before the specific command **read** like `ISP=, read ...`. This must at least have the comma separator or else this will break how input is read. It can be blank by just setting this equal to nothing, but that would be a bad idea. This is just used to have that variable be set to that value temporary for that read operation only and that is it.
4. Creating a subshell and running this inside there. This can be made by executing another script to create it or this can be made with the parentheses special syntax. More about this is mentioned in a later section. [^subshell]



<u>For Example</u>

```bash
var="One Two Three" # String that has speace separeted values inside it
arr=($var) # this creates an array with 3 indexes with a separate one for each part

echo ${arr[@]} # will print One Two Three
echo ${#arr[@]} # will print 3 since there are that many indexes
```

### Shell Expansion & Substitution



### Functions



### Loops



### Conditionals

- [x] File Setup 
- [x] Variables
- [x] Data Types
- [ ] Functions
- [ ] Loops
- [ ] Conditionals
- [ ] CLI Arguments
- [x] Shell Expansion & Substitution
- [x] Quoting & Escaping
- [ ] CLI commands
- [ ] I/O
- [ ] Processes
- [ ] Exit Codes & Error Handling
- [ ] Debugging & Testing
- [ ] Signal Handling
- [ ] Coprocesses
- [ ] Subshells vs Current Shell
- [x] Word splitting & $IFS
- [ ] Arrays
- [ ] "\$@" and $@
- [ ] Environment & Shell Behavior
- [ ] Text Processing Power
- [x] Built-in Commands vs External Tools
- [ ] Pipes and Command Chaining
- [ ] Job Control
- [ ] Sourcing vs Executing Scripts
- [ ] Traps





# TODO

[^subshell]: talk about special syntax about subshell with parenthesis and about the subshell in general.



