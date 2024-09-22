### IS NUMBER PRIME --- test question / project inside UDEMY
def is_prime(num):
    for x in range (2, int((num * 0.50) + 1)):
        if num % x == 0:
            return False
    else:
        return True
print(is_prime(13))

