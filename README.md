# 🐧 Daily Mini-Challenges

<details>
  <summary>Today's Mini-Challenge</summary>

```python
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

```

</details>

## <span style="color: #1589F0;">🔷</span> `Week 1` \* June 11-14

| 📅 Date  | 🏆 Challenge                     | 🗂️ File                                                                                                       |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ⛓️ 06/11 | **Day 1** - Reverse String       | [`d1_reverse_string.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d1_reverse_string.py) |
| ✖️ 06/12 | **Day 2** - Multiplication Table | [`d2_multiply_table.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d2_multiply_table.py) |
| 🅰️ 06/13 | **Day 3** - Count Vowels         | [`d3_count_vowels.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d3_count_vowels.py)     |
| 📦 06/14 | **Day 4** - Sort List            | [`d4_sort_list.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d4_sort_list.py)           |

## <span style="color: #1589F0;">🔷</span> `Week 2` \* June 17-21

| 📅 Date  | 🏆 Challenge                        | 🗂️ File                                                                                                                  |
| -------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 📙 06/17 | **Day 5** - List to Dictionary      | [`d5_list_to_dict.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d5_list_to_dict.py)                   |
| 🌡️ 06/18 | **Day 6** - Celsius to Fahrenheit   | [`d6_celsius_to_fahrenheit.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d6_celsius_to_fahrenheit.py) |
| ✊ 06/19 | **Day 7** - Rock, Paper, Scissors   | [`d7_rps.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d7_rps.py)                                     |
| 🔒 06/20 | **Day 8** - Safe Password Generator | [`d8_safe_password.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d8_safe_password.py)                 |

---
