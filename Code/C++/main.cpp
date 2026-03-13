#include <vector>
#include <iostream>

class Foo {
public:
    constexpr int add(int a, int b) {
        return a + b;
    }
};

int main() {
    std::vector<int> nums = {1,2,3};

    auto lambda = [&](int x) {
        return x * 2;
    };

    std::cout << lambda(5) << std::endl;
}
