# Bash Basics

## File Setup & Shell Behavior

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

## Sourcing VS Executing Scripts

Running the bash script can be done in two different ways. This matters because it determines if the current shell process runs the script or a child process will run the script.

1. When running the script like `./<FileName>` or `bash <FileName>` then it does not run in the current shell process. The current shell process will create a *subshell* called a child shell process. The script is ran in an isolated environment. This means once that script is finished that child subshell process will be destroyed and changes to the system like changing directories or creating variables will be destroyed once gone. For example, if the script changes to the directory ~/Learning/Code/Python/ and list all the file in it, then once the script is over. This method is called *executing*.
1. However, another way to run this is in the current shell environment. This is done by doing `source <FileName>` or `. <FileName>`. So any variables or anything done that changes the environment will affect the actual main shell and retain from the rest of the program. This method is called *sourcing*.

Most of the time this will be ran in *executing* mode as this will keep the current environment clean and prevent overriding current environment variables. Only use the *sourcing* method like modifying the PATH variable, .bashrc, importing list of reusable functions, etc.

There are something called *alias* that can be made. This can be made with the **alias** keyword. To make one do `alias <AliasName>=CommandsToRun`. This should be made if the file would be a short one-liner command. For example, instead of writing a single bash for three different commands then this could be like `alias biggest='du -ah . | sort -rh | head -10'` so this can now just be ran by called `biggest` and this will do all of this.



## CLI Commands Built-in vs External

When it comes to two different command categories:

1. *Built-ins* are programs that are precompiled and built into the bash executable itself. Some examples of these are **cd**, **echo**, **alias**, **export**, and **pwd**.
2. *Externals* are programs that live in a system directory for example like `/usr/bin`, `/usr/local/bin`, and `/bin`. These are programs that do not execute natively. Instead, these commands need to be "forked" into a new process and then ran in that subshell. Before the subprocess is created, the file must be found in the PATH variable listing then a "fork" will be ran and then the command there.

To see a commands category, use the comnand **type** followed by the command name. If it returns  "\<CommnadName\> is a shell builtin" then this falls under the *built-in* category, but if it returns a file path then this is an *external* command. There is a special -a that is available and this will show all possible matches for that command by returning each file path type. For example, `type cd` or `type -a cd`.

There is another special command called **which** that will work on *external* commands only. This will locate which executable fill will be called when that command is ran. This is important because there could be two executables with the same name in different locations and they can both do two different things. This helps to ensure that when that command is ran the correct file is executed. This returns the file path to the *external* command.

When it comes to 

There is another command **help** that will show all *built-in* commands available in bash.

When it comes to performance, using *built-in* commands is better since this requires less overhead. However, if for some reason the system path is broken then the *built-in* commands will not be able to run.

Another command called **man**. This is short for "manual". The syntax for this is `man <Command>`. This will tell what the command does, types of flags and what they do, and more.

# Data Types, Variables, Arrays

## Variables

To create a variables do `VariableName=Value`. It is important that there is no space between the equal sign, value, and name. This same style is used when assigning values to variables again as well.

When it comes to actually refercing the variable later, the $ must be put in front of the name like `$VariableName`.

<u>For Example</u>

```bash
x=50 # This creates a variable
y=$x # Creates a variable y and gets the values from x. Must use the $ since it is being referenced
x=100 # Do not need to use the $ on the x since this is not being referenced to be use else where

echo $x # Needs to use the $ again because this is being referenced to get its value.
```

## Data Types

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

### Incrementing

If something is assigned a numeric value, incrementing by one or decreasing by one is supported. However, the variable name has to be wrapped in two sets of parentheses. Inside the parentheses just put the name of the variable, without $, followed by ++ or --. This can also support pre-increment as well. For example:

```bash
x=1
((x++)) # increment x by 1, so it now holds the value of 2
echo $x
```



## Global Variable/Function

Bash has the typical local variables and global variables. However, there is an extra scope of variables that are allowed. This is when child processes are created from the current process. If it needs to use a variable that was declared in the parent process this would fail since it would not have access to it. To fix this, there is a keyword `export` that will give the ability to have that variable be seen by child processes. Place the keyword in front of the variable name.

This same thing applies to functions as well. The same steps are takes for functions to make the function available to the child process as well. The only difference is the -f option must be added to this like if using the **declare** keyword.

## Array

### Creating array

To declare an array, set this equal to parentheses and put values inside it like normal. However, unlike other languages to add more than one value it is space separated and not comma separated. For example `arr=(1 2 3)` or `arr=(1)`.

Just like python list, these can have any data of any type. For example, `arr=(4 "yes" 9 "")`.

### Accessing Indexes

To access a value from the array, the syntax is `${ArrayName[Index]}` where the index is zero based meaning starts at 0 and ends at $\text{Max Length}-1$. There is a special way to access all the elements at once by putting the @ symbol inside the brackets. This @ symbol will make this return all the values from inside the array at once. For example:

```bash
arr=(4 "yes" 9 "")
echo ${arr[@]}
```

### Adding Indexes

To add a value to the the array it can be appended or added at a specific index.

- To append a value just do the shorthand syntax += followed by () and the values inside it as there can be one or more values.
- To add to a specific index just use the bracket syntax and select the index (current size does not matter) to put this in then just assign this a value.

Since a value can be added to any index at any point, this means doing something like `arr[10]=50` when there is only 2 indexes currently in the array will not create empty indexes that are missing. Instead, this will make it so only the indexes 0,1, and 10 exist.

### Removing Indexes

To remove a value from the array there is a keyword **unset** that must be used. This will be placed before the variable name and using the bracket notation on it. For example `unset arr[1]` will remove the index 1 from the array. However, the array will not be reindexed; which means if the array has indexes 0,1, and 2 and 1 is removed then the indexes 0 and 2 exist as this will not be remade to 0 and 1 indexes.

> [!NOTE]
>
> To fix the messed up indexing issue, reassign the value of the array to the same thing using the @ symbol syntax for the index. For example `arr=(${arr[@]})` will reassign an array to the same variable again and then the indexes will be fixed.

### Unique Syntax

To get the total size of the array using the syntax `${#ArrayName[@]}`, but this will not say the values inside or the index they are at. Can also specify a specific index and will return the total size of that index (in characters even if a number).

To get all the indexes that values exist at, not the values themselves, use the syntax `${!ArrayName[@]}`.

To get all the values, but not the indexes they exist at or total number of index values, use the syntax `${ArrayName[@]}`.

> [!TIP]
>
> It is important to wrap the array when being accessed with $, no matter how, with double quotes. This is just to help prevent breaking logic changes to the content. For example, if there is a string "Hello World" that exist in the array and wanting to loop throgh the array will treat this as two separate values ("Hello" and "World") if done without quotes, but with them will treat it as "Hello World".

### Associative Array

These are like dictionaries in python. Unlike a normal array, to first declare this the use of the **declare** keyword must be used with the specific -A flag. To give it values when being created the syntax is `declare -A AssocArr=([Key]=Value)`.

When it comes to all the rules of making, using, add, removing, etc stuff from the associative array this is the same thing as a normal array. Only difference is [] will contain a key of the specified value.



### Storing CLI output

Arrays are a good place to store CLI command output in. For exampe, doing `arr="$(ls)"` will store the output of command "ls" inside this array.

## Quoting, Escaping, & Word Splitting

When deciding which quote types to use there are two different versions:

- Using single quotes around stuff when it should be treated as that literal string. For example `echo '$x'` will literally print "$x" and not the value inside x.
- Using double quotes when expansion and escaping is wanted. For example `echo "$x\n"` will print the value of x and add a newline. If done with single quotes then this would print "$x\n" literally.
- There is a special syntax called *escaping*, just like in C/C++, where things like \n, \\\, \\" , etc are used for special meaning.

There is a special predefined variable **$IFS** which stands for internal field separator. What this does is determines how text is split (or parsed) into words. This will split when space, tab, or newlines occur. The cases this is automatically used is:

- Text spliting --> like having a string value that contains a sentence
- Getting input --> getting input from the user like entering in CLI arguments or typing in arguments the program ask for.
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

## Shell Expansion & Substitution

### Shell Expansion

When writing commands, there are ways to write short hand versions of them to avoid repeation when writing code out. This acts like a pre-processing stage by first evaulating the short hand and replacing the desired result replaced with it. There are a few times this has already been done when doing the `${VariableName}` syntax. This does not keep that actual variable name there, instead it replaces that with the value assigned to that variable. Another example of this is using the tilde (~) symbol. Instead of staying as that, it is secretly converted to the absolute path to the home directory of  the current user on the system.

### Brace Expansion

This is a special way to write shorter code, but mean the same thing if was most explicit. This is useful for pattern matching things to get results. For example, doing `ls *.java` will mean list only all files that end with ".java" instead of having to write out every java file name. Another example is `touch file{1..100}.txt` will make 100 txt files all with the names "file#.txt" where # is the number 1 to 100. Another example is `echo ${A,B}1.txt` will print to the screen "A1.txt" and "B1.txt".

### Command Substitution

There are times when the output of a command is needed. To do this, use the $ like normal except after put a set of parentheses and put the command to run inside it. For example, `$(ls)` will run that command and then return the output to that spot to replace it just like replacing a variable.

### Arithmetic Expansion

There is a special way to do math unlike normal languages. For example, something in python like $3+5$ will work fine and return 8, but doing that in bash will not result in 8 but the actual string "3+5". If spaces were put between the values this would be even worse since it would cause an error. To do math use the $ like normal, except now have to put two sets of parentheses in each other like `$((Math Here))`. The result will be returned back as a string. For example `x=$((3 + 5))` returns 8, but doing `x=3 + 5` does not return a string and just breaks the program.

### Globing

This is more where the syntax like `ls *.java` comes in. This will make it so it reads all java files. Using something like this is called <u>regex pattern matching</u>. Regex are special symbols that have special meanings to help make commands more dynamic. For example, can list only files that start with "Hello" and end with a ".txt" extension, but the file name, after the word hello, can have any name after just as long as the file name starts with hello which would look like `^Hello.*\.txt$`.

Visit [here](https://www.rexegg.com/regex-quickstart.php) to see what spcial symbols are available to use to get more advanced globbing.

> [!NOTE]
>
> On Mac, it uses bash version 3.2.57, but the downside to this is there are a lot of new bash features this does not have. However, Mac now use tells users to use a shell called "zsh". This is very similar to bash, but there are a few differences. One difference is arrays do not start at index 0. Instead they start at index 1.
>
> There is a way to use the most up to date bash on Mac, but it has to be installed with homebrew. The command is `brew install bash`. If this is done, insted of using `#!bin/bash` for the shebang line use `#!/opt/homebrew/bin/bash`.



## If, For, and While Blocks

#### Conditional

There are times when certain could shoul execute based on if a certain condition was met. Bash using something called <u>exit codes</u> to determine if the result of something was successful or not. When a command is successful, it returns a code of 0, but values 1 - 255 are used to indicate errors of different types.

An <u>exit code</u> value will be generated each time a command or expression is evaluated and completed. For example, running `ls` should (about %99.9 of the time) return a code of 0. Doing something like `echo $(3 + 5))` returns an exit code 127 on Mac to signal there are too many braces. 

The exist code value can be seen by running a special command `$?`. This will return the specific exist code and the message for that code.

Now, when it comes to executing code based on a specific <u>exit code</u>, this can be done with an if statement. To make an if statement is much different compared to normal languages. The syntax is:

```bash
if [ condition ]; then
	# Code Here
fi
```

Inside the conditional, it can also use the && (AND) and ||(OR) for the logical conditions, but there are more than one set of [] separated by the logical symbol like `if [] && []`.

However, there is another way this can be made and instead of having just one set of brackets, another set is placed inside it. However, this will makes the result something totally different.

> [!TIP]
>
> If doing the double brackets then there is no need to separate into different blocks to use the && and ||. Instead they can just be put inside the blocks themseleves.

> [!TIP]
>
> The syntax for the if statement is just an alias for the linux command **test**. So doing `if [$x=5]` is the same as `test $x=5`. This will return an <u>exist code</u>. However, the version of `if [[]]` is different since this is just a special bash keyword and it is a more safe and powerful version. The bash version supports pattern matching (regex), logical operators, and no need to quote variables that have a string with a space.

> [!CAUTION]
>
> Notice there is a space on both sides of the condition. If there is no space placed there then this WILL cause an error and code will fail. Always make sure to add the extra spaces.

> [!IMPORTANT]
>
> The single bracket version is POSIX compliant since it can works on shells like dash, sh, etc. However, the double bracket version is a bash version that is not POSIX compliant.

Can also do comparisons like using "=" to test if two things are equal, using "!=" to test if they are not equal, using "-z" to test if the value is empty, and "-n" is the value is not empty. However, that only works when comparing strings. 

```bash
x="Hello, World"

if [ "$x"="Hello" ]; then
	echo "Matched"
	exit 0
fi

exit 1
```



Even though everything is considered a string, to make this do numeric comparisons use the following instead:

| flag | Meaning                                                |
| ---- | ------------------------------------------------------ |
| -eq  | Checks if values are equal                             |
| -ne  | Checks if values are not equal                         |
| -lt  | Checks if value is less than other $x<50$              |
| -gt  | Checks if value is greater than other $x>50$           |
| -le  | Checks if value is less than or equal to $x \le 50$    |
| -ge  | Checks if value is greater than or equal to $x \ge 50$ |



```bash
x="Hello, World"
y=50

if [ "$y" -eq 50 ]; then
	echo "Matched"
	exit 0
fi

exit 1
```

Can also check if the name of something is a file or directory and if it exist or not. This is done with the following flags:

| flag | Meaning                                             |
| ---- | --------------------------------------------------- |
| -f   | Checks if thing is a file and it exist              |
| -d   | Checks if thing is a directory and it exist         |
| -e   | Checks if thing is a file or directory and it exist |
| -x   | Checks if thing is a file and is executable         |

```bash
if [ -f "myfile.txt" ]; then
  echo "File exists"
fi
```

Now, there is a way to make an if-else statement that will execute other code if the main condition fails. To add an else clause to this, just add the **else** keyword followed by the code to execute under it.

```bash
if [ condition ]; then
	# Code here
else
	# Code to execute otherwise
fi
```

There is a way to make to make this an else-if statement. To do this just add an **elif** keyword just like in python and after put the condition to be checked as well. After the condition is put, put the "; then" after and the code under the block like before.

```bash
if [ condition ]; then
	# Code here
elif [ condition ]; then
	# Code here
else
	# Code here
fi
```

There is a linux command **exit** that make it so the program will end. After it, it can have an optional number to specify an <u>exit code</u> that can be from 0 (success) to 1-255 (failure).

### Loops

A loop is a way to repeat a block of code until a specific condition is met or repeat something a specified amount of times. Just like an if statement, a loop works on a success or failure pattern. If the condition to check passes then the code is executed, but if the condition fails then the code does not execute and the program will leave that loop and continue to execute code after that loop.

#### For Loop

This type of loop is used to iterate over something a specific amount of times or until the condition fails. A for loop is kind of like an if statement in how it is written, but just uses different keywords. The way this functions is just like python where it has something to hold the current value of an index list being stepped through and must specify the list to walk through. The syntax for this is using the keywords **for**, **do**, and **done**:

```bash
for IndexValue in List; do
	echo "$IndexValue"
done
```

> [!NOTE]
>
> The above code does not iterate over the entire array. Instead, this will just return back the first index thing in the array. To iterate over all things in the array must use the `${ArrName[@]}` syntax.

Another way to make a for loop is to specify a certain number of times for this to execute. This will look like {start..end} where the end is inclusive. This also has a way to do stepping by certain values like in python as well by putting an additional .. followed by a number like {start..end..skip}.

```bash
for i in {1..5}; do
	echo $i
done
```

> [!NOTE]
>
> When a collection or range inside this this it will expand to individual parts. For example, doing `for i in {1..3}; do` turns to `for i in 1 2 3; do`. This means this can also be done explicitly. For example:
>
> ```bash
> x=("Yes" "No" "Maybe")
> 
> # for i in ${x[@]}; do
> for i in "Yes" "No" "Maybe"; do
>   echo ${i}
> done
> # Doing either of these will yield the same result
> ```



Another way to make an array is to use C style syntax. This is made slightly different by putting two sets of parentheses after the **for** keyword. Inside it will create a variable for an initializer separated by a semi-colon then the condition to evaluate followed by another semi-colon as well for the increment. For example `or (( i=0; i<5; i++ )); do echo "Hello" done`.

> [!CAUTION]
>
> It is important to also have the spaces at the start and end of the content inside like the if statement otherwise this will cause errors

The last way to make a for loop is using <u>globing</u> (regex) for the thing to iterate over. For example, doing `for i in *.java` will go over all java files in the current directory that end with the .java extension.

```bash
for file in *.java; do
    echo "Found text file: $file"
done
```



#### While loop

This is a way to execute code while the zero exit code value is returned from a condition or command. The way this is made is basically the same as the for loop except replace the keyword **for** with **while**. For example:

```bash
count=1
while [ $count -le 3 ]; do
    echo "Count is $count"
    ((count++))
done
```

The while loop can also support the double bracket syntax to get extra features. However, it also support the single separate bracket syntax as well. For example:

```bash
count=1
x=10

while [ $count -le 3 ] && [ $x -gt 5 ]; do
    echo "Count is $count"
    echo "X is $x"
    ((count++))
    ((x--))
done
```

Another way to use a while loop in a more unique way it so read a file line by line until the end. This uses the **read** command and the special predefined variable **IFS** and set its separation value to nothing. One important difference is at the **done** keyword, the file name output must be directed to it or else this will not know where to read the data from.

```bash
while IFS= read -r line; do
    echo "Line content: $line"
done < input.txt
```

> [!TIP]
>
> The -r flag here tells the read command not to treat backslashes as escape sequences. So if a line has \n then that will be treated literally as that.

#### Until Loop

This is a special type of loop that is unique because it is the opposite of the while loop because the code here will keep executing only while the result is false (any non-zero status code). This is made exactly the same way as the while loop except this uses the **until** keyword and not the 'while' keyword. For example:

```bash
until [[ -f /tmp/ready.txt ]]; do
    echo "Waiting for file..."
    sleep 2
done
echo "File detected!"
# This keeps looping until the file ready.txt is found in the /tmp directory. 
```

#### Loop Control

There are times that when a certain condition is met inside a loop, it should be left right away. Another case would be to not continue the rest of the code in the loop and start back at the top of the loop with a new iteration. This is achieved with the **break** and **continue** keyword. The **break** keyword will leave the current loop scope right away. The **continue** keyword will skip all the code that supposed to be executed after the current line and start at the top of the loop again.

## Functions and CLI Arguments

### CLI Arguments

When it comes to normal program, there can be CLI arguments supplied to the program that is used and can affect the outcome of the program. These are the same as in C where the first CLI argument will always be the name of the executing file, but the first going down will be the arguments passed into the program.

The way to get access to these arguments is to use the following:

| Variable           | Usage                                                       |
| ------------------ | ----------------------------------------------------------- |
| $0                 | The name of current program file executing                  |
| $1 - $9            | Variable name of first 9 CLI arguments                      |
| \${10} to $\infty$ | Variable name for all CLI arguments past 10+                |
| $#                 | Returns total number of CLI arguments passed in             |
| "$@"               | Displays all the CLI arguments as individual quoted strings |
| $*                 | Displays all the CLI arguments as a single quoted string    |
| $$                 | Returns the process ID (PID) of the current script          |

> [!WARNING]
>
> Can use $@ instead, but this is bad if strings are passed in that have spaces. This will just break the program. Always good to quote everything.

There is a special linux command **shift** that is specifically for working with CLI arguments. This command is called by itself. This is used as a way to help show a CLI argument is process by removing it and shifting all others. For example, there are two CLI arguments passed in so `$1` and `$2` hold values, but once the **shift**  is called then this will remove the current argument in `$1` and move the value in `$2` into the first one. This will then make it so the first argument no longer exist.

### Functions

A function is just a way to contain repeating logic to be called on later. The way a function is made is with the syntax `function <FunctionName>() {}` or with `<FunctionName>() {}`. It is important to know that there are no actual parameters that are supposed to be specified inside the parentheses as these are really just used to signal the things is a function.

To call a function, just put the function name. There are no parentheses used to signal a call

```bash
# Creates the function
DisplayAdd(){
	echo "Adding Now"
}

DisplayAdd # Calls the function
```



When it comes to passing arguments to functions, this is not typical like normal languages. Theses are passed like giving CLI arguments to the program when being called. Inside the function these will be accessed using the same rules when it comes to accessing CLI arguments of a program.

```bash
DisplayAdd(){
  x=$(( $1 + $2 ))
  echo "$x"
  echo $#
  echo $@
}

DisplayAdd 50 50
```

It is important to know that unlike other languages all variables created ANYWEHRE are considered global variables. So if a variable is created outside a function and inside that function it tries to create a variable with the same name then this will cause it to override the declaration outside the function. Same if a variable is declared inside a function as this will make the variable persist outside the function as well.

To resolve the variable scope issue, use the keyword **local** right before the variable name inside a function. This will give the ability to ensure that variable only exist inside that function and no where else.

```bash
DisplayAdd(){
  x=$(( $1 + $2 ))
  local y=$(( $1 + $2 ))
  
  echo $x # Will print 100
  echo $y # Will print 100
}

DisplayAdd 50 50

echo $x # Will print 100
echo $y # Does not print anything
```

If wanting to store the output of a function inside a variable, wrap the whole function call and arguments for it in a set of parentheses. Make sure there is a $ in front of the parentheses.

When wanting to return data from a function, this is not done the same way like in java or C. While there is a **return** keyword that takes a number to return only, this returns a <u>status code</u> for that function and not actual data. To return data from a function, the **echo** command must be used as printing the data is what will be returned. This is also why the following rule above regarding the parentheses for the function is needed since they act as a <u>capture group</u>.

```bash
GetAddResult(){
  if [ $# -ne 2 ]; then
    return 1
  fi

  echo $(( $1 + $2 ))
  return 0
}

x=$(GetAddResult 50 50)
status=$?

echo "result=$x"
echo "status=$status"
```

## I/O Redirection

In linux systems, there are three ways I/O gets around and these are done with something called <u>file descriptors</u>. Under the hood, these really just files or "data streams". These are represented by numbers with:

- 0 (stdin) --> representing data received. For example keyboard input
- 1 (stdout) --> represents sending data. For example printing to the terminal by default
- 2 (stderr) --> represented sending error data. Works just like stdout except this only gets data if error occurs in program.



When it comes to calling the actual program on CLI or inside the bash scripts is where this is useful. There are special symbols used to signal what is considered output, input, and error data. This is done with something called <u>output redirection</u> (stdout) and <u>input redirection</u> (stdin). The symbols are:

- `>` --> This is used to write data to a file, but will overwrite any data inside that file.
- `>>` --> This is used to write data to a file, but will append the content to that file instead of overwriting in it.
- `<` --> This will take content from a file and feed it into a commands stdin.
- `2>` --> This is used to redirect ONLY error messages to a specific file.
- `&2>` --> This is used to redirect stdout and stderr data to a specific file
- `> /dev/null 2>&1` --> This is used to totally discard the stdout and stderr data into what is called the "void".

```bash
echo "Hello" > greet.txt          # overwrite file
echo "World" > greet.txt          # overwrite again
echo "Bye" >> greet.txt           # append to file

x=$(cat < greet.txt)               # read file via stdin

ls greet.txt non_existent 2> err.txt     # write errors only to file
ls greet.txt non_existent &> all.txt     # write stdout + stderr to file

ls greet.txt > /dev/null 2>&1     # discard all output (stdout + stderr)
```









##### TODO Check List

- [x] File Setup 
- [x] Variables
- [x] Data Types
- [x] Functions
- [x] Loops
- [x] Conditionals
- [x] CLI Arguments
- [x] Shell Expansion & Substitution
- [x] Quoting & Escaping
- [ ] CLI commands
- [x] I/O
- [ ] Processes
- [x] Exit Codes & Error Handling
- [ ] Debugging & Testing
- [ ] Signal Handling
- [ ] Coprocesses
- [x] Subshells vs Current Shell
- [x] Word splitting & $IFS
- [x] Arrays
- [x] "\$@" and $@
- [ ] Environment & Shell Behavior
- [ ] Text Processing Power
- [x] Built-in Commands vs External Tools
- [x] Pipes and Command Chaining
- [ ] Job Control
- [x] Sourcing vs Executing Scripts
- [ ] Traps





# TODO

[^subshell]: talk about special syntax about subshell with parenthesis and about the subshell in general.



