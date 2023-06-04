#Create a Python program that checks if a given number is prime or not. 
#The user should input a number, and the program should print whether it is prime or not.

def primo(number):
    if number <= 1:
        return False
    
    for i in range (2, number):
        if number % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    number = int(input("Ingresa un número: "))    

    if primo(number):
        print(number,"es un número primo.")
    else:
        print(number, "no es un número primo.")

