#include <fstream>
#include <iostream>
#include <regex>
#include <string>

int main() {
  // Open the C++ input file and the C output file
  std::ifstream inFile("C:\\Users\\Owner\\HOME\\Learning\\Code\\input.cpp");
  std::ofstream outFile("C:\\Users\\Owner\\HOME\\Learning\\Code\\output.c");

  if (!inFile.is_open() || !outFile.is_open()) {
    std::cerr << "Error: Could not open input.cpp or output.c" << std::endl;
    return 1;
  }

  std::string line;

  // Read the C++ file line by line
  while (std::getline(inFile, line)) {

    // 1. Swap <iostream> for <stdio.h>
    line = std::regex_replace(line, std::regex("#include <iostream>"),
                              "#include <stdio.h>");

    // 2. Remove 'using namespace std;' as it does not exist in C
    line = std::regex_replace(line, std::regex("using namespace std;"), "");

    // 3. Naively convert a basic std::cout statement to a printf statement
    // Example: std::cout << "Hello World" << std::endl; -> printf("Hello
    // World\n");
    std::smatch match;
    std::regex cout_regex(R"(std::cout\s*<<\s*\"([^\"]*)\"\s*<<\s*std::endl;)");

    if (std::regex_search(line, match, cout_regex)) {
      line = std::regex_replace(line, cout_regex, "printf(\"$1\\n\");");
    }

    // Output the transformed line to the .c file
    // Skip empty lines left by removing namespace declarations
    if (!line.empty() || line == "") {
      outFile << line << "\n";
    }
  }

  std::cout << "Transpilation complete. Check output.c" << std::endl;

  inFile.close();
  outFile.close();

  return 0;
}
