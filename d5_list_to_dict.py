'''
DIA 5
Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.
'''

class Color:
    ENDC = '\033[0m'
    GREEN = '\x1b[32m'
    RED = '\x1b[31m'
    BG_GRAY = '\x1b[47m'
    BG_RED = '\x1b[41m'

def warning():
    print(f"""
{Color.BG_RED}!WARNING{Color.ENDC}
{Color.RED}Keys or values that contain spaces in them must be separated with "-".
Example: Write "Last-Name" instead of "Last Name".{Color.ENDC}
***-***-***""")

def list_to_dict(key_list, value_list, item):
    dictionary = {}
    len_key_list = len(key_list)
    len_value_list = len(value_list)

    if len_key_list != len_value_list:
        raise TypeError(f"{Color.BG_RED}Length of both lists must be the same.{Color.ENDC}")
    elif len_key_list != item or len_value_list != item:
        if len_key_list > item:
            raise TypeError(
                f"{Color.BG_RED}Too many keys or values. Promised {item} items, got {len_key_list} keys and "
                f"{len_value_list} values.{Color.ENDC}"
            )
        if len_key_list < item:
            raise TypeError(
                f"{Color.BG_RED}Not enough keys or values. Promised {item} items, got {len_key_list} keys and "
                f"{len_value_list} values.{Color.ENDC}"
            )
    else:
        for index in range(item):
            dictionary[key_list[index]] = value_list[index]
    return dictionary

GREEN = Color.GREEN
RED = Color.RED
END_CLR = Color.ENDC
BG_GRAY = Color.BG_GRAY
BG_RED = Color.BG_RED

# Sample
# item = 3 
# key_list = ['Name', 'Last-Name', 'Location']
# value_list = ['Lucas', 'Valdez', 'Luque']

warning()

item = int(input('Enter item amount for dictionary: '))

print(f'{GREEN}Separate inputs with spaces{END_CLR}')

key_input = input('🔑 Enter keys for dictionary: ')
key_list = list(key_input.split())

value_input = input('✴️ Enter values for dictionary: ')
value_list = list(value_input.split())

key_value_dict = list_to_dict(key_list=key_list, value_list=value_list, item=item)

print(f'📙 {BG_GRAY}Dictionary{END_CLR}')
for key, value in key_value_dict.items():
    print(f'{GREEN}{key}:{END_CLR} {value}')
