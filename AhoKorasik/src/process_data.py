from .aho_korasik_alg import Automaton


def process_data(text, n):
    pairs = {}
    for i in range(1, n + 1):
        pairs.update({str(input()): i})
    A = Automaton(list(pairs.keys()))
    return A.get_keywords_found(text)
