nums = [2, 7, 11, 15, 4, 10]
target = 12
s = [0, 0]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            s[0] = i
            s[1] = j
            break

# Print the result
print(s)