def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_array = sorted(s)
    t_array = sorted(t)

    return s_array == t_array


test_cases = [
    ("anagram", "nagaram"),
    ("rat", "car"),
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pale"),
]

for s, t in test_cases:
    print(f'Are "{s}" and "{t}" anagrams? {is_anagram(s, t)}')
