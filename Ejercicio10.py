# Create a Python decorator called timer that measures the time taken to execute a
# function. Use this decorator on a function that sorts a list of random numbers and
# prints the sorted list.

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Tiempo de ejecución: {:.6f} segundos".format(execution_time))
        return result
    return wrapper

@timer_decorator
def ordenar_e_imprimir(numeros):
    numeros_ordenados = sorted(numeros)
    print("Lista ordenada:", numeros_ordenados)

entrada = input("Ingresa una lista de números separados por espacios: ")
numeros = [int(num) for num in entrada.split()]

ordenar_e_imprimir(numeros)

