/*
02. Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando
 cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).
*/

#include <iostream>
#include <vector>

void bubbleSort(std::vector<int>& vi){
	int n = vi.size();	
	for (int i = 0; i < n - 1; ++i){
		int limit = n - i - 1;
		for (int j = 0; j < limit; ++j){
			if (vi[j] > vi[j + 1]){
				std::swap(vi[j], vi[j + 1]);
			}
		}
	}
}

void printArray(std::vector<int>& vi){
	for (int i = 0; i < vi.size(); ++i)
	{
		std::cout << vi[i] << " ";
	}
	std::cout << std::endl;
}

int main(){
	
	std::vector<int> vi = {1, 10, 2, 9, 3, 8, 4, 7, 5, 6};
	bubbleSort(vi);
	printArray(vi);
	return 0;
}
