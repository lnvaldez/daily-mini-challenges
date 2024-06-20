import string 
import random

class Color:
    GREEN_CLR = '\x1b[32m'
    END_CLR = '\033[0m'

def generate_password(length):
    if length < 8 or length > 16:
        raise ValueError("Password length must be between 8 and 16 characters")

    password = []

    # Ensure at least one character from each category is included
    password.append(random.choice(lower_case))
    password.append(random.choice(upper_case))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    # Fill the rest of the password length with random choices from all categories
    all_characters = lower_case + upper_case + digits + symbols
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    password = ''.join(password)

    return password

GREEN = Color.GREEN_CLR
END = Color.END_CLR

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

# Example 
# print(generate_password(16))

user_input = int(input("Enter a number between 8 and 16: "))
password = generate_password(user_input)

print(f"{GREEN}{password}{END}")
