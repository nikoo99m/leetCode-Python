def is_perfect_square(num):
    if num < 1:
        return False  # Add a check for numbers less than 1

    for i in range(1, num // 2 + 1):
        if i * i == num:
            return True
    return False


# Test cases
test_numbers = [1, 4, 9, 16, 25, 36, 49, 50, 64, 81, 100, 144, 200, 225, 256, 300]

for num in test_numbers:
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")
