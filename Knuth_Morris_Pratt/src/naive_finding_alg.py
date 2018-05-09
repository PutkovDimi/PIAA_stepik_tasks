def naive_string_matcher(pattern, text):
    n = len(text)
    m = len(pattern)
    ans = []
    for i in range(0, n - m):
        if pattern in text[i:i + m]:
            ans.append(i)
    return ans