#include <fstream>
#include <iostream>

int main() {
  std::cout << "Attempting to create file..." << std::endl;

  // Attempt to write a completely new file
  std::ofstream outFile(
      "C:\\Users\\Owner\\HOME\\Learning\\Code\\test_output.c");

  if (outFile.is_open()) {
    outFile << "Success!\n";
    outFile.close();
    std::cout << "File created successfully." << std::endl;
  } else {
    std::cout << "CRITICAL ERROR: Operating system blocked file creation."
              << std::endl;
  }

  return 0;
}
