def isPowerOfTwo(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


print(isPowerOfTwo(1))  # True
print(isPowerOfTwo(2))  # True
print(isPowerOfTwo(3))  # False
print(isPowerOfTwo(4))  # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(18))  # False
print(isPowerOfTwo(0))  # False
print(isPowerOfTwo(-16))  # False
