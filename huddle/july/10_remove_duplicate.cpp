// 10. Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.

#include <iostream>
#include <vector>
#include <set>

std::vector<int> removeDuplicates(const std::vector<int>& array) {
    std::set<int> seen;
    std::vector<int> uniqueArray;

    for (int element : array) {
        if (seen.find(element) == seen.end()) {  
            seen.insert(element);
            uniqueArray.push_back(element);
        }
    }

    return uniqueArray;
}

int main() {
    std::vector<int> array = {1, 2, 2, 3, 4, 4, 5};
    std::vector<int> uniqueArray = removeDuplicates(array);

    for (int element : uniqueArray) {
        std::cout << element << " ";
    }

    return 0;
}
