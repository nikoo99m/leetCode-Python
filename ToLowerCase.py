def to_lower_case(s):
    result = []

    for c in s:
        if "A" <= c <= "Z":

            result.append(chr(ord(c) + (ord("a") - ord("A"))))
        else:

            result.append(c)

    return "".join(result)


# Example usage
s = "Hello, WORLD!"
result = to_lower_case(s)
print(result)
