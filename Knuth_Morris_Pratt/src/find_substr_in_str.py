from src.kmp_alg import kmp_find_occurrences


def process_answer(pattern, text):
    occurrences = kmp_find_occurrences(text, pattern)
    if not occurrences:
        return -1
    else:
        return occurrences[:-1]