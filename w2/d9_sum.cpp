/*
DIA 9
Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)
*/

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
