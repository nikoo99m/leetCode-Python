def find_single_num(nums):
    result = 0
    for i in range(len(nums)):
        result ^= nums[i]
    return result


# Example usage
nums = [4, 1, 2, 1, 2]
print(find_single_num(nums))  # Output: 4
