# 🐧 Daily Mini-Challenges

<details>
  <summary>Today's Mini-Challenge</summary>

```c++
#include <iostream>
#include <algorithm>
#include <cctype>
#include <string>

int main()
{
    std::string str;

    std::cout << "Enter your string: ";
    std::getline(std::cin, str);

    // Create a copy of the original string for transformation
    std::string rev_str = str;

    // Transform both strings to lowercase
    std::transform(str.begin(), str.end(), str.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    std::transform(rev_str.begin(), rev_str.end(), rev_str.begin(),
                   [](unsigned char c) { return std::tolower(c); });

    // Remove non-alphanumeric characters from both strings
    str.erase(std::remove_if(str.begin(), str.end(),
               [](unsigned char c) { return !std::isalnum(c); }), str.end());
    rev_str.erase(std::remove_if(rev_str.begin(), rev_str.end(),
               [](unsigned char c) { return !std::isalnum(c); }), rev_str.end());

    // Reverse the string for comparison
    std::reverse(rev_str.begin(), rev_str.end());

    // Compare the original string with the reversed string
    if (str == rev_str)
    {
        std::cout << "Palindrome";
    }
    else
    {
        std::cout << "Not a palindrome";
    }

    std::cout << std::endl;

    return 0;
}
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

| 📅 Date  | 🏆 Challenge                        | 🗂️ File                                                                                                                     |
| -------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 📙 06/17 | **Day 5** - List to Dictionary      | [`d5_list_to_dict.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w2/d5_list_to_dict.py)                   |
| 🌡️ 06/18 | **Day 6** - Celsius to Fahrenheit   | [`d6_celsius_to_fahrenheit.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w2/d6_celsius_to_fahrenheit.py) |
| ✊ 06/19 | **Day 7** - Rock, Paper, Scissors   | [`d7_rps.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w2/d7_rps.py)                                     |
| 🔒 06/20 | **Day 8** - Safe Password Generator | [`d8_safe_password.py`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w2/d8_safe_password.py)                 |
| ➕ 06/21 | **Day 9** - Sum                     | [`d9_sum.cpp`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w2/d9_sum.cpp)                                   |

---

## <span style="color: #1589F0;">🔷</span> `Week 3` \* June 24-25

| 📅 Date  | 🏆 Challenge                  | 🗂️ File                                                                                                               |
| -------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 📈 06/24 | **Day 10** - Order Array      | [`d10_order_array.cpp`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w3/d10_order_array.cpp)           |
| ✅ 06/25 | **Day 11** - Check Palindrome | [`d11_check_palindrome.cpp`](https://github.com/lnvaldez/Daily-Mini-Challenges/blob/main/w3/d11_check_palindrome.cpp) |
