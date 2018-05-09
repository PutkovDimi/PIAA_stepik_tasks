def kmp_find_occurrences(text, pattern):
    d = {0: 0}
    occurrences = []
    template = pattern + '#' + text
    for i in range(1, len(template)):
        j = d[i - 1]
        while j > 0 and template[j] != template[i]:
            j = d[j - 1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(pattern):
            occurrences.append(i - j * 2)
            print(occurrences)
    return occurrences
