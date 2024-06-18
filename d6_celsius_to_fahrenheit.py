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
