import re

def cpp_to_c(cpp_code):
    c_code = cpp_code

    # 1. Convert class definition to struct
    # class Name { ... };  → typedef struct Name { ... } Name;
    class_pattern = r'class\s+(\w+)\s*{([^}]*)};'
    def class_to_struct(match):
        name = match.group(1)
        body = match.group(2)
        # Remove 'public:' keywords
        body = body.replace('public:', '')
        return f"typedef struct {name} {{{body}}} {name};"
    c_code = re.sub(class_pattern, class_to_struct, c_code, flags=re.MULTILINE)

    # 2. Convert method definitions inside class to functions
    # void method(int x) { ... } → void Class_method(Class* self, int x) { ... }
    method_pattern = r'\bvoid\s+(\w+)\s*\(([^)]*)\)\s*{'
    c_code = re.sub(method_pattern, lambda m: f"void {m.group(1)}({m.group(2)}, ...) {{", c_code)

    # 3. Replace member access: obj.method(...) → Class_method(&obj, ...)
    # This is a very basic replacement for demonstration
    c_code = re.sub(r'(\w+)\.(\w+)\(', r'\2(&\1, ', c_code)

    # 4. Replace cout with printf
    c_code = c_code.replace('cout << ', 'printf("')
    c_code = c_code.replace('<< endl;', '\\n");')

    # 5. Replace 'new Class()' with malloc
    c_code = re.sub(r'new\s+(\w+)\s*\(\s*\)', r'(struct \1*)malloc(sizeof(struct \1))', c_code)

    return c_code

# Example C++ input
cpp_example = """
#include <iostream>
using namespace std;

class Point {
public:
    int x, y;
    void move(int dx, int dy) { x += dx; y += dy; }
};

int main() {
    Point p;
    p.move(1, 2);
    cout << p.x << endl;
}
"""

c_output = cpp_to_c(cpp_example)
print(c_output)