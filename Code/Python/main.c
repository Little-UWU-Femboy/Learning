#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PI 3.14159
#define SQUARE(x) ((x) * (x))

// Enum
typedef enum {
    RED,
    GREEN,
    BLUE
} Color;

// Structure
typedef struct {
    char name[50];
    int age;
} Person;

// Union
typedef union {
    int i;
    float f;
    char str[20];
} Data;

// Function prototypes
void basicDemo();
int factorial(int n);
void pointerDemo();
void arrayDemo();
void stringDemo();
void structureUnionEnumDemo();
void dynamicMemoryDemo();
void fileIODemo();
void functionPointerDemo();
void bitwiseDemo();

// Function pointer target
int add(int a, int b) {
    return a + b;
}

// Recursive function
int factorial(int n) {
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

int main(int argc, char *argv[]) {

    printf("C Comprehensive Demo Program\n\n");

    // Command line arguments
    printf("Command Line Arguments:\n");
    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }

    basicDemo();
    arrayDemo();
    stringDemo();
    pointerDemo();
    structureUnionEnumDemo();
    dynamicMemoryDemo();
    functionPointerDemo();
    bitwiseDemo();
    fileIODemo();

    printf("\nFactorial of 5 = %d\n", factorial(5));

    return 0;
}

// Basic concepts
void basicDemo() {
    printf("\n--- Basic Demo ---\n");

    int a = 10;
    float b = 5.5;
    char c = 'A';
    const int CONST_VAL = 100;

    printf("a = %d, b = %.2f, c = %c\n", a, b, c);
    printf("Constant = %d\n", CONST_VAL);

    printf("PI = %.2f\n", PI);
    printf("Square of 4 = %d\n", SQUARE(4));

    if (a > 5)
        printf("a is greater than 5\n");

    switch (c) {
        case 'A':
            printf("Character is A\n");
            break;
        default:
            printf("Unknown character\n");
    }

    for (int i = 0; i < 3; i++)
        printf("For Loop i = %d\n", i);

    int i = 0;
    while (i < 2) {
        printf("While Loop i = %d\n", i);
        i++;
    }
}

// Arrays
void arrayDemo() {
    printf("\n--- Array Demo ---\n");

    int arr[5] = {1, 2, 3, 4, 5};
    int matrix[2][2] = {{1,2},{3,4}};

    for (int i = 0; i < 5; i++)
        printf("%d ", arr[i]);
    printf("\n");

    printf("2D Array:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
}

// Strings
void stringDemo() {
    printf("\n--- String Demo ---\n");

    char str1[20] = "Hello";
    char str2[20] = "World";

    strcat(str1, " ");
    strcat(str1, str2);

    printf("Concatenated String: %s\n", str1);
    printf("Length: %lu\n", strlen(str1));
}

// Pointers
void pointerDemo() {
    printf("\n--- Pointer Demo ---\n");

    int x = 10;
    int *ptr = &x;

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", (void*)&x);
    printf("Pointer ptr: %p\n", (void*)ptr);
    printf("Value at ptr: %d\n", *ptr);
}

// Struct, Union, Enum
void structureUnionEnumDemo() {
    printf("\n--- Struct, Union, Enum Demo ---\n");

    Person p1 = {"Alice", 25};
    printf("Person: %s, Age: %d\n", p1.name, p1.age);

    Data data;
    data.i = 10;
    printf("Union int: %d\n", data.i);
    data.f = 220.5;
    printf("Union float (overwrites int): %.2f\n", data.f);

    Color color = GREEN;
    printf("Enum value (GREEN): %d\n", color);
}

// Dynamic Memory
void dynamicMemoryDemo() {
    printf("\n--- Dynamic Memory Demo ---\n");

    int *arr = (int*)malloc(5 * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);
}

// Function Pointer
void functionPointerDemo() {
    printf("\n--- Function Pointer Demo ---\n");

    int (*funcPtr)(int, int) = add;
    printf("Addition using function pointer: %d\n", funcPtr(5, 3));
}

// Bitwise Operations
void bitwiseDemo() {
    printf("\n--- Bitwise Operations Demo ---\n");

    int a = 5;  // 0101
    int b = 3;  // 0011

    printf("a & b = %d\n", a & b);
    printf("a | b = %d\n", a | b);
    printf("a ^ b = %d\n", a ^ b);
    printf("~a = %d\n", ~a);
    printf("a << 1 = %d\n", a << 1);
    printf("a >> 1 = %d\n", a >> 1);
}

// File I/O
void fileIODemo() {
    printf("\n--- File I/O Demo ---\n");

    FILE *fp = fopen("demo.txt", "w");

    if (fp == NULL) {
        printf("File could not be opened\n");
        return;
    }

    fprintf(fp, "Hello File Handling in C!\n");
    fclose(fp);

    printf("Data written to demo.txt\n");
}
