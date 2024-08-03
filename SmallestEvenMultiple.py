def smallest_even_multiple(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2


# Test cases
test_cases = [1, 2, 3, 4, 5, 6, 10, 15]

for n in test_cases:
    print(f"The smallest even multiple of {n} is: {smallest_even_multiple(n)}")
