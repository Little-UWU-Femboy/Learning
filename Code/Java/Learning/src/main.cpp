#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string name;
    int age;

protected:
    int salary;

public:
    // Constructor
    Employee(string name, int age) {
        this->name = name;
        this->age = age;
    }

private:
    int salaryIncrease() {
        this->salary += 300;
        return this->salary + 300;
    }

protected:
    void displaySalary() {
        cout << this->salary << endl;
    }

public:
    void wrapper() {
        salaryIncrease();
        displaySalary();
    }
};