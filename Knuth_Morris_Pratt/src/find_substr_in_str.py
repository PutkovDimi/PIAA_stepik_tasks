from .kmp_alg import kmp_find_occurrences

'''
This function is for processing data for specific stepik's task
'''


def process_answer(pattern, text):
    occurrences = kmp_find_occurrences(text, pattern)
    print(occurrences)
    if not occurrences:
        return -1
    else:
        return occurrences[:-1]
