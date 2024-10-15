def get_smallest_string(word, substr):
    word_length = len(word)
    substr_length = len(substr)
    result = None

    for i in range(word_length - substr_length + 1):
        candidate = list(word)

        for j in range(substr_length):
            word_char = word[i + j]
            substr_char = substr[j]

            if word_char != "?" and word_char != substr_char:
                can_fit = False
                break
            candidate[i + j] = substr_char

        if can_fit:
            for k in range(word_length):
                if candidate[k] == "?":
                    candidate[k] = "a"

            candidate_str = "".join(candidate)
            if result is None or candidate_str < result:
                result = candidate_str

    return result if result is not None else "-1"


if __name__ == "__main__":
    word = "as?b?e?gf"
    substr = "dbk"
    print(get_smallest_string(word, substr))
