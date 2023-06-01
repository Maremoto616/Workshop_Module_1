#2.  Create a Python program that converts a temperature from Fahrenheit to Celsius. 
# The user should enter the temperature in Fahrenheit, and the program should print
# the equivalent temperature in Celsius.

def f_to_c(fa):
    ce = (fa - 32)*5/9
    return ce

fa = float(input("Indica la temperatura en Fahrenheit: "))
ce = f_to_c(fa)

print ("El cambio de Fahrenheit a celsius es: ", int(ce))