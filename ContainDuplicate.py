def contains_duplicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Test cases
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 4]
nums3 = [1]
nums4 = []

# Check for duplicates and print results
print("nums1 contains duplicates:", contains_duplicate(nums1))
print("nums2 contains duplicates:", contains_duplicate(nums2))
print("nums3 contains duplicates:", contains_duplicate(nums3))
print("nums4 contains duplicates:", contains_duplicate(nums4))
