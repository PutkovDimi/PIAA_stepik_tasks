from .get_partial import get_partial


def search(text, pattern):
    pattern = pattern * 2
    partial = get_partial(pattern)
    j = 0
    for i in range(len(pattern)):
        while j > 0 and pattern[i] != text[j]:
            j = partial[j - 1]
        if text[j] == pattern[i]:
            j += 1
        if j == len(text):
            return i - (j - 1)
    return -1
