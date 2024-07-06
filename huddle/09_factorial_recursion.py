'''
09. Recursión Factorial: Implementa una función recursiva para 
calcular el factorial de un número pequeño (por ejemplo, 5).
'''

def factorial(x, n):
    if n == 1:
        return x
    else:
        a = x * n 
        return factorial(a, n - 1)

user_input = int(input("Enter a number: "))
n = factorial(1, user_input)

print(f"{user_input}! = {n}")

factorial_sequence = []

for i in range(1, user_input + 1):
    factorial_sequence.append(str(i))

print(f"{' X '.join(factorial_sequence)} = {n}")