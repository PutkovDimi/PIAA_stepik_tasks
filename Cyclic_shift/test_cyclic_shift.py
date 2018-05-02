from src.search import search


def test_if_correct():
    assert search('aaa', 'aaa') == 0


def test_if_correct_2():
    assert search(pattern='defabc', text='abcdef') == 3


def test_if_wrong():
    assert search(pattern='defabf', text='abcdef') == -1


def test_if_pattern_empty():
    assert search(pattern='', text='fld;fld') == -1