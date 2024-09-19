def commonChars(words):

    result = list(words[0])

    for word in words[1:]:
        new_result = []
        for char in word:
            if char in result:
                new_result.append(char)
                result.remove(char)
        result = new_result

    return result


# Example usage
words = ["bella", "label", "roller"]
print(commonChars(words))  # Output: ['e', 'l', 'l']
