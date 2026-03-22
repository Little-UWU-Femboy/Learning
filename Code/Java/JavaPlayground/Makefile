# 1. Manual Path Configuration
# Change this path to match the exact location on the computer
JDK_PATH = C:\Program Files\Java\jdk-21\bin

ifeq ($(OS),Windows_NT)
    # Windows Commands using the Manual Path
    JC = "$(JDK_PATH)\javac.exe"
    JVM = "$(JDK_PATH)\java.exe"
    JDOC = "$(JDK_PATH)\javadoc.exe"
    CLEAN_CMD = if exist bin del /q bin\*.class
    MKDIR_BIN = if not exist bin mkdir bin
    MKDIR_DOCS = if not exist docs mkdir docs
    SEP = \\
else
    # Mac/Linux Settings (Standard paths usually work here)
    JC = javac
    JVM = java
    JDOC = javadoc
    CLEAN_CMD = rm -f bin/*.class
    MKDIR_BIN = mkdir -p bin
    MKDIR_DOCS = mkdir -p docs
    SEP = /
endif

# 2. Variables
JFLAGS = -d bin
CP = -cp bin
SRC_DIR = src
SOURCES = $(SRC_DIR)$(SEP)*.java
MAIN = Main

# 3. Targets
all: compile

compile:
	@$(MKDIR_BIN)
	$(JC) $(JFLAGS) $(SOURCES)

run:
	$(JVM) $(CP) $(MAIN)

rebuild: clean compile

clean:
	@$(CLEAN_CMD)

docs:
	@$(MKDIR_DOCS)
	$(JDOC) -d docs $(SOURCES)
