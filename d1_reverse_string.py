'''
DIA 1
Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario.
'''

def reverse_string(text):

    if len(text) == 0:
        return ""
    else:
        return text[-1] + reverse_string(text[:-1])
    
text = str(input("Enter a string: "))    
reversed_text = reverse_string(text)

print(reversed_text)
