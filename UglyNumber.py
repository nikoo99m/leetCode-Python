def isUgly(num):
    if num <= 1:
        return True
    for factor in [2, 3, 5]:
        while num % factor == 0:
            num //= factor

    return num == 1


print(isUgly(6))
print(isUgly(121))
print(isUgly(14))
print(isUgly(1))
