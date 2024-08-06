def common_factors(a, b):
    count = 0
    min_val = min(a, b)
    for i in range(1, min_val + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count


# Test cases
a = 12
b = 18
result = common_factors(a, b)
print(f"Number of common factors of {a} and {b}: {result}")

c = 100
d = 75
result2 = common_factors(c, d)
print(f"Number of common factors of {c} and {d}: {result2}")
