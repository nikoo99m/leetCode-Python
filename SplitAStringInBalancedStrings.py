def balancedStringSplit(s: str) -> int:
    balance = 0
    count = 0

    for char in s:
        if char == "L":
            balance += 1
        else:
            balance -= 1

        # When balance is zero, we have a balanced substring
        if balance == 0:
            count += 1

    return count


test_string = "RLRRLLRLRL"
result = balancedStringSplit(test_string)
print(result)
