def count_even_digit_numbers(nums):
    def is_even_digit_count(n):
        return len(str(abs(n))) % 2 == 0

    count = 0
    for num in nums:
        if is_even_digit_count(num):
            count += 1

    return count


nums = [12, 345, 2, 6, 7896]
print(count_even_digit_numbers(nums))
