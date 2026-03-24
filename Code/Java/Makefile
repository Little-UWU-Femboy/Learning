Output = bin
MainClass = Main

# Detect OS
ifeq ($(OS),Windows_NT)
    RM = if exist $(Output) del /Q $(Output)\*.class
    MKDIR = if not exist $(Output) mkdir $(Output)
else
    RM = rm -rf $(Output)
    MKDIR = mkdir -p $(Output)
endif

all: compile run

compile:
	@$(MKDIR)
	javac -d $(Output) *.java

run:
	java -cp $(Output) $(MainClass)

clean:
	@$(RM)
	@echo Deleting Class Files
