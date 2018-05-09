from ..src.kmp_alg import kmp_find_occurrences as kmp


#    kmp('a', 'bbb')== []
#    kmp('ab', 'abababababababab')== '[0, 2, 4, 6, 8, 10, 12, 14]'
#    kmp(' ', 'alkcskvlskvlsv')== []
#    kmp('s', '') == []
#    kmp('', 'aaa') == '[1, 2, 3]'

def test_valid_string(pattern, answer, text):
    assert answer == str(kmp(pattern=pattern,
                             text=text))
