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



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



def read_array_rec(n, index=0, arr=None):
    if arr is None:
        arr = []
    if index == n:
        return arr
    arr.append(int(input(f"Element {index + 1}: ")))
    return read_array_rec(n, index + 1, arr)