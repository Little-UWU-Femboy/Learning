# CMake

This is a tool that builds things like the *Makefile* for the system, but does not actually run the commands.

To use this, the root directory will need to have a file called **CMakeLists.txt**. Inside this file, will include all the commands that the *Makefile* will end up generated with.

To run this, use the command `cmake -S <path to CMakeList.txt> -B <Path to build path >`