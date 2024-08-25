class RemoveAllAdjacentDuplicatesInString:
    def removeDuplicates(self, s: str) -> str:
        word = []

        for char in s:
            if word and word[-1] == char:
                word.pop()
            else:
                word.append(char)

        return "".join(word)


# Example usage
if __name__ == "__main__":
    solution = RemoveAllAdjacentDuplicatesInString()

    input_string = "abbaca"
    result = solution.removeDuplicates(input_string)

    print("Final string after all duplicate removals:", result)
