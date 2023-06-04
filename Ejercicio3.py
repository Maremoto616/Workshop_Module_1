# Write a Python program that prints the first 10 Fibonacci numbers using a loop.

def fibonacci(n):
    list_num = [0 , 1]
    print(list_num [0])
    print(list_num[1])

    for i in range (2, n):
        fibonacci_num = list_num [i - 1] + list_num[i - 2]
        list_num.append(fibonacci_num)
        print(fibonacci_num)

fibonacci(10)

