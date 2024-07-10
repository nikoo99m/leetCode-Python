class HappyNumber:
    def is_happy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)

        return n == 1

    def get_next(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % 10
            n //= 10
            total_sum += digit * digit
        return total_sum


if __name__ == "__main__":
    happy_number = HappyNumber()
    test_number = 19

    if happy_number.is_happy(test_number):
        print(f"{test_number} is a happy number.")
    else:
        print(f"{test_number} is not a happy number.")
