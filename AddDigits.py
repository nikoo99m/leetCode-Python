class AddDigits:
    def add_digits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


if __name__ == "__main__":
    add_digits_instance = AddDigits()

    # Test cases
    num1 = 38
    result1 = add_digits_instance.add_digits(num1)
    print(f"The digital root of {num1} is: {result1}")

    num2 = 123
    result2 = add_digits_instance.add_digits(num2)
    print(f"The digital root of {num2} is: {result2}")

    num3 = 0
    result3 = add_digits_instance.add_digits(num3)
    print(f"The digital root of {num3} is: {result3}")

    num4 = 9
    result4 = add_digits_instance.add_digits(num4)
    print(f"The digital root of {num4} is: {result4}")
