#include <iostream> 

int main()
{
    int a;
    int b;

    std::cout << "Enter the first number: ";
    std::cin >> a; 
    std::cout << "Enter the second number: ";
    std::cin >> b;

    std::cout << "The sum of " << a << " and " << b << " is = " << a + b << std::endl;
    
    return 0;
}
