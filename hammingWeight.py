def hamming_weight(n):
    count = 0

    while n:
        count += n & 1
        n >>= 1

    return count


# Example usage:
n = 11
result = hamming_weight(n)
print(f"The number of set bits in {n} is: {result}")
