#include <iostream>

class Person {
public:
  std::string name;
  int age;

  Person(std::string name, int age) {
    this->name = name;
    this->age = age;
  }

  void introduce() {
    std::cout << "Hi, my name is " << name << " and I am " << age
              << " years old." << std::endl;
  }

private:
  void ShowMe() { std::cout << "Hello Friend" << std::endl; }
};

int main() {
  Person p1("Alice", 25);

  p1.introduce();
  int x = 50;
  if (x == 60){
      
  }

  return 0;
}
