from src.aho_korasik_alg import Automaton

'''
CCCA
3
C
CCA
CA
[(1, 'C'), (2, 'C'), (3, 'C'), (2, 'CCA'), (3, 'CA')]
'''


def test_valid_string(count, patterns, answer, text):
    patterns = patterns[1:-1]
    patterns = patterns.split(", ")
    pairs = {}
    for i in range(1, int(count) + 1):
        pairs.update({patterns[i - 1]: i})
    A = Automaton(list(pairs.keys()))
    print(answer)
    print(str(A.get_keywords_found(text)))
    assert answer == str(A.get_keywords_found(text))
