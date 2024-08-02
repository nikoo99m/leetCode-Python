def percentage_letter(s: str, letter: str) -> int:
    count = s.count(letter)
    # Calculate percentage and use integer division to round down
    percentage = (count * 100) // len(s)
    return percentage


if __name__ == "__main__":
    s1 = "hello"
    letter1 = "l"
    result1 = percentage_letter(s1, letter1)
    print(f"Percentage of 'l' in 'hello': {result1}%")

    s2 = "world"
    letter2 = "o"
    result2 = percentage_letter(s2, letter2)
    print(f"Percentage of 'o' in 'world': {result2}%")

    s3 = "openai"
    letter3 = "p"
    result3 = percentage_letter(s3, letter3)
    print(f"Percentage of 'p' in 'openai': {result3}%")

    s4 = "aaaabbbb"
    letter4 = "a"
    result4 = percentage_letter(s4, letter4)
    print(f"Percentage of 'a' in 'aaaabbbb': {result4}%")

    s5 = "percentage"
    letter5 = "z"
    result5 = percentage_letter(s5, letter5)
    print(f"Percentage of 'z' in 'percentage': {result5}%")
