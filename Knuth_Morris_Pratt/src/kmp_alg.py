def kmp_find_occurrences(s, x):
    d = {0: 0}
    occurrences = str()
    template = x + '#' + s
    for i in range(1, len(template)):
        j = d[i - 1]
        while j > 0 and template[j] != template[i]:
            j = d[j - 1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(x):
            occurrences += str((i - j * 2)) + ','
    return occurrences
