# Problem: Multiple of 3 or 7
# Task: Write a function that returns True if either integer is a multiple of 3 or 7, otherwise False.

# Test Cases:
# ● Input: 9, 4 -> Output: True
# ● Input: 5, 10 -> Output: False
# ● Input: 8, 11 -> Output: False

def multiple_check(a,b):
    if a%3 == 0 or a%7 == 0 or b%3 == 0 or b%7 == 0:
        return True
    return False
a,b = int(input()),int(input())
print(multiple_check(a,b))