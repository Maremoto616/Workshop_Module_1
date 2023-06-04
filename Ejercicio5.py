# Write a Python function called find_maximum that takes a list of numbers as input
# and returns the maximum number from the list.

numbers = input("Ingresa una lista de números enteros por espacios: ").split() #se utiliza el método split() para dividir la entrada en una lista de cadenas

def find_maximum(numbers):
    if not numbers:
        return None
    
    numbers = [int(num) for num in numbers] #se utiliza una comprensión de lista para convertir cada cadena en un número entero
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

maximum_number = find_maximum(numbers)
print("Maximum number:", maximum_number)