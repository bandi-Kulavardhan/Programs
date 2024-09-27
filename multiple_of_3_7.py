def multiple_check(a,b):
    if a%3 == 0 or a%7 == 0 or b%3 == 0 or b%7 == 0:
        return True
    return False
a,b = int(input()),int(input())
print(multiple_check(a,b))