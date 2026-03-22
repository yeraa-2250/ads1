import math

def print_digits(n):
    n = abs(n)
    if n < 10:
        print(n)
        return
    print_digits(n // 10)
    print(n % 10)




def recursive_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index + 1)




def average(arr):
    if len(arr) == 0:
        return 0
    return recursive_sum(arr) / len(arr)

def is_prime_recursive(n, divisor=2):
    if n < 2:
        return False
    if divisor > math.isqrt(n):
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)



def reverse_print(nums, n, index=0):
    if index == n:
        return
    x = int(input())
    reverse_print(nums, n, index + 1)
    print(x)




def only_digits(s, index=0):
    if index == len(s):
        return True
    if not s[index].isdigit():
        return False
    return only_digits(s, index + 1)



def count_chars(s):
    if s == "":
        return 0
    return 1 + count_chars(s[1:])


# Task 10. GCD using Euclidean algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# ---------------- DEMONSTRATION ----------------

def run_all_tasks():
    print("Task 1: Print Digits of a Number")
    n1 = int(input("Enter number: "))
    print_digits(n1)

    print("\nTask 2: Average of Elements")
    size = int(input("Enter number of elements: "))
    arr = read_array_rec(size)
    print(average(arr))

    print("\nTask 3: Prime Number Check")
    n3 = int(input("Enter number: "))
    print("Prime" if is_prime_recursive(n3) else "Composite")

    print("\nTask 4: Factorial")
    n4 = int(input("Enter number: "))
    print(factorial(n4))

    print("\nTask 5: Fibonacci Number")
    n5 = int(input("Enter n: "))
    print(fibonacci(n5))

    print("\nTask 6: Power Function")
    a = int(input("Enter base: "))
    n6 = int(input("Enter power: "))
    print(power(a, n6))

    print("\nTask 7: Reverse Output")
    n7 = int(input("Enter count of numbers: "))
    reverse_print([], n7)

    print("\nTask 8: Check Digits in String")
    s8 = input("Enter string: ")
    print("Yes" if only_digits(s8) else "No")

    print("\nTask 9: Count Characters in a String")
    s9 = input("Enter string: ")
    print(count_chars(s9))

    print("\nTask 10: Greatest Common Divisor (GCD)")
    a10 = int(input("Enter first number: "))
    b10 = int(input("Enter second number: "))
    print(gcd(a10, b10))


# Recursive input of array without loops
def read_array_rec(n, index=0, arr=None):
    if arr is None:
        arr = []
    if index == n:
        return arr
    arr.append(int(input(f"Element {index + 1}: ")))
    return read_array_rec(n, index + 1, arr)


run_all_tasks()