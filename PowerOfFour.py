def is_power_of_four(n):
    if n == 1:
        return True
    while n > 1:
        if n % 4 != 0:
            return False
        n //= 4
    return n == 1


def main():
    # Test cases
    test_cases = [1, 4, 16, 64, 2, 8, 32, 0, -4]

    for n in test_cases:
        print(f"Is {n} a power of four? {is_power_of_four(n)}")


if __name__ == "__main__":
    main()
