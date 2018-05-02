from src.find_substr_in_str import process_answer as kmp


def test_kmp_find_occurrences_wrong():
    assert kmp('a', 'bbb') == -1


def test_kmp_find_occurrences_correct_1():
    assert kmp('a', 'aaaaaaaaaaa') == '0,1,2,3,4,5,6,7,8,9,10'


def test_kmp_find_occurrences_correct_2():
    assert kmp('ab', 'abababababababab') == '0,2,4,6,8,10,12,14'


def test_kmp_find_occurrences_whitespace():
    assert kmp(' ', 'alkcskvlskvlsv') == -1


def test_kmp_find_occurrences_empty_pattern():
    assert kmp('', 'aaa') == '1,2,3'


def test_kmp_find_occurrences_empty_text():
    assert kmp('s', '') == -1