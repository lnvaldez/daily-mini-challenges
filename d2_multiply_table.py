'''
Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.
'''
from tabulate import tabulate

# ANSI Color Codes
class color:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

# Function to multiply a number 'x'
def multiplication_table(x):

    product_list = []

    # Multiply 'x' by 1-10
    for multiplier in range(1, 11):
        # Add result of multiplication to product_list
        product_list.append(x * multiplier)

    return product_list

# Get styling for odd and even numbers
EVEN_CLR = color.BLUE
ODD_CLR = color.YELLOW
# 'End' color and underline
END_CLR = color.ENDC
UNDERLINE = color.UNDERLINE

# User input
x = int(input("Enter a number: "))
product_list = multiplication_table(x)

# Table 
data = []
align = ["center"]
headers = [f"{UNDERLINE}Multiplication Table of {x}{END_CLR}"]

for i in range(1, 11):
    # Color even numbers with 'EVEN_CLR'
    # Color odd numbers with 'ODD_CLR'
    if x % 2 == 0:
        if i % 2 == 0:
            data.append([f'{EVEN_CLR}{x}{END_CLR} x {EVEN_CLR}{i}{END_CLR} = {EVEN_CLR}{product_list[i - 1]}{END_CLR}']) 
        else:
            data.append([f'{EVEN_CLR}{x}{END_CLR} x {ODD_CLR}{i}{END_CLR} = {EVEN_CLR}{product_list[i - 1]}{END_CLR}'])
    else:
        if i % 2 == 0:
            data.append([f'{ODD_CLR}{x}{END_CLR} x {EVEN_CLR}{i}{END_CLR} = {ODD_CLR}{product_list[i - 1]}{END_CLR}'])   
        else:
            data.append([f'{ODD_CLR}{x}{END_CLR} x {ODD_CLR}{i}{END_CLR} = {ODD_CLR}{product_list[i - 1]}{END_CLR}'])

# Print table
table = tabulate(data, headers, tablefmt="grid", colalign=align)
print(table)