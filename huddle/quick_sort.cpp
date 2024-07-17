#include <iostream>
#include <chrono>
#include <algorithm>
#include <random>

using namespace std;

constexpr int MAX_SIZE = 300;
constexpr int INSERTION_SORT_THRESHOLD = 32;

inline void insertionSort(int* arr, int start, int end) {
    for (int i = start + 1; i <= end; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= start && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

inline int medianOfThree(int* arr, int lo, int hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] < arr[lo])
        swap(arr[lo], arr[mid]);
    if (arr[hi] < arr[lo])
        swap(arr[lo], arr[hi]);
    if (arr[hi] < arr[mid])
        swap(arr[hi], arr[mid]);
    return arr[hi];
}

void quickSort(int* arr, int lo, int hi) {
    while (lo < hi) {
        if (hi - lo + 1 <= INSERTION_SORT_THRESHOLD) {
            insertionSort(arr, lo, hi);
            return;
        }
        int pivot = medianOfThree(arr, lo, hi);
        
        int lt = lo, i = lo, gt = hi;
        while (i <= gt) {
            if (arr[i] < pivot)
                swap(arr[lt++], arr[i++]);
            else if (arr[i] > pivot)
                swap(arr[i], arr[gt--]);
            else
                i++;
        }
        
        if (lt - lo < hi - gt) {
            quickSort(arr, lo, lt - 1);
            lo = gt + 1;
        } else {
            quickSort(arr, gt + 1, hi);
            hi = lt - 1;
        }
    }
}

unsigned int fastRand() {
    static random_device rd;
    static mt19937 gen(rd());
    static uniform_int_distribution<> dis(0, 0x7FFF);
    return dis(gen);
}

void testSort(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; i++) {
        arr[i] = fastRand() % 1000;
    }

    auto start = chrono::high_resolution_clock::now();
    quickSort(arr, 0, size - 1);
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double, milli> elapsed = end - start;
    cout << "Size: " << size << ", Time: " << elapsed.count() << " ms" << endl;

    if (!is_sorted(arr, arr + size)) {
        cout << "Error: Array not sorted correctly!" << endl;
    }

    delete[] arr;
}

int main() {
    const int sizes[] = {100, 300, 500};
    
    for (int size : sizes) {
        cout << "\nTesting with size " << size << ":" << endl;
        testSort(size);
    }
    return 0;
}
