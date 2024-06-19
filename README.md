<h1 style="background: linear-gradient(to right, #a1c4fd, #c2e9fb); color: white; padding: 20px; border-radius: 10px; text-align: center;">
  🐧 Daily Mini-Challenges
</h1>

<details style="border: 1px solid #ccc; padding: 10px; margin-bottom:15px;border-radius: 5px;">
  <summary style="font-size: 18px; font-weight: bold; cursor: pointer; color: #007bff; ">Today's Mini-Challenge</summary>

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

<div style="font-family: Arial, sans-serif; padding: 20px; border-radius: 10px; border: 0.5px solid #ccc; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">

## <span style="color: #1589F0;">🔷</span> `Week 1` \* June 11-14

| 📅 Date  | 🏆 Challenge                     | 🗂️ File                                                                                                       |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ⛓️ 06/11 | **Day 1** - Reverse String       | [`d1_reverse_string.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d1_reverse_string.py) |
| ✖️ 06/12 | **Day 2** - Multiplication Table | [`d2_multiply_table.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d2_multiply_table.py) |
| 🅰️ 06/13 | **Day 3** - Count Vowels         | [`d3_count_vowels.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d3_count_vowels.py)     |
| 📦 06/14 | **Day 4** - Sort List            | [`d4_sort_list.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w1/d4_sort_list.py)           |

## <span style="color: #1589F0;">🔷</span> `Week 2` \* June 17-21

| 📅 Date  | 🏆 Challenge                      | 🗂️ File                                                                                                                  |
| -------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 📙 06/17 | **Day 5** - List to Dictionary    | [`d5_list_to_dict.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d5_list_to_dict.py)                   |
| 🌡️ 06/18 | **Day 6** - Celsius to Fahrenheit | [`d6_celsius_to_fahrenheit.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/d6_celsius_to_fahrenheit.py) |

---

</div>
