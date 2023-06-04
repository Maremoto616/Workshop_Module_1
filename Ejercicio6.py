# Create a Python function called reverse_string that takes a string as input and returns the reversed string.

string = input("Escriba palabra: ")

def reverse_string(string):
    reverse_string = string[::-1] #se utiliza la sintaxis de rebanado (slicing) con [::-1] para obtener una versión invertida de la cadena
    return reverse_string

reversed_str = reverse_string(string)
print("Palabra al revés:", reversed_str)