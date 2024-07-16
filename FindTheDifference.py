def findTheDifference(s: str, t: str) -> str:
    result = 0

    # XOR all characters in s
    for char in s:
        result ^= ord(char)

    # XOR all characters in t
    for char in t:
        result ^= ord(char)

    # The result will be the ASCII value of the additional character
    return chr(result)


# Example usage
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))  # Output: "e"
