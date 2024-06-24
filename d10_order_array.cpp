/*
DIA 10
Ordenamiento de un Array: Escribir un programa que ordene un array de enteros �Pero hazlo en C++! :)
*/

#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int arr[] = {1, 16, 8, 19, 21, 3, 5};

    int size = sizeof(arr) / sizeof(arr[0]);

    std::sort(std::begin(arr), std::end(arr));

    std::cout << "Sorted array: ";

    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << ' ';
    }

    return 0;
}

// Vector version

//int main()
//{
//    int n;
//
//    std::cout << "Enter size of 'array': ";
//    std::cin >> n;
//    std::vector<int> nums(n);
//
//    for (int i = 0; i < n; ++i)
//    {
//        std::cout << "Enter number " << i + 1<< " : ";
//        std::cin >> nums[i];
//    }
//
//    std::sort(std::begin(nums), std::end(nums));
//
//    std::cout << "Sorted 'array': ";
//
//    for (int i = 0; i < nums.size(); i++)
//    {
//        std::cout << nums[i] << " ";
//    }
//
//    std::cout << std::endl;
//
//    return 0;
//
//}
