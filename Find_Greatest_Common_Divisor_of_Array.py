def find_gcd(nums):
    def gcd(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    min_num = float("inf")
    max_num = float("-inf")

    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return gcd(min_num, max_num)


# Example usage
if __name__ == "__main__":
    nums = [2, 5, 6, 9, 10]
    result = find_gcd(nums)
    print(f"The GCD of the smallest and largest number in the array is: {result}")
