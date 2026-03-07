// dummy_all_cpp_topics.cpp

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <memory>
#include <thread>
#include <mutex>
#include <fstream>
#include <optional>
#include <variant>
#include <algorithm>
#include <functional>
#include <stdexcept>

#define PI 3.14159
#define SQUARE(x) ((x)*(x))

using std::cout;
using std::endl;

// enum
enum Color {
    RED,
    GREEN,
    BLUE
};

// enum class
enum class Direction {
    North,
    South,
    East,
    West
};

// struct
struct Point {
    int x;
    int y;
};

// union
union Data {
    int i;
    float f;
    char c;
};

// forward declaration
class Base;

// template function
template<typename T>
T add(T a, T b) {
    return a + b;
}

// constexpr function
constexpr int squareConstexpr(int x) {
    return x * x;
}

// inline function
inline int multiply(int a, int b) {
    return a * b;
}

// abstract base class
class Base {
public:
    virtual void speak() const = 0;
    virtual ~Base() {}
};

// derived class
class Dog : public Base {
public:
    void speak() const override {
        cout << "Dog barks\n";
    }
};

// class with many features
class Example {
private:
    int value;

public:
    static int count;

    Example() : value(0) {
        count++;
    }

    Example(int v) : value(v) {
        count++;
    }

    // copy constructor
    Example(const Example& other) {
        value = other.value;
    }

    // move constructor
    Example(Example&& other) noexcept {
        value = other.value;
        other.value = 0;
    }

    // destructor
    ~Example() {}

    // operator overloading
    Example operator+(const Example& other) const {
        return Example(value + other.value);
    }

    // getter
    int get() const {
        return value;
    }

    // setter
    void set(int v) {
        value = v;
    }

    // friend function
    friend std::ostream& operator<<(std::ostream& os, const Example& ex);
};

int Example::count = 0;

std::ostream& operator<<(std::ostream& os, const Example& ex) {
    os << ex.value;
    return os;
}

// template class
template<typename T>
class Box {
public:
    T value;

    Box(T v) : value(v) {}

    T get() {
        return value;
    }
};

// lambda example
void lambdaExample() {
    auto lambda = [](int a, int b) {
        return a + b;
    };

    cout << "Lambda: " << lambda(3,4) << endl;
}

// exception example
void exceptionExample() {
    try {
        throw std::runtime_error("Example exception");
    }
    catch(const std::exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
}

// thread example
std::mutex mtx;

void threadTask(int id) {
    std::lock_guard<std::mutex> lock(mtx);
    cout << "Thread " << id << " running\n";
}

// file IO
void fileExample() {
    std::ofstream out("test.txt");
    out << "Hello File\n";
    out.close();

    std::ifstream in("test.txt");
    std::string line;
    std::getline(in, line);
    cout << line << endl;
}

// STL container example
void containerExample() {
    std::vector<int> vec = {1,2,3,4};

    std::map<std::string,int> mp;
    mp["a"] = 1;
    mp["b"] = 2;

    for(auto& v : vec)
        cout << v << " ";

    cout << endl;

    std::for_each(vec.begin(), vec.end(), [](int n){
        cout << n*n << " ";
    });

    cout << endl;
}

// optional / variant
void modernTypes() {
    std::optional<int> opt = 5;

    if(opt)
        cout << "Optional: " << *opt << endl;

    std::variant<int, std::string> var;
    var = "hello";

    std::visit([](auto&& arg){
        cout << arg << endl;
    }, var);
}

// casting examples
void castingExample() {
    double d = 3.5;
    int i = static_cast<int>(d);

    cout << "Cast: " << i << endl;
}

// pointer & reference
void pointerReferenceExample() {
    int a = 10;

    int* ptr = &a;
    int& ref = a;

    *ptr = 20;
    ref = 30;

    cout << a << endl;
}

// smart pointers
void smartPointerExample() {
    std::unique_ptr<int> up = std::make_unique<int>(10);
    std::shared_ptr<int> sp = std::make_shared<int>(20);

    cout << *up << " " << *sp << endl;
}

int main() {

    cout << "Macros: " << PI << " " << SQUARE(5) << endl;

    Point p{1,2};
    cout << "Point: " << p.x << "," << p.y << endl;

    Data data;
    data.i = 42;
    cout << "Union: " << data.i << endl;

    Example a(5), b(7);
    Example c = a + b;

    cout << "Example: " << c << endl;

    Box<int> box(100);
    cout << "Box: " << box.get() << endl;

    lambdaExample();
    exceptionExample();
    containerExample();
    modernTypes();
    castingExample();
    pointerReferenceExample();
    smartPointerExample();
    fileExample();

    Dog dog;
    Base* basePtr = &dog;
    basePtr->speak();

    std::thread t1(threadTask, 1);
    std::thread t2(threadTask, 2);

    t1.join();
    t2.join();

    cout << "Template add: " << add(2,3) << endl;

    cout << "Constexpr: " << squareConstexpr(6) << endl;

    cout << "Inline: " << multiply(3,4) << endl;

    auto x = 5;
    decltype(x) y = 10;

    cout << "Auto/decltype: " << x+y << endl;

    return 0;
}
