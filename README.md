# 🐧 Daily Mini-Challenges

<details>
  <summary>Today's Mini-Challenge</summary>

```python
class Color:

  MAGENTA = '\x1b[35m'
  CYAN = '\x1b[36m'
  ENDC = '\033[0m'

def check_temp(temp):

  if temp > 95 and temp < 140:
      return '🥵'
  elif temp > 60 and temp < 100:
      return '😁'
  elif temp > 20 and temp < 60:
      return '🥶'
  else:
      return '💀'

def celsius_to_fahrenheit(temp_in_celsius):

   fahrenheit = (temp_in_celsius * 9/5) + 32

   return fahrenheit

MAGENTA_CLR = Color.MAGENTA
CYAN_CLR = Color.CYAN
END_CLR = Color.ENDC

user_input = int(input("Enter temperature in celsius: "))

fahrenheit = celsius_to_fahrenheit(user_input)
temp_eval = check_temp(fahrenheit)

print(f'{MAGENTA_CLR}{user_input} °C{END_CLR} = {CYAN_CLR}{fahrenheit} °F{END_CLR} {temp_eval}')

```

</details>

## - ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Week 1` \* June 11-14

| 📅 Date  | 🏆 Challenge                     | 🗂️ File                                                                                                       |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ⛓️ 06/11 | **Day 1** - Reverse String       | [`d1_reverse_string.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d1_reverse_string.py) |
| ✖️ 06/12 | **Day 2** - Multiplication Table | [`d2_multiply_table.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d2_multiply_table.py) |
| 🅰️ 06/13 | **Day 3** - Count Vowels         | [`d3_count_vowels.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d3_count_vowels.py)     |
| 📦 06/14 | **Day 4** - Sort List            | [`d4_sort_list.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d4_sort_list.py)           |

## - ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Week 2` \* June 17-21

| 📅 Date  | 🏆 Challenge                      | 🗂️ File                                                                                                                  |
| -------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 📙 06/17 | **Day 5** - List to Dictionary    | [`d5_list_to_dict.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d5_list_to_dict.py)                   |
| 🌡️ 06/18 | **Day 6** - Celsius to Fahrenheit | [`d6_celsius_to_fahrenheit.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d6_celsius_to_fahrenheit.py) |

---
