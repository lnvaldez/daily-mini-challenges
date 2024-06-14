'''
DIA 4
Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.
'''

# User input is a string 
user_input = input("Enter numbers separated by spaces: ")
# Turn user input into a list, and convert string elements to integers
num_list = list(map(int, user_input.split()))
# Sort list by ascending order
sorted_list = sorted(num_list)

print(f"Sorted numbers: {sorted_list}")
