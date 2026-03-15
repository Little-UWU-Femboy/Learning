ifeq ($(OS),Windows_NT)
    # Windows Settings
    CXX = clang++
    CXXFLAGS = -Wall -g -std=c++20 -static -static-libgcc -static-libstdc++ -pthread
    TARGET = $(BIN_DIR)/out.exe
    MKDIR = if not exist $(OBJ_DIR) mkdir $(OBJ_DIR) && if not exist $(BIN_DIR) mkdir $(BIN_DIR)
    RM = del /Q
    FIX_PATH = $(subst /,\,$1)
    EXEC = $(TARGET)
else
    # macOS Settings
    CXX = clang++
    CXXFLAGS = -std=c++20 -Wall -g
    TARGET = $(BIN_DIR)/out
    MKDIR = mkdir -p $(OBJ_DIR) $(BIN_DIR)
    RM = rm -rf
    FIX_PATH = $1
    EXEC = ./$(TARGET)
endif

# Directories
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin

# Find all cpp files
SRCS = $(wildcard $(SRC_DIR)/*.cpp)

# Convert cpp files to object files in obj directory
OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRCS))

# Default target
all: directories $(TARGET)

# Create directories
directories:
	@$(MKDIR)

# Link object files
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

# Compile cpp files to object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean target
clean:
ifeq ($(OS),Windows_NT)
	@if exist $(BIN_DIR) $(RM) $(call FIX_PATH,$(BIN_DIR)\*) 2>nul
	@if exist $(OBJ_DIR) $(RM) $(call FIX_PATH,$(OBJ_DIR)\*) 2>nul
else
	@$(RM) $(OBJ_DIR)/*.o $(TARGET)
endif

# Run the executable
run: all
	@$(EXEC)
