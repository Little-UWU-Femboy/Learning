# Setup

1. First install the antlr4 base [jar file](https://www.antlr.org/download.html) tool
2. Ensure that python 3.6.* is installed on system as this is the minimum version required.
3. Run `pip3 install antlr4-python3-runtime` to install the needed python runtime. If python version is installed with brew then will have to create a virtual environment to do this. However, if python without a package mananger (like I have) then can just run that command.
4. 



DISCLAIMER: I am on MacOS. All the commands being ran here work on MacOS, however I do not know if these commands will be the same for windows

```shell
# Command 1
# Used pip3 and not pip as the documentation says to run the following, but this didn't work -->  pip install antlr4-python3-runtime
# There is a weird thing that happens if python is installed via a package manager and trying to run pip3 install. I don't have my
# Python version installed with homebrew so this works normally for me 
pip3 install antlr4-python3-runtime

# Command 2
# Now download submitted files and do:
# Included the .jar file in case you cannot find it
java -jar ./antlr-4.13.2-complete.jar -Dlanguage=Python3 XMLLexer.g4

# Command 3
# Example of input input from io folder downloaded
python3 Driver.py < io/error_bohemian.xml
```

References to all the python modules can be found [here](https://github.com/antlr/antlr4/tree/dev/runtime/Python3/src/antlr4)

Antlr4 book code converted to [python code](https://github.com/jszheng/py3antlr4book)

How to run code was gotten from [here](https://github.com/antlr/grammars-v4/tree/master/python/python3/Python3)