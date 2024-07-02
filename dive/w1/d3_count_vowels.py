'''
DIA 3
Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.
'''

def count_vowels(text):

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    text = text.lower()

    for letter in text:
        if letter in vowels:
            vowel_count += 1

    return vowel_count

print("** Count Vowels **")
txt_input = str(input("Your Input: "))
print(count_vowels(txt_input))