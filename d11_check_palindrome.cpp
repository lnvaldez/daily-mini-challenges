/*
DIA 11
Pal�ndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un pal�ndromo �Pero hazlo en C++! :)
*/

#include <iostream>
#include <algorithm>
#include <cctype>
#include <string>

int main()
{
    std::string str;

    std::cout << "Enter your string: ";
    std::getline(std::cin, str);

    // Create a copy of the original string for transformation
    std::string rev_str = str;

    // Transform both strings to lowercase
    std::transform(str.begin(), str.end(), str.begin(), 
                   [](unsigned char c) { return std::tolower(c); });
    std::transform(rev_str.begin(), rev_str.end(), rev_str.begin(), 
                   [](unsigned char c) { return std::tolower(c); });

    // Remove non-alphanumeric characters from both strings
    str.erase(std::remove_if(str.begin(), str.end(), 
               [](unsigned char c) { return !std::isalnum(c); }), str.end());
    rev_str.erase(std::remove_if(rev_str.begin(), rev_str.end(), 
               [](unsigned char c) { return !std::isalnum(c); }), rev_str.end());

    // Reverse the string for comparison
    std::reverse(rev_str.begin(), rev_str.end());

    // Compare the original string with the reversed string
    if (str == rev_str)
    {
        std::cout << "Palindrome";
    }
    else
    {
        std::cout << "Not a palindrome";
    }

    std::cout << std::endl;

    return 0;
}

