// Comprehensive C++ Example
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <memory>
#include <algorithm>
#include <exception>
// #include <typeinfo>

// 1. Namespace
namespace ExampleNamespace {
    const int CONST_VAR = 42;
}

// 2. Enum and enum class
enum Color { RED, GREEN, BLUE };
enum class Direction { UP, DOWN, LEFT, RIGHT };

// 3. Class, struct, access specifiers, constructor, destructor, static, mutable, friend
class Person {
private:
    std::string name;
    mutable int accessCount; // mutable keyword
    static int population;   // static member

public:
    Person(const std::string& n) : name(n), accessCount(0) { ++population; }
    ~Person() { --population; }

    void greet() const {
        ++accessCount;
        std::cout << "Hello, I am " << name << "\n";
    }

    static int getPopulation() { return population; }

    friend void showName(const Person& p);
};

int Person::population = 0;

void showName(const Person& p) {
    std::cout << "Person's name: " << p.name << "\n";
}

// 4. Template function
template<typename T>
T add(T a, T b) {
    return a + b;
}

// 5. Template class
template<typename T>
class Container {
    T value;
public:
    Container(T v) : value(v) {}
    T get() const { return value; }
};

// 6. Inheritance, virtual, override, final
class Animal {
public:
    virtual void speak() { std::cout << "Animal sound\n"; }
};

class Dog : public Animal {
public:
    void speak() override final { std::cout << "Woof!\n"; }
};

// 7. Try, catch, throw, exception
void mightThrow(bool flag) {
    if(flag) throw std::runtime_error("An error occurred");
}

// 8. Lambda, auto, decltype, nullptr, static_assert
auto lambdaExample = [](int x) -> int { return x * x; };
static_assert(sizeof(int) == 4, "Unexpected int size!");

// 9. Range-based for, for, while, do-while, if, switch, break, continue
void loopsAndConditions() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    for(auto v : vec) {
        if(v % 2 == 0) continue;
        std::cout << v << " ";
    }
    std::cout << "\n";

    int i = 0;
    while(i < 3) { std::cout << i << " "; ++i; }
    std::cout << "\n";

    do { std::cout << "Do-while once\n"; } while(false);

    int n = 2;
    switch(n) {
        case 1: std::cout << "One\n"; break;
        case 2: std::cout << "Two\n"; break;
        default: std::cout << "Other\n";
    }
}

// 10. Pointers, references, new/delete, smart pointers
void pointerExamples() {
    int x = 10;
    int* ptr = &x;
    int& ref = x;

    std::unique_ptr<int> uptr = std::make_unique<int>(100);
    std::shared_ptr<int> sptr = std::make_shared<int>(200);

    std::cout << "Pointer: " << *ptr << ", Reference: " << ref
              << ", Unique Ptr: " << *uptr << ", Shared Ptr: " << *sptr << "\n";
}

// 11. STL containers, iterators, algorithms
void stlExamples() {
    std::vector<int> v = {3, 1, 4, 1, 5};
    std::sort(v.begin(), v.end());
    for(auto it = v.begin(); it != v.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";

    std::map<std::string, int> m;
    m["Alice"] = 30;
    m["Bob"] = 25;
}

// 12. Constexpr, inline, friend (already shown), volatile
constexpr int square(int n) { return n * n; }

// 13. Type casting
void castingExamples() {
    double pi = 3.1415;
    int intPi = static_cast<int>(pi);
    std::cout << "Cast double to int: " << intPi << "\n";
}

// 14. Main function
int main() {
    std::cout << "C++ Keywords and Topics Demo\n";

    // Namespace usage
    std::cout << "Const from namespace: " << ExampleNamespace::CONST_VAR << "\n";

    // Classes
    Person p("Alice");
    p.greet();
    showName(p);
    std::cout << "Population: " << Person::getPopulation() << "\n";

    // Templates
    std::cout << "Template add<int>: " << add(5, 7) << "\n";
    Container<std::string> c("Hello");
    std::cout << "Template class: " << c.get() << "\n";

    // Inheritance
    Dog d;
    d.speak();

    // Exceptions
    try { mightThrow(true); }
    catch(const std::exception& e) { std::cout << "Caught exception: " << e.what() << "\n"; }

    // Loops and conditions
    loopsAndConditions();

    // Pointers
    pointerExamples();

    // STL
    stlExamples();

    // Casting
    castingExamples();

    // Lambda
    std::cout << "Lambda square 5: " << lambdaExample(5) << "\n";

    // Constexpr
    std::cout << "Constexpr square 6: " << square(6) << "\n";

    return 0;
}
