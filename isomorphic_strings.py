def isIsomorphic(s: str, t: str) -> bool:

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):

        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True


# Example usage of isIsomorphic function

print(isIsomorphic("egg", "add"))  # Output: True
print(isIsomorphic("foo", "bar"))  # Output: False
print(isIsomorphic("paper", "title"))  # Output: True
print(isIsomorphic("abc", "def"))  # Output: True
print(isIsomorphic("abc", "ab"))  # Output: False
print(isIsomorphic("", ""))  # Output: True
print(isIsomorphic("ab", "aa"))  # Output: False
print(isIsomorphic("aabbcc", "xxyyzz"))  # Output: True
print(isIsomorphic("abc", "aaa"))  # Output: False
