def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Test cases
nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums4 = [0]

print(f"Missing number in {nums1}: {missing_number(nums1)}")
print(f"Missing number in {nums2}: {missing_number(nums2)}")
print(f"Missing number in {nums3}: {missing_number(nums3)}")
print(f"Missing number in {nums4}: {missing_number(nums4)}")
