# Setup

1. First install the antlr4 base [jar file](https://www.antlr.org/download.html) tool
2. Ensure that python 3.7.* is installed on system as this is the minimum version required.
3. Run `pip3 install antlr4-python3-runtime` to install the needed python runtime. If python version is installed with brew then will have to create a virtual environment to do this. However, if python is installed without a package mananger (like I have) then that command will run successfully.

> [!CAUTION]
>
> I am on MacOS. All the commands being ran here work on MacOS. I do not know the equivalent version of the windows commands

```shell
# Command 1
pip3 install antlr4-python3-runtime

# Command 2
# Now download submitted files and do:
# Included the .jar file in case you cannot find it
java -jar ./antlr-4.13.2-complete.jar -Dlanguage=Python3 -no-listener -visitor logo.g4

# Command 3
# Example of input input from io folder downloaded
cat io/ex05.logo | python3 Driver.py > img.svg && open img.svg
```

References to all the python modules can be found [here](https://github.com/antlr/antlr4/tree/dev/runtime/Python3/src/antlr4)

Antlr4 book code converted to [python code](https://github.com/jszheng/py3antlr4book)

How to run code was gotten from [here](https://github.com/antlr/grammars-v4/tree/master/python/python3/Python3)

> [!NOTE]
>
> I made .py file equivalents to all the java class files. I basically just copied word from word those .java files into python versions and added the needed logic as necessary.
