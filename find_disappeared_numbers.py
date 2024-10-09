def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

    return result


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    missing_numbers = findDisappearedNumbers(nums)

    print("Missing numbers:", missing_numbers)
