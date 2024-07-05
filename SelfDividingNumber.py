def self_dividing_numbers(left, right):
    def is_self_dividing(num):
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                return False
            temp //= 10
        return True

    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result


if __name__ == "__main__":
    left = 1
    right = 22
    result = self_dividing_numbers(left, right)

    print(f"Self-dividing numbers between {left} and {right}:")
    print(result)
