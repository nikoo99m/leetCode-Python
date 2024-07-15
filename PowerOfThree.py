def is_power_of_three(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    while n > 1:
        if n % 3 != 0:
            return False
        n //= 3
    return True


test_numbers = [1, 3, 9, 27, 81, 0, -3, 10, 45]

for number in test_numbers:
    print(f"Is {number} a power of three? {is_power_of_three(number)}")
