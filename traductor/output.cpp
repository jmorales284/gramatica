int resta(int a, int b) {
a - b;
}

int factorial(int n) {
if (n == 0) {
1;
} else {
n * factorial(resta(n, 1));
}
}

#include <iostream>

int main() {
    std::cout << factorial(6) << std::endl;
    return 0;
}