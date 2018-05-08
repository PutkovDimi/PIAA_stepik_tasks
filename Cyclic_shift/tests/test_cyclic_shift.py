from src.search import search


# search('aaa', 'aaa') == 0
# search(pattern='defabc', text='abcdef') == 3
# search(pattern='defabf', text='abcdef') == -1
# search(pattern='', text='fld;fld') == -1

def test_valid_string(pattern, answer, text):
    assert str(answer) == str(search(pattern=pattern,
                                     text=text))
