'''
01. Búsqueda en lista ordenada: Implementa una función de búsqueda binaria 
que determine si un número está en una lista ordenada de 10 elementos.
'''

class Color:
    GREEN_BG = '\x1b[32m'
    END_CLR = '\033[0m'

GREEN_BG = Color.GREEN_BG
END = Color.END_CLR

def binary_search(array, target, low, high):
    if low > high:
        return "Not found"

    mid = (low + high) // 2
    print(f"Mid index: {mid}, Mid value: {array[mid]}")

    if array[mid] == target:
        print(f"{GREEN_BG}{'->'*30}{END}")
        print(f"Found {target} at index {mid}")
        return array[mid]
    elif array[mid] < target:
        print(f"Current mid value {array[mid]} is less than target {target}. Searching right subarray: {array[mid+1:high+1]}")
        return binary_search(array, target, mid + 1, high)
    else:
        print(f"Current mid value {array[mid]} is greater than target {target}. Searching left subarray: {array[low:mid]}")
        return binary_search(array, target, low, mid - 1)

# Input your own array and target
# array = [int(x) for x in input("Enter your array: ").split()]
# array.sort()
# target = int(input("Enter your target value: "))

# Test case
array = [54, 74, 3, 81, 22, 3, 4, 91, 23, 5]
array.sort() # Ordered list
target = 3

print(f"{GREEN_BG}{'->'*30}{END}")
result = binary_search(array, target, 0, len(array) - 1)
