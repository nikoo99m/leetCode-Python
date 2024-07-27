def sumBase(n, k):

    base_k_number = []
    while n > 0:
        base_k_number.append(n % k)
        n //= k

    digit_sum = sum(base_k_number)

    return digit_sum


# Test cases
print(sumBase(34, 6))
print(sumBase(10, 10))
print(sumBase(255, 16))
