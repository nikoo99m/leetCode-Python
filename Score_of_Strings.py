class ScoreOfAString:
    def score_of_string(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score


if name == "main":
    scorer = ScoreOfAString()

    test1 = "abc"
    test2 = "abcd"
    test3 = "aA"
    test4 = "123"
    test5 = "AAB"

    print(f"Score of '{test1}': {scorer.score_of_string(test1)}")
    print(f"Score of '{test2}': {scorer.score_of_string(test2)}")
    print(f"Score of '{test3}': {scorer.score_of_string(test3)}")
    print(f"Score of '{test4}': {scorer.score_of_string(test4)}")
    print(f"Score of '{test5}': {scorer.score_of_string(test5)}")
